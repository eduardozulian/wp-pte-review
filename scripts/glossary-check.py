#!/usr/bin/env python3
"""Cruza as traduções de um arquivo .po com o glossário pt-BR do WordPress.org.

Lista CANDIDATOS a desvio do glossário: strings em que um termo do glossário
aparece no texto original, mas a tradução não contém o termo esperado (nem uma
forma flexionada dele). O resultado é uma lista para revisão, não um veredito:
desvios justificados pelo contexto são aceitáveis.

Uso:
    python3 glossary-check.py ARQUIVO.po [--projeto wp-plugins/SLUG]
                              [--glossario ARQUIVO_OU_URL]

Sem --glossario, baixa o glossário geral pt-BR. Com --projeto, também tenta
baixar o glossário específico do projeto; os termos dele têm prioridade sobre
os do glossário geral.
"""

import argparse
import csv
import io
import re
import sys
import unicodedata
import urllib.error
import urllib.request

GLOSSARIO_GERAL = "https://translate.wordpress.org/locale/pt-br/default/glossary/-export/"
GLOSSARIO_PROJETO = "https://translate.wordpress.org/projects/{projeto}/pt-br/default/glossary/-export/"
PALAVRAS_VAZIAS = {"a", "o", "as", "os", "de", "da", "do", "das", "dos", "e", "em",
                   "no", "na", "nos", "nas", "para", "por", "um", "uma", "com", "ou"}


# ---------------------------------------------------------------- leitura

