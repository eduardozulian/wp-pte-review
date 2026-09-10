---
name: pte-review-ptbr
description: Revisar solicitações de PTE (Project Translation Editor) para traduções pt-BR do WordPress.org. Use para avaliar se um candidato deve virar PTE de um plugin ou tema, dado o link do post de solicitação ou o nome do projeto.
---

# Instruções de revisão — Solicitações de PTE (pt-BR)

> Documento de referência para revisar um pedido de alguém para se tornar Editor de
> Tradução de Projeto (PTE) de um plugin ou tema. Escrito para o GTE que conduz a revisão.
> Base: handbook da Equipe Brasileira de Tradução do WordPress
> (https://br.wordpress.org/team/handbook/traducao/).

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

As duas primeiras perguntas exigem contexto que normalmente não está no `.po` em si —
olhar o post do pedido e, se necessário, o perfil do candidato em
profiles.wordpress.org. As últimas duas são o foco técnico deste documento.

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

## 1. Quando este processo é acionado

Quando você for avaliar se alguém pode ser PTE de um projeto — normalmente partindo do
link do post de solicitação (site da equipe brasileira ou fórum internacional) ou apenas
do nome do projeto/candidato. Não é necessário ter o `.po` em mãos; localizar e exportar
o arquivo faz parte do processo (`references/po-export.md`).

## 2. Fluxo de trabalho

1. Ler o `.po` e listar os pares texto original / tradução. Para arquivos grandes (UI
   real, não só readme), ler em blocos — não confiar só na visualização truncada do meio
   do arquivo.
2. **Rodar checagens automatizadas antes/junto da leitura manual de fluência** (especialmente
   em arquivos grandes ou de UI real, onde bugs técnicos têm mais impacto que em um readme):
   - Contagem real de vazias/fuzzy via grep (`grep -c '^msgstr ""$'`, `grep -c fuzzy`) — não
     confiar só em leitura visual. Atenção: strings multi-linha no formato `.po` abrem com
     `msgstr ""` seguido de linhas de continuação entre aspas; isso **não** é uma string vazia,
     é só o formato de string longa. Confirmar visualmente antes de contar como vazia.
   - Duas frases coladas na mesma tradução sem separador (sinal de erro de merge/cópia de
     sugestões, não de tradução ruim) — buscar padrão de ponto final seguido de letra
     maiúscula sem espaço dentro da mesma string (`\.[A-Z]`).
   - Corrupção de encoding (mojibake clássico de UTF-8 lido como Latin-1 e reconvertido,
     geralmente aparecendo como "â" seguido de caracteres de controle invisíveis onde devia
     haver um travessão "—" ou outro caractere acentuado). Comparar ocorrências de
     caracteres especiais no original com as da tradução.
   - Padrão de Title Case carregado do inglês (maiúscula em cada palavra da tradução,
     quando o português pede só a primeira). Descontar nomes próprios e nomes de
     método de pagamento/produto que funcionam quase como marca (zona cinzenta — ver
     `references/review-checklist.md`).
3. Marcar separadamente:
   - Strings vazias (não traduzidas)
   - Strings `fuzzy`
   - Strings com placeholders (`%s`, `%d`, `%1$s`, `===VAR===`, `%@`, etc.) para checar
     se foram preservados corretamente
4. Avaliar cada string traduzida com `references/review-checklist.md`. **Defeitos técnicos
   são sempre bloqueantes**: texto duplicado/colado, corrupção de encoding e placeholders
   ou tags quebrados impedem a recomendação de PTE independente da qualidade do resto do
   arquivo.
5. Cruzar termos relevantes com o glossário oficial pt-BR (link acima). Se eu não tiver
   certeza do termo padrão atual, devo consultar o glossário (busca/fetch) antes de
   apontar inconsistência — o glossário muda com o tempo. Dois termos têm histórico de
   erro recorrente em revisões anteriores e merecem checagem obrigatória mesmo sem
   suspeita prévia: `enable`/`disable` e `please` (detalhe em
   `references/review-checklist.md`).
6. Verificar se há glossário **específico do projeto** (alguns plugins/temas grandes,
   como o WooCommerce, têm o próprio).
7. Compilar o resultado no formato da seção 3.

## 3. Formato de saída

**Padrão quando não especificado:** resumo executivo + mensagem pronta.

**Revisão detalhada string por string:** só quando pedida explicitamente.

**Quando o post for no fórum internacional (em inglês):** o formato que funcionou bem em
revisões anteriores foi gerar primeiro o resumo detalhado em português (pra você decidir
o que entra na versão pública) e só depois a mensagem em inglês — mais enxuta, preferindo
**linkar a string específica filtrada no GlotPress** em vez de citar o texto problemático
por extenso entre aspas. Ao montar esses links, confirmar o filtro de status correto
(`current_or_waiting_or_fuzzy_or_untranslated` é mais seguro que `waiting` isolado, que
pode não retornar nada se a string já tiver outro status).

Para o tom e a estrutura da mensagem, ver `references/message-templates.md`.

## 4. Limites e bom senso

- O glossário não é absoluto: se o contexto exigir uma tradução diferente, isso é
  aceitável — mas deve ser sinalizado como exceção justificada, não como erro.
- Erros pontuais (um typo isolado) pesam menos que padrões recorrentes do mesmo
  problema espalhados pelo projeto.
- Se o volume de strings enviadas for muito baixo para avaliar com confiança, sinalizar
  isso em vez de aprovar/reprovar precipitadamente.
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
