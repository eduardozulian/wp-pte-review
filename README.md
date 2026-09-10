# Skill para revisão de solicitações de PTE no WordPress (pt-BR)

Skill de referência para revisão de solicitações de PTE (Project Translation Editor) das traduções pt-BR do WordPress.org.

Documento operacional pra GTEs (Editores de Tradução Geral) da locale pt-BR que precisam avaliar se um candidato deve virar PTE de um plugin ou tema.

## Uso

O conteúdo operacional está em [`SKILL.md`](./SKILL.md), que cobre:

1. O que se espera na revisão, incluindo o checklist oficial do guia de GTE
2. Princípio de linguagem humana em qualquer output, sem jargão do formato `.po`
3. Fluxo de trabalho, incluindo as checagens automatizadas via grep
4. Formato de saída (resumo executivo + mensagem pronta ao candidato)
5. Limites e bom senso, incluindo nunca afirmar a origem de uma tradução

O detalhamento fica em [`references/`](./references/), lido sob demanda:

- [`po-export.md`](./references/po-export.md) — como localizar e exportar o `.po` do projeto em translate.wordpress.org
- [`review-checklist.md`](./references/review-checklist.md) — critérios de defeito técnico (bloqueantes), fluência, consistência terminológica, comportamento do código e convenções formais
- [`non-english-source-strings.md`](./references/non-english-source-strings.md) — o que fazer quando o texto original não está em inglês
- [`message-templates.md`](./references/message-templates.md) — tom da mensagem ao candidato e estilo por canal (Slack, fórum interno, fórum internacional)

## Estrutura

```text
wp-pte-review/
├── SKILL.md
├── README.md
├── LICENSE
└── references/
    ├── message-templates.md
    ├── non-english-source-strings.md
    ├── po-export.md
    └── review-checklist.md
```

## Instalação no Claude Code

Clonar direto no diretório de skills:

```bash
git clone https://github.com/eduardozulian/wp-pte-review.git ~/.claude/skills/wp-pte-review
```

Esse é o único passo. O `git clone` cria os diretórios que faltarem, então funciona mesmo em uma instalação do Claude Code que nunca teve nenhuma skill. Pra atualizar depois, rodar `git pull` dentro de `~/.claude/skills/wp-pte-review`.

O clone precisa ser do repositório inteiro, não só do `SKILL.md`, porque o `SKILL.md` referencia os arquivos em `references/`.

Depois disso, o Claude Code aciona a skill quando o pedido do usuário se encaixar no `description` (revisão de PTE pt-BR), ou por invocação direta com `/wp-pte-review`. Pode ser necessário reiniciar o Claude Code pra skill aparecer.

## Como referência humana

O `SKILL.md` e os arquivos em `references/` também funcionam como documento de leitura direta, sem necessidade de ferramenta. Toda a lógica de decisão está em prosa.

## Base

Handbook oficial da Equipe Brasileira de Tradução do WordPress: https://br.wordpress.org/team/handbook/traducao/

Guia de GTE: https://br.wordpress.org/team/handbook/traducao/equipe/gte/

Glossário pt-BR: https://translate.wordpress.org/locale/pt-br/default/glossary/

## Licença

GPL-2.0, seguindo o padrão do ecossistema WordPress.