def carregar_texto(origem):
    if re.match(r"https?://", origem):
        req = urllib.request.Request(origem, headers={"User-Agent": "wp-pte-review"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8")
    with open(origem, encoding="utf-8") as f:
        return f.read()


def ler_glossario(texto):
    """Devolve {termo_en_minusculo: {"en", "alternativas", "descricoes"}}."""
    termos = {}
    for linha in csv.DictReader(io.StringIO(texto)):
        en = (linha.get("en") or "").strip()
        if not en:
            continue
        item = termos.setdefault(en.lower(), {"en": en, "alternativas": [], "descricoes": [],
                                              "classes": set()})
        pt = (linha.get("pt-br") or "").strip()
        if pt and pt not in item["alternativas"]:
            item["alternativas"].append(pt)
        desc = (linha.get("description") or "").strip()
        classe = (linha.get("pos") or "").strip()
        item["classes"].add(classe)
        nota = f"{classe}: {desc}" if desc else classe
        if nota and nota not in item["descricoes"]:
            item["descricoes"].append(nota)
    return termos


def _desescapar(s):
    return re.sub(r'\\(.)', lambda m: {"n": "\n", "t": "\t"}.get(m.group(1), m.group(1)), s)


def ler_po(texto):
    """Devolve lista de pares (original, tradução), incluindo formas de plural."""
    entradas, atual, campo = [], {}, None

    def fechar():
        if atual.get("msgid"):
            entradas.append(dict(atual))
        atual.clear()

    for linha in texto.splitlines():
        linha = linha.strip()
        if not linha:
            fechar()
            campo = None
            continue
        if linha.startswith("#"):
            if atual.get("msgstr") is not None or any(k.startswith("msgstr[") for k in atual):
                fechar()
            continue
        m = re.match(r'(msgctxt|msgid_plural|msgid|msgstr(?:\[\d+\])?)\s+"(.*)"$', linha)
        if m:
            if m.group(1) in ("msgctxt", "msgid") and any(k.startswith("msgstr") for k in atual):
                fechar()
            campo = m.group(1)
            atual[campo] = _desescapar(m.group(2))
        elif linha.startswith('"') and campo:
            atual[campo] += _desescapar(linha[1:-1])
    fechar()

    pares = []
    for e in entradas:
        if "msgstr" in e:
            pares.append((e["msgid"], e["msgstr"]))
        else:
            pares.append((e["msgid"], e.get("msgstr[0]", "")))
            if "msgid_plural" in e:
                pares.append((e["msgid_plural"], e.get("msgstr[1]", "")))
    return [(o, t) for o, t in pares if t.strip()]


# ---------------------------------------------------------------- comparação

def limpar(texto):
    """Remove tags HTML e placeholders, para não casar termos dentro de código."""
    texto = re.sub(r"<[^>]+>", " ", texto)
    return re.sub(r"%(\d+\$)?[sdfu@]|===\w+===", " ", texto)


def normalizar_pt(texto):
    sem_acento = "".join(c for c in unicodedata.normalize("NFKD", texto.lower())
                         if not unicodedata.combining(c))
    return re.sub(r"(oes|aes)\b", "ao", sem_acento)  # ações/ação, padrões/padrão


def radical(palavra):
    return palavra if len(palavra) <= 4 else palavra[:max(4, len(palavra) - 3)]


def regex_termo_en(termo, classes):
    """Casa o termo com plural; formas verbais (-ed, -ing) só se ele puder ser verbo."""
    partes = [re.escape(p) for p in termo.split()]
    so_substantivo = classes == {"noun"}
    sufixo = "(?:s|es)?" if len(termo) <= 3 or so_substantivo else "(?:s|es|d|ed|ing)?"
    return re.compile(r"\b" + r"[\s-]+".join(partes) + sufixo + r"\b", re.IGNORECASE)


def alternativa_presente(alternativa, traducao_norm):
    """Verdadeiro se todas as palavras de conteúdo da alternativa aparecem (pelo radical)."""
    for variante in alternativa.split("/"):
        variante = re.sub(r"\([^)]*\)", " ", variante)
        palavras = [p for p in re.findall(r"[\w-]+", normalizar_pt(variante))
                    if p not in PALAVRAS_VAZIAS]
        if palavras and all(re.search(r"\b" + re.escape(radical(p)), traducao_norm)
                            for p in palavras):
            return True
    return False


def analisar(pares, glossario):
    # Termos mais longos primeiro: "action links" consome o trecho antes de "action".
    ordem = sorted(glossario.values(), key=lambda t: len(t["en"]), reverse=True)
    regexes = [(t, regex_termo_en(t["en"], t["classes"])) for t in ordem]
    desvios, especiais, ocorrencias = {}, {}, 0

    for original, traducao in pares:
        texto = limpar(original)
        traducao_norm = normalizar_pt(limpar(traducao))
        for termo, rx in regexes:
            if not rx.search(texto):
                continue
            texto = rx.sub(" ", texto)
            ocorrencias += 1
            if not termo["alternativas"]:
                especiais.setdefault(termo["en"], (termo, []))[1].append((original, traducao))
            elif not any(alternativa_presente(a, traducao_norm) for a in termo["alternativas"]):
                desvios.setdefault(termo["en"], (termo, []))[1].append((original, traducao))
    return desvios, especiais, ocorrencias


# ---------------------------------------------------------------- relatório

def resumir(s, limite=160):
    s = " ".join(s.split())
    return s if len(s) <= limite else s[:limite - 1] + "…"


def imprimir(desvios, especiais, ocorrencias, n_pares, n_termos):
    print(f"Strings traduzidas analisadas: {n_pares}")
    print(f"Termos do glossário carregados: {n_termos}")
    print(f"Ocorrências de termos do glossário no texto original: {ocorrencias}")
    print(f"Possíveis desvios: {sum(len(v[1]) for v in desvios.values())} "
          f"em {len(desvios)} termos\n")

    for en, (termo, casos) in sorted(desvios.items(), key=lambda kv: -len(kv[1][1])):
        print(f'## "{en}" → esperado: {" | ".join(termo["alternativas"])}')
        for nota in termo["descricoes"]:
            print(f"   nota do glossário: {nota}")
        for original, traducao in casos:
            print(f'- Original: "{resumir(original)}"')
            print(f'  Tradução: "{resumir(traducao)}"')
        print()

    if especiais:
        print("# Termos sem tradução fixa no glossário (seguir a nota)\n")
        for en, (termo, casos) in especiais.items():
            print(f'## "{en}" ({len(casos)} ocorrência(s)) — {" / ".join(termo["descricoes"])}')
            for original, traducao in casos:
                print(f'- Original: "{resumir(original)}"')
                print(f'  Tradução: "{resumir(traducao)}"')
            print()


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("po", help="arquivo .po exportado do translate.wordpress.org")
    p.add_argument("--glossario", default=GLOSSARIO_GERAL, help="CSV do glossário geral (arquivo ou URL)")
    p.add_argument("--projeto", help="ex.: wp-plugins/woocommerce/stable ou wp-themes/astra")
    args = p.parse_args()

    try:
        glossario = ler_glossario(carregar_texto(args.glossario))
    except (OSError, urllib.error.URLError) as erro:
        sys.exit(f"Não foi possível carregar o glossário geral: {erro}")

    if args.projeto:
        projeto = args.projeto.strip("/")
        if projeto.startswith("wp-plugins/") and projeto.count("/") == 1:
            projeto += "/stable"
        try:
            termos_projeto = ler_glossario(carregar_texto(GLOSSARIO_PROJETO.format(projeto=projeto)))
            glossario.update(termos_projeto)  # glossário do projeto prevalece
            print(f"Glossário do projeto: {len(termos_projeto)} termos (têm prioridade)")
        except urllib.error.HTTPError as erro:
            if erro.code != 404:
                sys.exit(f"Erro ao baixar o glossário do projeto: {erro}")
            print("Glossário do projeto: não existe para este projeto")

    pares = ler_po(carregar_texto(args.po))
    desvios, especiais, ocorrencias = analisar(pares, glossario)
    imprimir(desvios, especiais, ocorrencias, len(pares), len(glossario))


if __name__ == "__main__":
    main()
