---
name: wp-pte-review
description: Revisar solicitações de PTE (Project Translation Editor) para traduções pt-BR do WordPress.org. Use para avaliar se um candidato deve virar PTE de um plugin ou tema, dado o link do post de solicitação ou o nome do projeto. Also use for "review this PTE request", Polyglots PTE requests, or reviewing a contributor's pt-BR suggestions on translate.wordpress.org.
---

# Instruções de revisão — Solicitações de PTE (pt-BR)

> Documento de referência para revisar um pedido de alguém para se tornar Editor de
> Tradução de Projeto (PTE) de um plugin ou tema. Escrito para o GTE que conduz a revisão.
> Base: handbook da Equipe Brasileira de Tradução do WordPress
> (https://br.wordpress.org/team/handbook/traducao/).

## Papel de quem usa esta skill

Quando um agente (Claude Code, Codex ou outro) segue estas instruções, ele **prepara** a
revisão para o GTE: baixa e analisa as strings, escreve o resumo e o rascunho da mensagem.
**A decisão e as ações públicas são sempre do GTE humano.** O agente não deve, por conta
própria:

- aprovar ou recusar o pedido de PTE;
- aprovar, rejeitar ou editar strings no translate.wordpress.org;
- publicar ou responder no site da equipe, no fórum de Polyglots ou no Slack.

Essas ações afetam um voluntário real e ficam públicas. O agente entrega o material e o
GTE decide o que fazer com ele. As referências a "você" neste documento se dirigem ao GTE.

## O que se espera nessa revisão

Como GTE (Editor de Tradução Geral), você tem acesso para aprovar ou rejeitar traduções
em qualquer projeto da localidade pt-BR, e é responsável por designar PTEs (Editores de
Tradução de Projeto). Guia oficial:
https://br.wordpress.org/team/handbook/traducao/equipe/gte/

**Importante: o candidato não envia um arquivo `.po`.** Ele publica um post pedindo PTE
— seja no site da equipe brasileira (https://br.wordpress.org/team/) ou no fórum
internacional de Polyglots (https://make.wordpress.org/polyglots/) — geralmente contendo
o nome/link do projeto e, às vezes, o link direto para o próprio perfil de tradutor ou
para as strings enviadas. **Cabe a você localizar o projeto em translate.wordpress.org e
exportar o `.po` a partir de lá** — ver `references/po-export.md`.

O checklist oficial que baseia toda essa revisão (do guia de GTE) é:
- O candidato parece falar português brasileiro fluentemente?
- O candidato já é PTE de algum outro projeto?
- O candidato enviou sugestões de tradução suficientes?
- As traduções seguem as boas práticas de tradução?

O passo 1 do fluxo de trabalho mostra como responder cada uma. As duas últimas são o
foco técnico deste documento.

## Referências

- `references/po-export.md` — ler antes de baixar o arquivo, quando você ainda não tem o
  `.po` em mãos. Passo a passo no translate.wordpress.org e a armadilha do filtro de
  export.
- `references/review-checklist.md` — ler ao avaliar as strings traduzidas. Critérios
  completos de defeito técnico, fluência, consistência terminológica, comportamento do
  código e convenções formais.
- `references/non-english-source-strings.md` — ler quando o texto original do projeto
  não estiver em inglês. Define quando o PTE é desnecessário e quando o pedido fica
  pendente de correção de i18n.
- `references/message-templates.md` — ler ao redigir a mensagem final ao candidato. Tom
  por canal, prática da equipe BR no fórum internacional, e o caso do pedido partir do
  próprio autor do plugin.

Glossário oficial pt-BR (fonte autoritativa, muda com o tempo):
https://translate.wordpress.org/locale/pt-br/default/glossary/
Export em CSV para busca em lote:
https://translate.wordpress.org/locale/pt-br/default/glossary/-export/

## 0. Princípio geral de linguagem

**Usar linguagem humana em qualquer output, não jargão técnico do formato `.po`.**
Isso vale para mensagem ao candidato, resumo executivo, revisão detalhada ou qualquer
comunicação entre GTEs — não só a mensagem final. Em vez de `msgid`/`msgstr`, usar
equivalentes em linguagem natural: "string original" ou "texto original do código" em
vez de `msgid`; "tradução" ou "texto traduzido" em vez de `msgstr`. Objetivo: qualquer
pessoa (revisor, candidato, ou outro GTE lendo depois) deve conseguir entender sem
precisar saber o formato técnico do arquivo.

## 1. Fluxo de trabalho

1. **Ler o post do pedido** e anotar: o projeto (slug), o nome de usuário do candidato
   no WordPress.org, se quem pede é o próprio autor do plugin/tema, e o canal (site da
   equipe brasileira ou fórum internacional). Com isso, responder as perguntas de
   contexto do checklist oficial:
   - **Já é PTE de outro projeto?** O perfil em `profiles.wordpress.org/<usuario>/` mostra
     o selo "Translation Editor" para quem já é editor de tradução, mas não diz de quais
     projetos nem de qual idioma. Usar o selo como indício e, se não der para confirmar,
     deixar a pergunta em aberto no resumo para o GTE.
   - **Parece falar português brasileiro fluentemente?** Responder a partir das próprias
     traduções (passo 6) e do texto do post, se estiver em português.
2. **Exportar o `.po`** com as sugestões do candidato (`references/po-export.md`). A
   contagem do passo 4 responde se ele **enviou sugestões suficientes**. O handbook não
   define um número mínimo: informar a quantidade no resumo e, se for pequena demais para
   avaliar com confiança, dizer isso (ver seção 3).
3. Ler o `.po` e listar os pares texto original / tradução. Para arquivos grandes (UI
   real, não só readme), ler em blocos — não confiar só na visualização truncada do meio
   do arquivo.
4. **Rodar checagens automatizadas antes/junto da leitura manual de fluência** (especialmente
   em arquivos grandes ou de UI real, onde bugs técnicos têm mais impacto que em um readme):
   - **Contagem de traduzidas, vazias e fuzzy:** usar as ferramentas do gettext, que
     entendem o formato, em vez de `grep`. Um `grep '^msgstr ""$'` conta errado: pega o
     cabeçalho do arquivo e as strings longas (que abrem com `msgstr ""` seguido de linhas
     de continuação), e não pega plurais vazios (`msgstr[0] ""`). Um `grep fuzzy` também
     pega qualquer string que contenha a palavra "fuzzy".
     ```bash
     msgfmt --statistics -o /dev/null candidato.po   # ex.: "120 translated, 2 fuzzy, 3 untranslated"
     msgattrib --untranslated candidato.po           # lista as não traduzidas
     msgattrib --only-fuzzy candidato.po             # lista as fuzzy
     ```
     (`msgfmt` e `msgattrib` vêm no pacote `gettext`: `brew install gettext` no macOS,
     `apt install gettext` no Debian/Ubuntu.)
   - **Duas frases coladas na mesma tradução sem separador** (sinal de erro de
     merge/cópia de sugestões, não de tradução ruim): ponto final seguido de letra
     maiúscula sem espaço. Buscar só nas traduções e com uma classe que inclua
     maiúsculas acentuadas; `[A-Z]` não pega "É" nem "Á":
     ```bash
     LC_ALL=en_US.UTF-8 grep -n '^msgstr.*\.[[:upper:]]' candidato.po
     ```
     Descontar falsos positivos como nomes de domínio e números de versão.
   - **Corrupção de encoding** (mojibake: UTF-8 lido como Latin-1 ou Windows-1252 e
     reconvertido, como "Ã§" no lugar de "ç" ou "â€”" no lugar de "—"):
     ```bash
     grep -nE 'Ã.|â€' candidato.po
     ```
     Também comparar os caracteres especiais do original com os da tradução.
   - **Termos com erro recorrente** (ver `references/review-checklist.md`):
     ```bash
     grep -niE '^msgstr.*(por favor|habilit)' candidato.po
     grep -nE '^msgstr.*(Wordpress|Woocommerce)' candidato.po   # grafia da marca
     ```
   - **Padrão de Title Case carregado do inglês** (maiúscula em cada palavra da
     tradução, quando o português pede só a primeira). Não há comando confiável para
     isso: ler as traduções curtas (botões, rótulos, títulos) procurando o padrão.
     Descontar nomes próprios e nomes de método de pagamento/produto que funcionam quase
     como marca (zona cinzenta, ver `references/review-checklist.md`).
5. Marcar separadamente:
   - Strings vazias (não traduzidas)
   - Strings `fuzzy`
   - Strings com placeholders (`%s`, `%d`, `%1$s`, `===VAR===`, `###VAR###`, `%@`, etc.)
     ou tags HTML, para checar se foram preservados corretamente:
     ```bash
     python3 ~/.claude/skills/wp-pte-review/scripts/placeholder-check.py candidato.po
     ```
     (regras em `references/review-checklist.md`, "Placeholders intactos")
6. Avaliar cada string traduzida com `references/review-checklist.md`. **Defeitos técnicos
   são sempre bloqueantes**: texto duplicado/colado, corrupção de encoding e placeholders
   ou tags quebrados impedem a recomendação de PTE independente da qualidade do resto do
   arquivo.
7. **Cruzar todas as traduções com o glossário**, o geral pt-BR e o do projeto, se
   existir. O script baixa os dois e lista os candidatos a desvio:
   ```bash
   python3 ~/.claude/skills/wp-pte-review/scripts/glossary-check.py candidato.po --projeto wp-plugins/<slug>
   ```
   (Temas: `--projeto wp-themes/<slug>`. Se a skill estiver instalada em outro lugar,
   ajustar o caminho.) Como o script baixa a versão atual do glossário a cada execução,
   ele acompanha as mudanças no glossário. Os termos do glossário do projeto têm
   prioridade sobre os do geral (exemplo: no WooCommerce, "tax" é "imposto", não "taxa").

   Como ler o resultado (critérios em `references/review-checklist.md`):
   - Cada item é um **candidato**, não um erro confirmado. O script considera flexões
     ("ativar" aceita "ativado", "ativação"), mas não entende o contexto. Ler cada caso e
     decidir: desvio real, exceção justificada pelo contexto ou falso positivo (por
     exemplo, o termo em inglês usado em outro sentido).
   - Ler as **notas do glossário** que o script mostra: algumas regras estão só nelas
     ("please": não traduzir; "sorry" e "thank you": traduzir só se for o objetivo da
     string; meses sempre em minúsculas).
   - `enable`/`disable` e `please` têm histórico de erro recorrente. Conferir esses
     termos mesmo que o script não acuse nada.
   - Sem Python disponível: baixar o CSV (link acima; glossário do projeto em
     `https://translate.wordpress.org/projects/wp-plugins/<slug>/stable/pt-br/default/glossary/-export/`,
     que retorna 404 se o projeto não tiver glossário) e cruzar os termos manualmente.
8. Compilar o resultado no formato da seção 2, incluindo uma lista **"Desvios do
   glossário"** com os desvios confirmados e, separadas, as exceções que você considerou
   justificadas, com o motivo.

## 2. Formato de saída

**Padrão quando não especificado:** resumo executivo + mensagem pronta.

O resumo executivo segue sempre esta estrutura, para que revisões diferentes possam ser
comparadas:

1. **Recomendação**, em uma linha, com uma destas três opções:
   - **Recomendar o PTE**: sem defeitos bloqueantes e com qualidade suficiente.
   - **Pedir ajustes antes**: há defeitos bloqueantes ou problemas recorrentes que o
     candidato precisa corrigir (rejeitando as próprias sugestões e reenviando).
   - **Pendente**: falta algo que não depende da qualidade da tradução (texto original
     fora do inglês, volume pequeno demais para avaliar, pergunta de contexto sem resposta).
2. **Checklist oficial**: as quatro perguntas do guia de GTE, cada uma com resposta curta
   (sim, não, ou "não foi possível confirmar") e a evidência.
3. **Números**: strings traduzidas, vazias e fuzzy (passo 4).
4. **Defeitos bloqueantes**, se houver, primeiro e com os exemplos.
5. **Desvios do glossário** e **outros problemas**, agrupados por tipo e indicando se são
   recorrentes ou pontuais.
6. **Pontos positivos**, para a mensagem ao candidato não ser só de correções.

**Revisão detalhada string por string:** só quando pedida explicitamente.

**Quando o post for no fórum internacional (em inglês):** o formato que funcionou bem em
revisões anteriores foi gerar primeiro o resumo detalhado em português (pra você decidir
o que entra na versão pública) e só depois a mensagem em inglês — mais enxuta, preferindo
**linkar a string específica filtrada no GlotPress** em vez de citar o texto problemático
por extenso entre aspas. Ao montar esses links, confirmar o filtro de status correto
(`current_or_waiting_or_fuzzy_or_untranslated` é mais seguro que `waiting` isolado, que
pode não retornar nada se a string já tiver outro status).

Para o tom e a estrutura da mensagem, ver `references/message-templates.md`.

## 3. Limites e bom senso

- O glossário não é absoluto: se o contexto exigir uma tradução diferente, isso é
  aceitável — mas deve ser sinalizado como exceção justificada, não como erro.
- Erros pontuais (um typo isolado) pesam menos que padrões recorrentes do mesmo
  problema espalhados pelo projeto.
- Se o volume de strings enviadas for muito baixo para avaliar com confiança, sinalizar
  isso em vez de aprovar/reprovar precipitadamente.
- Quando o volume de strings for grande e a qualidade tão baixa que separar as boas das
  ruins levaria tempo demais, o handbook considera razoável o GTE **rejeitar em massa**
  ("Colabore", em boas práticas). O agente pode sugerir isso no resumo, com os exemplos
  que justificam; a decisão e a ação são do GTE.
- **Nunca afirmar nem negar a origem de uma tradução** (tradução automática vs. humana).
  Não há como confirmar isso só pelo texto final — avaliar a tradução pelo que ela é
  (fluente ou não, consistente ou não, correta ou não), não pela suposição de como foi
  produzida. Sintomas como erro gramatical ou estrutura estranha podem ser citados como
  sintomas; "isso parece/não parece MT" não deve aparecer como conclusão, nem em
  conversa interna nem na mensagem ao candidato.
- **Sinais de contexto são hipótese, não prova.** Coisas como o pedido de PTE ser para
  uma única locale (vs. para 8-10 de uma vez), o nome de quem solicita, ou o tipo de
  plugin (ex.: um gateway de pagamento brasileiro como PagSeguro/PagBank sugerindo
  desenvolvedor nativo) ajudam a calibrar expectativa antes de abrir o arquivo, mas a
  avaliação final deve sempre se basear no conteúdo do `.po` em si, não nesses sinais.
