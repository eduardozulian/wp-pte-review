#!/usr/bin/env python3
"""Compara placeholders e tags HTML entre o texto original e a tradução de um .po.

Os exports do translate.wordpress.org não marcam as strings como php-format,
então `msgfmt --check-format` não verifica nada neles. Este script faz a
comparação diretamente.

Uso:
    python3 placeholder-check.py ARQUIVO.po
"""

import importlib.util
import pathlib
import re
import sys
from collections import Counter

sys.dont_write_bytecode = True  # não deixar __pycache__ dentro da skill

_spec = importlib.util.spec_from_file_location(
    "glossary_check", pathlib.Path(__file__).with_name("glossary-check.py"))
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
ler_po, carregar_texto, resumir = _mod.ler_po, _mod.carregar_texto, _mod.resumir

PLACEHOLDER = re.compile(r"%(?:(\d+)\$)?[-+0'#]*\d*(?:\.\d+)?([bcdeEfFgGosuxX@])|===\w+===|###\w+###")
TAG = re.compile(r"</?([a-zA-Z][\w-]*)[^>]*>")
ATRIBUTO = re.compile(r"\b(href|target|rel|class|id|src)\s*=\s*(\"[^\"]*\"|'[^']*')")


def placeholders(texto):
    """Lista de (posição, tipo). Placeholders sem número recebem a posição pela ordem."""
    texto = texto.replace("%%", "")
    itens, sequencia = [], 0
    for m in PLACEHOLDER.finditer(texto):
        if m.group(0)[:3] in ("===", "###"):
            itens.append((m.group(0), "var"))
            continue
        if m.group(1):
            itens.append((int(m.group(1)), m.group(2)))
        else:
            sequencia += 1
            itens.append((sequencia, m.group(2)))
    return itens


def problemas(original, traducao):
    achados = []
    ph_o, ph_t = placeholders(original), placeholders(traducao)
    if sorted(ph_o, key=str) != sorted(ph_t, key=str):
        achados.append(f"placeholders diferentes: original {_fmt(ph_o)}, tradução {_fmt(ph_t)}")
    elif (len([p for p in ph_o if p[1] != "var"]) >= 2
          and not re.search(r"%\d+\$", original)):
        achados.append("dois ou mais placeholders sem número: conferir se a ordem das "
                       "informações na frase continua correta (não podem trocar de lugar)")
    tags_o, tags_t = Counter(TAG.findall(original)), Counter(TAG.findall(traducao))
    if tags_o != tags_t:
        achados.append(f"tags HTML diferentes: original {dict(tags_o)}, tradução {dict(tags_t)}")
    attr_o, attr_t = Counter(ATRIBUTO.findall(original)), Counter(ATRIBUTO.findall(traducao))
    if attr_o != attr_t:
        achados.append("atributos de tag alterados (href, target, rel, class, id ou src)")
    return achados


def _fmt(itens):
    return ", ".join(f"{p}:{t}" if t != "var" else p for p, t in itens) or "nenhum"


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    pares = ler_po(carregar_texto(sys.argv[1]))
    total = 0
    for original, traducao in pares:
        achados = problemas(original, traducao)
        if not achados:
            continue
        total += 1
        print(f'- Original: "{resumir(original)}"')
        print(f'  Tradução: "{resumir(traducao)}"')
        for a in achados:
            print(f"  → {a}")
        print()
    print(f"Strings traduzidas analisadas: {len(pares)}; com alerta: {total}")


if __name__ == "__main__":
    main()
