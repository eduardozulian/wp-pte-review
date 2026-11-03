# Checklist de boas práticas

Baseado em: https://br.wordpress.org/team/handbook/traducao/boas-praticas/
(versão em inglês, espelhada quase 1:1: https://make.wordpress.org/polyglots/handbook/translating/expectations/)

Cada seção da página de boas práticas tem um item correspondente aqui. As seções
"O que é internacionalização?", "Aprenda com outras localizações" e "Colabore" orientam
quem traduz e não viram critério de revisão. Do "Colabore" vem só a possibilidade de
rejeitar em massa, tratada na seção de limites do `SKILL.md`. Se a página mudar, conferir
de novo esta correspondência.

O checklist está dividido em camadas com prioridade diferente. **Defeitos técnicos são
sempre bloqueantes**, independente da qualidade do resto do arquivo — não tratar como
"ponto de estilo" na comunicação com o candidato.

## Defeitos técnicos (bloqueantes)

- **Strings com texto duplicado/colado** — duas versões da mesma frase (ou frases
  diferentes) coladas sem espaço ou separador. Geralmente erro de merge/cópia de
  sugestões, não tradução ruim. Mostraria texto quebrado pro usuário final.
- **Corrupção de encoding** — caracteres especiais (acentos, travessão) virando sequências
  de bytes sem sentido.
- **Placeholders ou tags quebrados** — `%s`/`%d`/`%1$s` removidos, trocados de tipo,
  placeholders sem número trocados de ordem, ou tags HTML mal formadas que quebrariam o
  layout/funcionamento da página. Detalhes em "Placeholders intactos", abaixo.

Esses três pontos, se presentes, devem aparecer primeiro e com destaque no resumo e na
mensagem ao candidato — não importa quão boa seja a fluência do resto do arquivo, **não
recomendar aprovação de PTE enquanto eles existirem**.

## Fluência do português

O teste central aqui é: **lendo só a tradução, sem olhar o original, isso é como um
brasileiro escreveria ou falaria?** Isso é diferente de consistência terminológica — uma
tradução pode ser perfeitamente consistente e ainda soar estranha, e vice-versa.

- **Tradução orgânica, não literal** — a ideia foi transmitida de forma natural em
  português, sem replicar a estrutura da frase em inglês? Cuidado especial com frases que
  empilham reforços redundantes (ex.: "às centenas de uma vez", "em massa de uma vez" —
  cada termo já carrega a ideia de quantidade/simultaneidade, não precisa reforçar com
  os dois ao mesmo tempo).
- **Formalidade equivalente** — o tom informal/educado do original foi mantido sem
  formalizar demais (ex.: "Use" em vez de "Utilize", "têm" em vez de "possuem") nem
  inserir elementos novos (emojis, gírias) que não estavam no original? Exceção: um emoji
  que já estava no original e não é culturalmente adequado pode ser trocado.
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
  contexto do código/tela? ("Backup settings" pode ser "Fazer backup das configurações"
  ou "Configurações de backup"; só o contexto decide.) Regência do verbo está correta em
  português? Tradução literal costuma errar aqui: "pesquisar todos os computadores", e
  não "pesquisar **por** todos os computadores".
- **Gerúndio com cuidado** — geralmente vira substantivo ("Printing new copies" →
  "Impressão de novas cópias"); gerúndio só quando indica ação em andamento agora. Se for
  título de seção, pode virar instrução no infinitivo ("Writing e-mails" → "Como escrever
  e-mails"). Em locuções verbais, evitar o gerúndio: "You will be writing" → "Você vai
  escrever" ou "Você escreverá", nunca "Você vai estar escrevendo".
- **Pronomes desnecessários** — a maioria dos pronomes do inglês não precisa ser
  traduzida ("Refer to this article if you need assistance" → "Consulte este artigo caso
  precise de ajuda", sem "você").
- **Cuidado com sinais de tradução automática não revisada** — estrutura estranha, erro de
  concordância, espaço extra em volta de tags ou placeholders (ex.: "Registre-se <br>
  abaixo" em vez de "Registre-se<br>abaixo"), o que pode quebrar o funcionamento da
  string. **Importante:** isso é uma checagem de sintomas, não uma
  conclusão sobre origem — ver a seção de limites e bom senso no `SKILL.md`.

## Consistência terminológica

Aqui o teste é diferente do anterior: **o mesmo termo em inglês foi traduzido sempre da
mesma forma dentro do projeto?** Essa categoria pode legitimamente herdar problemas do
próprio original — se o inglês usa "retail" numa string e "regular price" em outra para o
mesmo conceito, a tradução inconsistente correspondente deve ser sinalizada como herdada
da inconsistência do original, não tratada como o mesmo tipo de erro que uma
inconsistência criada do zero pelo tradutor.

- **Consistência interna geral** — antes de apontar como erro, checar se a variação já
  existia no inglês original.
- **Consistência com outros projetos** — para termos fora do glossário, ver como outros
  projetos pt-BR traduziram na ferramenta de consistência
  (https://translate.wordpress.org/consistency/, escolher o conjunto `pt-br/default`).
  Uma tradução que diverge do uso estabelecido em outros projetos merece ser apontada.
- **Glossário completo** — todo termo do glossário geral (e do glossário do projeto, se
  houver) que aparece no texto original deve seguir a tradução definida. O
  `scripts/glossary-check.py` lista os candidatos a desvio (ver passo 5 do `SKILL.md`).
  Para julgar cada candidato:
  - **Classe da palavra importa.** O glossário separa substantivo de verbo ("display":
    *exibir* como verbo, *exibição* como substantivo; "Block" como substantivo é *bloco*,
    do editor, e não se aplica a "blocked spam").
  - **As notas do glossário são regras.** Algumas entradas não têm tradução e a regra está
    só na nota ("please": não traduzir; "thank you": traduzir só quando agradecer é o
    objetivo da string).
  - **Desvio justificado não é erro**, mas precisa de motivo concreto no contexto da
    string (ver seção de limites e bom senso no `SKILL.md`).
  - **Inconsistência dentro do arquivo agrava o desvio**: o mesmo termo traduzido de
    formas diferentes em strings diferentes é pior que um desvio aplicado de forma
    consistente.
- **Checagens obrigatórias de glossário** (dois termos com histórico de erro recorrente
  em revisões anteriores — checar mesmo sem suspeita prévia):
  - `enable`/`disable` → glossário define **ativar**/**desativar**. "Habilitar"/
    "desabilitar" aparecem com frequência mas não são o termo padrão — e o erro tende a
    ser inconsistente dentro do próprio arquivo (ex.: botão diz "Ativar X" mas o status
    ao lado diz "X habilitado").
  - `please` → glossário diz explicitamente **não traduzir** ("não pedir por favor ao
    usuário"). Erro típico: 8-9 de 9 ocorrências corretas, com 1 exceção isolada mantendo
    "Por favor" — vale grep especificamente por isso.
  - `successfully` — o guia de boas práticas diz que essa palavra "pode e deve ser
    eliminada" ("The plugin was installed successfully" → "O plugin foi instalado"). Pedir
    o ajuste, mas como ponto de estilo, não como defeito bloqueante. Se "com sucesso"
    aparecer só em parte das strings, apontar também a inconsistência.
- Cruzar com o glossário **específico do projeto**, se existir (alguns plugins grandes,
  como o WooCommerce, têm termos próprios — ex.: "tax" não é "taxa").

## Regras de conteúdo e comportamento do código

- **Sem ideologia inserida** — a tradução não adiciona opinião política/religiosa/cultural
  que não estava no original.
- **Comportamento do código preservado** — nenhuma alteração em parâmetros como
  `target="_blank"`, tags HTML ou lógica da string.
- **Placeholders intactos** — `%s`, `%d`, `%1$s`/`%2$s`, `%%`, `===VAR===`, `%@` etc.
  devem aparecer na tradução na mesma quantidade e com o mesmo tipo do original. Em
  strings com placeholders, o sinal de porcentagem é escrito `%%` (`%d%%` é válido e
  mostra "50%"); um `%` sozinho na tradução quebra a string.
  - **Mudar de posição só vale para placeholders numerados.** `%2$s contém %1$d macacos`
    é uma tradução válida de `%d macacos estão contidos em %s`. Já com dois `%s` sem
    número (`%s respondeu a %s`), a ordem é fixa: se a tradução inverter a frase, os
    valores trocam de lugar sem nenhum aviso (quem respondeu vira quem recebeu). Nesse
    caso a tradução precisa manter a ordem original ou o código precisa passar a usar
    placeholders numerados.
  - **Plural:** quando o original no singular tem `%d` ("%d item"), a tradução no
    singular também deve manter o `%d`. Em pt-BR a forma singular também é usada para
    zero, então "Um item" mostraria "Um item" quando houver 0 itens.
  - Verificação automática:
    ```bash
    python3 ~/.claude/skills/wp-pte-review/scripts/placeholder-check.py candidato.po
    ```
    O script compara placeholders, tags HTML e atributos (`href`, `target`, `rel`...)
    entre original e tradução e avisa quando há dois ou mais placeholders sem número.
    Os exports do translate.wordpress.org não marcam as strings como `php-format`, por
    isso `msgfmt --check-format` não detecta esses problemas.
- **Sem links novos/aleatórios** — só devem existir links que já estavam no original ou
  que apontam para domínios wordpress.org/bbpress.org/documentação oficial. Link
  comercial inserido na tradução é falta grave (o handbook diz que pode levar à remoção
  da pessoa da equipe de tradução): não recomendar PTE enquanto ele existir.
- **Marcas e nomes preservados** — nome de marcas (WordPress, WooCommerce etc.) e nomes
  de plugins/temas **nunca** são traduzidos, e a grafia da marca é respeitada:
  "Wordpress" ou "Woocommerce" (sem a maiúscula no meio) é erro. Atenção: quando o
  "nome do plugin" no projeto de tradução é composto por marca + tagline descritiva
  (ex.: "Product Upload: AI Product Importer for WooCommerce"), é aceitável traduzir só a
  parte descritiva depois dos dois pontos, mantendo a marca intacta.

## Outras boas práticas formais

- **Pontuação numérica invertida** — milhar com ponto, decimal com vírgula (1.500 / 1,5).
  Atenção: não aplicar essa conversão a números de versão de software (ex.: "WordPress
  6.2" continua "6.2", não "6,2").
- **Palavras desnecessárias removidas** — "please" e "successfully" devem ser eliminadas
  ("Please login to view this content" → "Acesse o site para ver este conteúdo"). Ver
  também as checagens obrigatórias de glossário acima.
- **Data e hora no padrão BR** — datas por extenso "dia de mês de ano"; formato curto
  `dd/mm/aaaa`; hora em formato 24h (`HH:mm`), não AM/PM. Plugins e temas costumam ter
  **strings de formato de data do PHP** para traduzir; elas não são texto, são códigos:

  | Original | Tradução esperada | Resultado |
  |---|---|---|
  | `F j, Y` | `j \d\e F \d\e Y` | 27 de maio de 2003 |
  | `m/d/Y` | `d/m/Y` | 27/05/2003 |
  | `g:i a` | `H:i` | 18:30 |
  | `g:i:s a` | `H:i:s` | 18:30:21 |

  Traduzir as letras ("F j, Y" → "M d, A") ou esquecer as barras invertidas em `\d\e`
  quebra a data exibida. O formato de texto "18h30" é correto em português, mas o
  handbook prefere o formato digital (`18:30`) em plugins e temas.
- **Outros detalhes** — `#` → `nº`; verbos em botões/links de ação no infinitivo
  ("Update" → "Atualizar").
