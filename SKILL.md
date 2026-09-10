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
exportar o `.po` a partir de lá** — ver seção 2.1.

O checklist oficial que baseia toda essa revisão (do guia de GTE) é:
- O candidato parece falar português brasileiro fluentemente?
- O candidato já é PTE de algum outro projeto?
- O candidato enviou sugestões de tradução suficientes?
- As traduções seguem as boas práticas de tradução?

As duas primeiras perguntas exigem contexto que normalmente não está no `.po` em si —
olhar o post do pedido e, se necessário, o perfil do candidato em
profiles.wordpress.org. As últimas duas são o foco técnico deste documento (seções 3 e 4).

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
o arquivo faz parte do processo (seção 2.1).

## 2. Formato esperado do arquivo e como obtê-lo

- **Sempre `.po`**, nunca `.mo` (binário, ilegível).
- Se vier `.mo` por engano, pedir o `.po` correspondente antes de revisar.

### 2.1 Como baixar o `.po`

Geralmente o suficiente é o nome do plugin/tema. Passo a passo:

1. A partir do nome, acessar `https://translate.wordpress.org/projects/wp-plugins/[nome-do-projeto]/`
   (ou `wp-themes/` para temas).
2. Entrar na área de tradução pt-BR do projeto:
   `https://translate.wordpress.org/locale/pt-br/default/wp-plugins/[nome-do-projeto]/`.
3. Entrar no subprojeto relevante (geralmente Stable; Development só se o pedido for
   especificamente sobre uma versão em desenvolvimento).
4. Filtrar geralmente por **"Waiting"** (strings aguardando aprovação — o cenário mais
   comum em pedidos de PTE). Esse é o padrão mais frequente, não uma regra fixa: sempre
   confirmar se é o filtro correto para o caso antes de exportar, já que outros filtros
   podem ser necessários dependendo do que está sendo avaliado.
5. No fim da página, no dropdown ao lado de **Export**, selecionar **"Only matching the
   filter"** (o padrão exporta o projeto inteiro e ignora o filtro escolhido no passo 4).
   Depois clicar em **Export** e escolher o formato **PO**.

- **Se o export sair vazio ou muito maior que o esperado**, checar primeiro se o dropdown
  ficou em "Only matching the filter" antes de tratar como problema do candidato.

### 2.2 Texto original (`msgid`) em idioma não-inglês

Em alguns projetos o autor do plugin/tema escreveu o texto original em português (ou
outro idioma que não inglês) em vez de en_US. Isso é uma decisão/problema de i18n do
autor, não do tradutor — mas vale duas situações distintas, que mudam a resposta ao
candidato:

- **Se o autor não pretende disponibilizar o plugin em outros idiomas**: PTE não é
  necessário nesse cenário. O plugin vai funcionar sempre só no idioma-fonte escolhido
  (pt-BR ou outro), porque o WordPress trata as strings originais como en_US
  internamente — um site com o WordPress configurado em inglês nunca aciona as funções
  de tradução, então não há função prática pro PTE existir enquanto o `msgid` não for
  en_US.
- **Se o autor quer o plugin disponível em múltiplos idiomas**: é necessário primeiro
  corrigir o texto original no código para en_US. O pedido de PTE fica pendente disso —
  aprovar PTE num projeto cujo texto-fonte ainda não é traduzível não resolve nada na
  prática.

Em ambos os casos, ao comunicar ao candidato, enquadrar como **opções pra ele escolher**,
não como bloqueio arbitrário. Referência de precedente real da comunidade (thread do
Slack #polyglots, onde um pedido foi negado pelo mesmo motivo, com explicação técnica
detalhada): https://wordpress.slack.com/archives/C02RP50LK/p1783626440167259

Isso não invalida a revisão do restante do arquivo: mesmo com `msgid` em português,
ainda avaliamos se a tradução manteve ou degradou a gramática, o tempo verbal e o
sentido do original. Mudanças de "Adiciona" para "Adicionado", por exemplo, são erro do
tradutor mesmo que a string já estivesse em PT.

## 3. Fluxo de trabalho

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
     seção 4.2).
