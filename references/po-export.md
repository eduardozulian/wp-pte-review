# Como baixar o `.po`

O candidato não envia arquivo: o `.po` é sempre exportado do translate.wordpress.org.
Sempre `.po`, nunca `.mo` (binário, ilegível).

Antes de exportar, identificar no post do pedido:

- o **slug** do projeto (a parte final da URL em wordpress.org/plugins/ ou
  wordpress.org/themes/);
- o **nome de usuário** do candidato no WordPress.org (o que aparece em
  profiles.wordpress.org/<usuario>/).

## Caminho principal: URL de export direto

O export pode ser baixado direto pela URL, sem passar pela interface:

```text
https://translate.wordpress.org/projects/wp-plugins/<slug>/stable/pt-br/default/export-translations/?filters[status]=waiting&filters[user_login]=<usuario>&format=po
```

- **`filters[user_login]` é essencial.** Sem ele, o export traz as sugestões
  pendentes de todo mundo que contribuiu com o projeto, e a revisão acabaria avaliando
  o trabalho de outras pessoas.
- **Temas** não têm o subprojeto `stable`: usar
  `/projects/wp-themes/<slug>/pt-br/default/export-translations/?...`.
- **Readme do plugin** é um subprojeto separado: trocar `stable` por `stable-readme`.
  Se o candidato traduziu os dois, exportar e revisar os dois.
- **Development** (`dev`, `dev-readme`) só se o pedido for especificamente sobre uma
  versão em desenvolvimento.
- **Status:** `waiting` (aguardando aprovação) é o caso mais comum em pedidos de PTE,
  mas não é regra fixa. Se o candidato já teve strings aprovadas ou rejeitadas, outros
  status podem ser relevantes; `current_or_waiting_or_fuzzy_or_untranslated` traz tudo.

Exemplo de download por linha de comando:

```bash
curl -sL -o candidato.po 'https://translate.wordpress.org/projects/wp-plugins/<slug>/stable/pt-br/default/export-translations/?filters%5Bstatus%5D=waiting&filters%5Buser_login%5D=<usuario>&format=po'
```

**Se o export sair vazio** (só o cabeçalho, sem strings), conferir nesta ordem: o slug,
o nome de usuário, o subprojeto (`stable` ou `stable-readme`) e o status. Um export vazio
com todos esses dados certos significa que o candidato não tem strings naquele status.

## Alternativa: pela interface

1. Acessar `https://translate.wordpress.org/locale/pt-br/default/wp-plugins/<slug>/`
   (ou `wp-themes/` para temas) e entrar no subprojeto relevante.
2. Em **Filter**, escolher o status (geralmente **Waiting**) e preencher o **usuário**
   do candidato.
3. No fim da página, no dropdown ao lado de **Export**, selecionar **"Only matching the
   filter"**. O padrão exporta o projeto inteiro e ignora o filtro. Depois clicar em
   **Export** e escolher o formato **PO**.

Se o export sair muito maior que o esperado, checar primeiro se o dropdown ficou em
"Only matching the filter" antes de tratar como problema do candidato.
