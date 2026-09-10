# Texto original (`msgid`) em idioma não-inglês

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