3. Marcar separadamente:
   - Strings vazias (não traduzidas)
   - Strings `fuzzy`
   - Strings com placeholders (`%s`, `%d`, `%1$s`, `===VAR===`, `%@`, etc.) para checar
     se foram preservados corretamente
4. Avaliar cada string traduzida com o checklist da seção 4.
5. Cruzar termos relevantes com o glossário oficial pt-BR
   (https://translate.wordpress.org/locale/pt-br/default/glossary/). Se eu não tiver
   certeza do termo padrão atual, devo consultar o glossário (busca/fetch) antes de
   apontar inconsistência — o glossário muda com o tempo. Dois termos têm histórico de
   erro recorrente em revisões anteriores e merecem checagem obrigatória mesmo sem
   suspeita prévia: ver seção 4.3.
6. Verificar se há glossário **específico do projeto** (alguns plugins/temas grandes,
   como o WooCommerce, têm o próprio).
7. Compilar o resultado no formato pedido (seção 5).

## 4. Checklist de boas práticas

Baseado em: https://br.wordpress.org/team/handbook/traducao/boas-praticas/
(versão em inglês, espelhada quase 1:1: https://make.wordpress.org/polyglots/handbook/translating/expectations/)

O checklist está dividido em camadas com prioridade diferente. **Defeitos técnicos são
sempre bloqueantes**, independente da qualidade do resto do arquivo — não tratar como
"ponto de estilo" na comunicação com o candidato.

### 4.1 Defeitos técnicos (bloqueantes)

- **Strings com texto duplicado/colado** — duas versões da mesma frase (ou frases
  diferentes) coladas sem espaço ou separador. Geralmente erro de merge/cópia de
  sugestões, não tradução ruim. Mostraria texto quebrado pro usuário final.
- **Corrupção de encoding** — caracteres especiais (acentos, travessão) virando sequências
  de bytes sem sentido.
- **Placeholders ou tags quebrados** — `%s`/`%d`/`%1$s` removidos, trocados de tipo (não
  só de posição), ou tags HTML mal formadas que quebrariam o layout/funcionamento da página.

Esses três pontos, se presentes, devem aparecer primeiro e com destaque no resumo e na
mensagem ao candidato — não importa quão boa seja a fluência do resto do arquivo, **não
recomendar aprovação de PTE enquanto eles existirem**.

### 4.2 Fluência do português

O teste central aqui é: **lendo só a tradução, sem olhar o original, isso é como um
brasileiro escreveria ou falaria?** Isso é diferente de consistência (seção 4.3) — uma
tradução pode ser perfeitamente consistente e ainda soar estranha, e vice-versa.

- **Tradução orgânica, não literal** — a ideia foi transmitida de forma natural em
  português, sem replicar a estrutura da frase em inglês? Cuidado especial com frases que
  empilham reforços redundantes (ex.: "às centenas de uma vez", "em massa de uma vez" —
  cada termo já carrega a ideia de quantidade/simultaneidade, não precisa reforçar com
  os dois ao mesmo tempo).
- **Formalidade equivalente** — o tom informal/educado do original foi mantido sem
  formalizar demais (ex.: "Use" em vez de "Utilize") nem inserir elementos novos
  (emojis, gírias) que não estavam no original?
- **Sem gírias ou jargão de nicho** — termos como *pingback*, *trackback*, *feed* podem
  ficar em inglês (são exceções conhecidas); o resto deve ser compreensível para
  qualquer usuário.
- **Maiúsculas/minúsculas (Title Case do inglês)** — em português só a primeira palavra
  da frase e nomes próprios levam maiúscula; meses, idiomas e gentílicos em minúscula
  (exceto início de frase). Esse é um erro recorrente: strings como "Total Reembolsado:"
  ou "Principais Características" carregam a capitalização de cada palavra do inglês
  ("Total Refunded:", "Main Features") em vez de aplicar a regra do português ("Total
  reembolsado:", "Principais características"). Vale buscar esse padrão ativamente no
  arquivo, não só notar quando aparece por acaso — costuma se repetir várias vezes.
  **Zona cinzenta:** nomes de método de pagamento/produto que funcionam quase como marca
  (ex.: "Cartão de Crédito", "Boleto Bancário", "Frete Grátis") são mais defensáveis com
  Title Case do que rótulos genéricos de interface — não tratar como erro automático,
  mas notar a inconsistência se o mesmo termo aparecer capitalizado de formas diferentes
  em lugares diferentes do mesmo arquivo.
- **Concordância de gênero e número (erro gramatical, não estilo)** — diferente do item
  de "gênero evitado" abaixo (que é sobre inclusividade), aqui é sobre erro objetivo de
  concordância: artigo/adjetivo no gênero ou número errado em relação ao substantivo
  (ex.: "Remova TODOS **as** cartões" deveria ser "TODOS **os** cartões", já que "cartão"
  é masculino).
- **Gênero evitado quando possível** — reescrever a frase para neutralizar gênero em vez
  de usar "(a)" ou escolher um gênero arbitrário.
- **Tamanho da tradução** — aceitável ser 20–30% maior que o original corrido, mas em
  botões/menus deve tentar ficar mais compacto.
- **Atenção a ambiguidades e regência verbal** — string traduzida faz sentido sem o
  contexto do código/tela? Regência do verbo está correta em português?
- **Gerúndio com cuidado** — geralmente vira substantivo ("Printing new copies" →
  "Impressão de novas cópias"); gerúndio só quando indica ação em andamento agora. Se for
  título de seção, pode virar instrução no infinitivo ("Writing e-mails" → "Como escrever
  e-mails").
- **Cuidado com sinais de tradução automática não revisada** — estrutura estranha, erro de
  concordância, espaço extra colado em tags (ex.: "Registre-se <br> abaixo" em vez de
  "Registre-se<br>abaixo"). **Importante:** isso é uma checagem de sintomas, não uma
  conclusão sobre origem — ver seção 7.

### 4.3 Consistência terminológica

Aqui o teste é diferente do anterior: **o mesmo termo em inglês foi traduzido sempre da
mesma forma dentro do projeto?** Essa categoria pode legitimamente herdar problemas do
próprio original — se o inglês usa "retail" numa string e "regular price" em outra para o
mesmo conceito, a tradução inconsistente correspondente deve ser sinalizada como herdada
da inconsistência do original, não tratada como o mesmo tipo de erro que uma
inconsistência criada do zero pelo tradutor.

- **Consistência interna geral** — antes de apontar como erro, checar se a variação já
  existia no inglês original.
- **Checagens obrigatórias de glossário** (dois termos com histórico de erro recorrente
  em revisões anteriores — checar mesmo sem suspeita prévia):
  - `enable`/`disable` → glossário define **ativar**/**desativar**. "Habilitar"/
    "desabilitar" aparecem com frequência mas não são o termo padrão — e o erro tende a
    ser inconsistente dentro do próprio arquivo (ex.: botão diz "Ativar X" mas o status
    ao lado diz "X habilitado").
  - `please` → glossário diz explicitamente **não traduzir** ("não pedir por favor ao
    usuário"). Erro típico: 8-9 de 9 ocorrências corretas, com 1 exceção isolada mantendo
    "Por favor" — vale grep especificamente por isso.
  - `successfully` — guia de boas práticas recomenda omitir ("instalado com sucesso" →
    "instalado"), mas isso é mais uma preferência de estilo do que regra rígida; "com
    sucesso" é uso comum e aceitável em pt-BR quando usado de forma consistente no
    projeto. Não tratar como erro automático, só notar se quebrar consistência interna.
- Cruzar com o glossário **específico do projeto**, se existir (alguns plugins grandes,
  como o WooCommerce, têm termos próprios — ex.: "tax" não é "taxa").

### 4.4 Regras de conteúdo e comportamento do código

- **Sem ideologia inserida** — a tradução não adiciona opinião política/religiosa/cultural
  que não estava no original.
- **Comportamento do código preservado** — nenhuma alteração em parâmetros como
  `target="_blank"`, tags HTML ou lógica da string.
- **Placeholders intactos** — `%s`, `%d`, `%1$s`/`%2$s`, `%%`, `===VAR===`, `%@` etc.
  devem aparecer exatamente como no original (podem trocar de posição, nunca de tipo).
- **Sem links novos/aleatórios** — só devem existir links que já estavam no original ou
  que apontam para domínios wordpress.org/bbpress.org/documentação oficial.
- **Marcas e nomes preservados** — nome de marcas (WordPress, WooCommerce etc.) e nomes
  de plugins/temas **nunca** são traduzidos. Atenção: quando o "nome do plugin" no projeto
  de tradução é composto por marca + tagline descritiva (ex.: "Product Upload: AI Product
  Importer for WooCommerce"), é aceitável traduzir só a parte descritiva depois dos dois
  pontos, mantendo a marca intacta.

### 4.5 Outras boas práticas formais

- **Pontuação numérica invertida** — milhar com ponto, decimal com vírgula (1.500 / 1,5).
  Atenção: não aplicar essa conversão a números de versão de software (ex.: "WordPress
  6.2" continua "6.2", não "6,2").
- **Palavras desnecessárias removidas** — "please" e "successfully" geralmente não
  precisam de tradução literal (ver também seção 4.3 sobre o glossário).
- **Data e hora no padrão BR** — datas por extenso "dia de mês de ano"; formato curto
  `dd/mm/aaaa`; hora em formato 24h (`HH:mm`), não AM/PM.
- **Outros detalhes** — `#` → `nº`; verbos em botões/links de ação no infinitivo
  ("Update" → "Atualizar").

## 5. Formato de saída

**Padrão quando não especificado:** resumo executivo + mensagem pronta.

**Revisão detalhada string por string:** só quando pedida explicitamente.

**Quando o post for no fórum internacional (em inglês):** o formato que funcionou bem em
revisões anteriores foi gerar primeiro o resumo detalhado em português (pra você decidir
o que entra na versão pública) e só depois a mensagem em inglês — mais enxuta, preferindo
**linkar a string específica filtrada no GlotPress** em vez de citar o texto problemático
por extenso entre aspas. Ao montar esses links, confirmar o filtro de status correto
(`current_or_waiting_or_fuzzy_or_untranslated` é mais seguro que `waiting` isolado, que
pode não retornar nada se a string já tiver outro status).

## 6. Mensagens de feedback ao candidato

Ao montar a mensagem final, seguir o tom dos modelos oficiais de GTE
(https://br.wordpress.org/team/handbook/traducao/equipe/gte/#modelos-de-mensagem-padrao-para-revisao-de-pedidos-de-ptes):
agradecer a contribuição, ser específico sobre os ajustes necessários (citando
exemplos concretos do .po), e deixar claro o próximo passo (revisar e rejeitar as
sugestões problemáticas antes de virar PTE, ou confirmar aprovação se a qualidade
já estiver boa). Não reproduzir os modelos da página literalmente — usar como
referência de tom e estrutura, adaptando ao caso real.

**Estilo por canal.** O tom e formatação variam por canal de comunicação, não existe um
template único:
- **Slack**: texto plano, marcadores com "•" (não traço), tom casual e direto.
- **Fórum** (interno ou internacional): tom mais formal, como descrito acima.

Ao adaptar este documento para outro contexto, ajustar as regras de canal à realidade de
cada equipe.

No fórum internacional, outras equipes de locale costumam ser bem mais sucintas (sem citar
strings específicas, às vezes só linkando o guia de estilo geral). Isso não significa que
devemos fazer igual — a especificidade com exemplos concretos é uma prática deliberada da
equipe BR (handbook, seção acima), não um padrão universal do fórum. Manter a
especificidade é uma escolha válida e mais útil para o candidato, mesmo contrastando com
o tom mais seco de outras locales.

Quando o pedido de PTE partir do **próprio autor do plugin/tema** (em vez de um
colaborador/tradutor terceiro), pode ser útil linkar
https://br.wordpress.org/team/how-the-wordpress-brazilian-community-handles-pte-requests-from-authors/
em vez do processo padrão de candidatura
(https://br.wordpress.org/team/handbook/traducao/processo-de-aplicacao-para-pte/).

## 7. Limites e bom senso

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
