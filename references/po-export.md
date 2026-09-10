# Como baixar o `.po`

Formato esperado:

- **Sempre `.po`**, nunca `.mo` (binário, ilegível).
- Se vier `.mo` por engano, pedir o `.po` correspondente antes de revisar.

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
