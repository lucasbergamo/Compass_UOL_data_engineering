1. uma locação só pode ter 1 cliente mas 1 cliente pode ter N locações
2. no modelo conceitual invertemos a cardinalidade



2 - a ultima é modelagem dimensional





1- primeiro se cria um modelo conceitual

1- a normalização é um processo dentro das tabelas para que evite anomalias, ex redudância de dados 

2- 1fn, 2fn, 3fn

3- 1fn Uma tabela deve possuir:

- Apenas valores atômicos
- não há grupos de atributos repetidos
- Existe uma chave primária(candidata)
- Não possui atributos multivalorados, compostos ou relações aninhadas (uma tabela dentro da outra)

- compostos pode ser o endereço que devemos dividir em rua, cep, estado, cidade...
- Já multivalorados pode ser o telefone, pois ela pode ter mais de 1


Esses sistemas de gerenciamento de banco de dados são conhecidos pela sigla SGBD e são os responsáveis por armazenar, manter e prover acesso de maneira controlada e segura à sua base de dados. Para tanto antes, é necessário que os bancos de dados sejam projetados segundo uma estrutura clara e bem definida, em um modelo teórico, chamado modelo conceitual.  Posteriormente, por intermédio dos SGBD, conseguimos transformar todo esse modelo conceitual em um modelo físico e real com toda a estrutura anteriormente projetada.

Então, para não restar dúvidas, o banco de dados é a base de dados, o agrupamento de dados de mesma natureza que ficam armazenados e gerenciados por intermédio dos sistemas gerenciadores de banco de dados.

Pode fazer uma analogia com a vida real: em um escritório, podem existir várias gavetas e armários com documentos separados em pastas, fichas ou até mesmo uma simples agenda. A organização dessas informações é que faz toda a diferença quando pensamos em banco de dados. A Fig. 2 ilustra um banco de dados no mundo real, com uma gaveta com pastas de documentos organizados.

Enquanto isso, os SGBDs, em nossa analogia, seriam os profissionais responsáveis em manter e manipular os documentos dessa gaveta no mundo real. 

**Analisando a Tabela 1, é perceptível que está dividida colunas. Essas colunas são os as divisões ou campos que agruparão os dados separadamente. Em um sistema de banco de dados computacional, essa tabela recebe o nome de entidade, muito embora que o nome tabela também seja bem praticado. Já suas colunas são os atributos da entidade, também conhecidos como campos.**

Os dados propriamente ditos estão nas linhas, onde aparecem as características de cada produto. Essas linhas com dados sãs chamadas de instâncias da entidade, conhecidas também por tuplas ou registros, que é o nome mais popularmente conhecido.





