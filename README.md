# pte-review-ptbr

Skill de referência para revisão de solicitações de PTE (Project Translation Editor) das traduções pt-BR do WordPress.org.

Documento operacional pra GTEs (Editores de Tradução Geral) da locale pt-BR que precisam avaliar se um candidato deve virar PTE de um plugin ou tema.

## Uso

O conteúdo operacional está em [`SKILL.md`](./SKILL.md). Ele cobre:

1. O que é um GTE e o que se espera na revisão
2. Como localizar e exportar o `.po` do projeto em translate.wordpress.org
3. O que fazer quando o texto original está em português (não en_US)
4. Checklist de defeitos técnicos (bloqueantes), fluência, consistência terminológica e boas práticas formais
5. Formato de saída (resumo executivo + mensagem pronta ao candidato)
6. Estilo por canal (Slack, fórum interno, fórum internacional)

### Como skill do Claude Code

O `SKILL.md` inclui o frontmatter YAML padrão de skill (`name`, `description`). Pra usar localmente:

```bash
mkdir -p ~/.claude/skills/pte-review-ptbr
cp SKILL.md ~/.claude/skills/pte-review-ptbr/
```

Depois disso, o Claude Code aciona a skill quando o pedido do usuário se encaixar no `description` (revisão de PTE pt-BR).

### Como referência humana

O `SKILL.md` também funciona como documento de leitura direta, sem necessidade de ferramenta. Toda a lógica de decisão está em prosa.

## Base

Handbook oficial da Equipe Brasileira de Tradução do WordPress: https://br.wordpress.org/team/handbook/traducao/

Guia de GTE: https://br.wordpress.org/team/handbook/traducao/equipe/gte/

## Licença

GPL-2.0, seguindo o padrão do ecossistema WordPress.
