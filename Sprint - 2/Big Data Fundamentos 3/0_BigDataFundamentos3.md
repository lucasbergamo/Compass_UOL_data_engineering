# Sumário

<details><summary><strong>Navegação</strong></summary>

1. [BIG DATA]()
2. [O V DE VOLUME EM BIG DATA]()
3. [Armazenamento e Processamento Paralelo]()
4. []()
5. []()
6. []()
7. []()
8. []()
9. []()
10. []()

</details>

## BIG DATA

- Neste exato momento, 2.5 quintilhões de bytes são gerados por dia para nortear indivíduos, empresas e governos, e está dobrando a cada dois anos.

- Cerca de 90% de todos os dados gerados no planeta, foram gerados nos últimos 2 anos.

- Aproximadamente 80% dos dados são não-estruturados ou estão em diferentes formatos, que dificulta a análise

- Toda vez que fazemos uma compra, uma ligação ou interagimos nas redes sociais, estamos produzindo esses dados.

- Com a recente conectividade em objetos, tal como relógios, carros e até geladeiras, as informações capturadas se tornam massivas e podem ser cruzadas para criar modelos preditivos cada vez mais elaborados, apontando e, até prevendo, o comportamento de empresas e clientes.

- BIG DATA é uma coleção de conjuntos de dados, grandes e complexos, que não podem ser processados por bancos de dados ou aplicações de processamento tradicionais

- o alto volume de dados gerado em alta velocidade e com muita variedade, isso é o que define BIG DATA

- O google estima que a humanidade criou nos últimos 5 anos, o equivalente a 300 exabytes de dados ou seja: 300.000.000.000.000.000.000

- Podemos definir o conceito de BIG DATA como sendo conjuntos de dados extremamente amplos e que, por este motivo, necessitam de ferramentas especialmente preparadas para lidar com grandes volumes, velocidade e variedade, de forma que toda e qualquer informação disponível nos dados possa ser encontrada, analisada e aproveitada em tempo hábil

- Análise de grades quantidades de dados para geração de resultados importantes que, em volumes menores dificilmente seriam alcançados

- O big data nos dá uma visão clara do que é granular, não temos de nos fixar na causalidade, Podemos descobrir padrões e correlações nos dados que nos propiciem novas e valiosas ideias

### Os 4Vs do Big Data: 

- Volume, Variedade, Velocidade e Veracidade

- para ser chamado de big data é preciso conter os 4 Vs em harmonia

**VOLUME (tamanho dos dados):**

- Espera-se que 40zettabytes de dados sejam criados por ano no mundo

- Cerca de 2.5 quintillionbytes de dados são criados por dia

- Existem atualmente cerca de 6 bilhões de telefones móveis no planeta

- Cada empresa americana armazena cerca de 100 Terabytes de dados.

**VARIEDADE (formato dos dados):**

- 150 exabytes é a estimativa de dados que foram gerados especificamente para tratamento de casos de doença em todo o mundo por ano desde 2011.

- Mais de 4 bilhões de horas por mês são usadas para assistir vídeos no YOUTUBE

- 30 bilhões de imagens são publicadas por mês no Facebook

- 200 milhões de usuários ativos por mês, publicam 400 milhões de tweets por dia

**VELOCIDADE (geração de dados):**

- 1 Terabyte de informação é criada durante uma única sessão da bolsa de valores Americana, a New York Stock Exchange (NYSE)

- Aproximadamente 100 sensores estão instalados nos carros modernos para monitorar nível de combustível, pressão dos pneus e muitos outros aspectos do veículo

- 18.9 bilhões de conexões de rede já existem no mundo

**VERACIDADE (confiabilidade dos dados):**

- Atualmente 1 em cada 3 gestores tem experimentado problemas relacionados a veracidade dos dados para tomar decisões de negócios

- Além disso, estima-se que 3.1 trilhões de dólares por ano sejam desperdiçados devido a problemas de qualidade dos dados.

### BIG DATA x CIÊNCIA DE DADOS

- Big Data é a matéria-prima, ou seja, dados.
- Ciência de dados é um conjunto de técnicas para análise de dados.
- Quando aplicamos ciência de dados ao big data extraímos valor e então temos o que é chamado de Big Data Anaytics.

### EXEMPLOS DE APLICAÇÃO DO BIG DATA ANALYTICS

- Uma companhia Aérea pode extrair, armazenar, processar e analisar dados de viagens dos passageiros a fim de oferecer rotas com maior probabilidade de venda.

- Uma rede de supermercados pode extrair, armazenar, processar e analisar dados de compras a fim de detectar padrões e organizar os produtos de forma a aumentar as vendas

- Uma rede de hotéis pode extrair, armazenar, processar e analisar dados de comentários de clientes em redes sociais para customizar seus serviços, aumentar as vendas e reduzir custos.

- Uma rede de hospitais pode extrair, armazenar, processar e analisar dados de exames médicos a fim de personalizar e otimizar o atendimento dos pacientes

- A parte mais relevante é o valor que voce extrai dos dados

- 1024 Kilobytes = 1 Megabyte

- 1024 Megabytes = 1 Gigabyte

- 1024 Gigabytes = 1 Terabyte

- 1024 Terabytes = 1 Petabyte

- 1024 Petabytes = 1 Exabyte

- 1024 Exabytes = 1 Zettabyte 

- 1024 Zettabytes = 1 Yottabyte [Facebook e Google estão aqui]

- 1024 Yottabytes = 1 Brontobyte

- 1024 Brontobytes = 1 Geobyte

----------

## O V DE VOLUME EM BIG DATA

- O V de volume é crítico em Big Data
- Como vamos armazenar grandes conjuntos de dados?
- Como vamos acessar grandes conjuntos de dados armazenados?
- Precisamos realmente armazenar tudo?
- Como armazenar Big Data?
- Os dados são estruturados ou podem ser estruturados antes do armazenamento?
	_Usamos um Data Warehouse!_
- Os dados não são estruturados ou Não podem ser estruturados antes do armazenamento?
	_Usamos um Data Lake ou um Data Store_

### BANCOS DE DADOS RELACIONAIS X NOSQL

### RELACIONAL

- Banco de dados relacionais são estruturados e com schema (organização dos dados) bem definido
- O schema é definido e criado antes do armazenamento dos dados
- Um data ware house, por exemplo é criado com alguma tecnologia de bando relacional como SGBD( sistema gerenciado de banco de dados) oracle, IBM DB2, Microsoft SQL Server, MySQL, PostgreSQL e muitos outros
- Em um banco de dados relacional os dados são organizados em tabelas que se relacionam

### NOSQL

- Bancos de dados Não relacionais (noSQL) partem do princípio que os dados podem ser semi ou não estruturados e que outros tipos de relacionamentos podem existir entre os dados
- Podemos usar bancos de dados NoSQL para construir data lakes e data stores (eles são conceitos)
- Normalmente não precisamos definir o schema antes do armazenamento ou o schema é definido no momento do armazenamento dos dados
- Existem diversos tipos de bancos de dados NoSQL : Key-Value, Graph Db (grafo), column family e Document

### DATA WAREHOUSES (DW)

- Um Data Warehouse é um sistema de armazenamento que conecta e harmoniza grandes quantidades de dados de muitas fontes diferentes
- O objetivo do DW é alimentar a inteligência de negócios (Business Intelligence), relatórios e análises e oferecer suporte aos requisitos de negócio, para que as empresas possam transformar seus dados em insights e tomar decisões inteligentes baseadas em dados
- Os DWs armazenam dados atuais e históricos em um único lugar e atuam como a única fonte de informações confiáveis para uma organização
- Os dados fluem para um DW a partir de sistemas transacionais ( como ERP e CRM ), bancos de dados e fontes externas, como sistemas de parceiros, dispositivos de internet das coisas (IoT), aplicativos de mídia social - geralmente em uma cadência regular

- O surgimento da computação em nuvem causou uma mudança no cenário

- Nos últimos anos, os locais de armazenamento de dados mudaram da infraestrutura local tradicional para vários locais, incluindo nuvem privada e nuvem pública

- O schema deve ser definido antes do processo de armazenamento dos dados

- Os DWs modernos são projetados para lidar com dados estruturados e não estruturados, como vídeos, arquivos de imagem e dados de sensor (embora data lakes ainda sejam opções melhores para dados não estruturados)

__“Exemplo nosql para data warehouse, uma empresa quer criar uma ia para detecção de tumor, a empresa tem um servidor com S.O, ela cria uma pasta e coloca todas as imagens de vários pacientes com raio x, as imagens são marcadas com Possui Tumor e Não possui tumor, a empresa não quer criar um data lake, então ela cria um  schema com uma tabela e 3 colunas = 1- nome da imagem, 2- id se tem tumor ou não, 3- caminho para pasta da imagem, É UMA QUESTÃO DE ARQUITETURA E NÃO DE TECNOLOGIA"__

- Alguns aproveitam a análise integrada e a tecnologia de banco de dados in-memory ( que mantém o conjunto de dados na memória do computador em vez de no armazenamento em disco ) para fornecer acesso em tempo real a dados confiáveis e impulsionar a tomada de decisões

- alguns SGBDs é possível colocar na memória ram, pois o acesso é mais rapido a memória do que no disco

- Sem Dw é muito difícil combinar dados de fontes heterogêneas, garantir que estejam no formato certo para análise e obter uma visão atual e de longo alcance dos dados ao longo do tempo

- Dw ainda é a principal forma de armazenar dados, data lake e data store ainda não superaram o DW

### BENEFÍCIOS DO DW

- Melhor análise de negócios: com o DW, os tomadores de decisão tem acesso a dados de várias fontes e não precisam mais tomar decisões com base em informações incompletas. 

- Consultas mais Rápidas: os DWs são construídos, especificamente para recuperação e análise rápida de dados. Com um DW, você pode consultar rapidamente grandes quantidades de dados consolidados com pouco ou nenhum suporte de TI.

- cuidado para não deixar o DW grande demais e causar demora nas consultas, é principal aspecto é a agilidade na consulta de dados

- Melhoria da qualidade dos dados: Antes de serem carregados no DW, os dados passam por um processo de limpeza garantindo que os dados sejam transformados em um formato consistente para apoiar análises e decisões, com base em dados precisos e de alta qualidade

- Visão histórica: ao armazenas dados históricos ricos, um data ware house permite que os tomadores de decisão aprendam com tendências e desafios passados, façam previsões e conduzam a melhoria contínua dos negócios.

### DATA LAKES

- No dw fazemos limpeza e transformação antes, acaba perdendo alguns dados no processo

- Um data lake é um repositório centralizado que permite armazenar todos os dados estruturados e não estruturados em qualquer escala. Podemos Armazenar os dados como estão na fonte, sem ter que primeiro estruturá-los e executar diferentes tipos de análises de painéis e visualizações a processamento de Big Data, análises em tempo real e aprendizado de máquina para orientar melhores decisões

- Dependendo dos requisitos, uma empresa típica exigirá um data Warehouse e um Data lake, pois eles atendem a diferentes necessidades e casos de uso

- A estrutura dos dados ou schema não é definida quando os dados são capturados, isso significa que você pode armazenar todos os dados em formato bruto sem a necessidade de saber quais perguntas de negócio deverão ser respondidas no futuro.

- Primeiro deve-se garantir a captura de todos os dados brutos direto no data lake e depois idealizar schema, ETL e passar pro DW para tomadas de decisões
- Diferentes tipos de análises, como consultar SQL , análises de Big Data, pesquisa de texto, análises em tempo real e aprendizado de máquina, podem ser usados para descobrir insights

- Os data lakes permitem que as empresas gerem diferentes tipos de percepções sobre os dados, desde relatórios sobre dados históricos até modelos preditivos criados com machine learning

- O principal desafio de uma arquitetura de data lake é que os dados brutos são armazenados sem supervisão do conteúdo. Para que um data lake torne os dados utilizáveis, ele precisa ter mecanismos definidos para catalogar e proteger os dados, Sem esses elementos, os dados não podem ser encontrados ou confiáveis, resultando em um “Pântano de dados” (DATA SWAMP). atender ás necessidades de públicos mais amplos exige que os data lakes tenham governança, gestão de metadados, consistência semântica e controle de acesso

- Data lake é um conceito e pode ser construído com diferentes tecnologias como APACHE HADOOP ou bancos de dados NOSQL.

- Podemos importar dados do DW para o Data lake e vice-versa dependendo das necessidades de negócio da empresa

- Para o DW normalmente usamos ETL ( extração, transformação e carga )

- Para o data lake normalmente usamos ELT ( Extração, carga e transformação )

- Data lakes e DWs podem fazer parte de uma grande estrutura central de armazenamento chamada Data Hub

### Benefícios do Data Lake

- Armazenamento em formato bruto: não precisamos limpar e transformar os dados antes do armazenamento

- Importação de qualquer quantidade de dados em tempo real: os dados são coletados de várias fontes e movidos para o data lake em seu formato original, Este processo permite dimensionar dados em qualquer tamanho, enquanto economiza tempo de definição de estruturas de dados, esquema e transformações

- Repositório centra para todos os dados da empresa: os data lakes permitem que várias funções como cientista de dados, engenheiros de machine learning, analista de dados e analista de negócios, acessem dados com sua ferramenta analítica específica.

- Sem necessidade de movimentação dos dados: análises podem ser executadas sem necessidade de mover os dados para um sistema de análise separado

### DEFININDO DATA STORES

- Um data store é um repositório para armazenar e gerenciar de forma persistente coleções de dados que incluem não apenas dados estruturados, mas também tipos de armazenamento variado , como documentos, dados no formato de chave-valor, filas de mensagens e outros formatos de arquivo

**Os tipos mais comuns de data stores:**

- Armazenamento de chave-valor ( Redis, Memcached )
- Motor de pesquisa de texto completo ( Elastic Search )
- Fila de mensagens ( Apache kafka )
- Sistemas de arquivos Distribuidos ( Hadoop HDFS, AWS S3 )

### Benefícios do Data Store

- Armazenamento de variados tipos de dados: dados que não se encaixam em outros repositórios de armazenamento

- Flexibilidade: armazenamento de dados aderente ás necessidades da aplicação final

- Suporte a dados semi-estruturados: dados que possuem alguma organização prévia, mas que devem ser usados em seu formato original

- Custo total menor: por se tratar de um tipo simplificado de armazenamento o custo total tende a ser menor que a outra solução de armazenamento

### SISTEMAS HÍBRIDOS DE ARMAZENAMENTO

- Com o avanço do Big data veremos cada vez mais sistemas híbridos de armazenamento, com dados armazenados em diferentes tipos de repositórios, local ou na nuvem.

- DWs, Data Lakes e Data Stores serão usados em conjunto criando assim uma grande estrutura de armazenamento de dados, um Data Hub.

----------
## Armazenamento e Processamento Paralelo

### O QUE É UM CLUSTER DE COMPUTADORES?

- Um servidor é um computador geralmente com alta capacidade computacional, que serve ( fornece) serviços de armazenamento, aplicações ou banco de dados

- Um servidor possui escalabilidade vertical, ou seja, há um limite até onde conseguimos incluir mais espaço em disco, mais processadores e mais memória RAM

- Um cluster de computadores é um conjunto de servidores com um mesmo propósito visando fornecer um tipo de serviço, como armazenamento ou processamento de dados

- Um cluster possui escalabilidade horizontal, ou seja, se quisermos aumentar a capacidade computacional incluímos mais máquinas no cluster ( além da escalabilidade vertical de cada máquina individual no cluster )

- Clusters de computadores são cada vez mais usados em Big data, o que nos permite realizar armazenamento e processamento paralelo através de diversas máquinas ( diversos servidores )

### O que é armazenamento Paralelo?

- Com clusters de computadores aumentamos de forma considerável a capacidade computacional

- O armazenamento paralelo consiste em distribuir o armazenamento de dados através de diversos servidores ( computadores ), o que permite aumentar de forma considerável a capacidade de armazenamento usando hardware de baixo custo

### Software para armazenamento paralelo - APACHE HADOOP

- Precisamos de um sistema de arquivos distribuido. Seu computador pessoal tem um sistema de arquivos ( NTFS, ext3, etc ) mas ele não foi desenvolvido para armazenamento distribuido

- Entre algumas opções, o Apache Hadoop HDFS ( hadoop distributed file system) tem se mostrado a solução ideal para gerenciar o armazenamento distribuido em um cluster de computadores 



- O HDFS é o software responsável pela gestão do cluster de computadores definido como os arquivos serão distribuídos através do cluster

- Com o HDFS podemos construir um data lake que roda sobre um cluster de computadores e permite o armazenamento de grandes volumes de dados com hardware commodity ( de baixo custo )

- O HDFS permitiu que o big data pudesse ser usado em larga escala !


### Processamento paralelo de Big Data

- Resolvemos um problema. Podemos agora armazenar grandes quantidades de dados em um cluster computadores através de armazenamento paralelo de dados

- mas como vamos processar os dados se eles estão agora distribuidos em diversos computadores?

- No Processamento paralelo o objetivo é dividir uma tarefa em várias sub-tarefas e executá las em paralelo

- O apache hadoop Map reduce e o Apache Spark são dois frameworks para esse propósito

- Ao usar um framework de processamento paralelo, as sub-tarefas são levadas para o processador da máquina do cluster onde os dados estão armazenados, aumentando assim a velocidade de processamento de grandes volumes de dados

### Arquitetura de armazenamento e processamento paralelo

- O HDFS é um serviço rodando em todas as máquinas do cluster, sendo um NameNode para gerenciar o cluster e os dataNodes que fazem o trabalho de armazenamento propriamente dito

- O MapReduce também é um serviço rodando em todas as máquinas do cluster, sendo um Job Tracker para gerenciar o processamento e os Task Trackers que fazem o trabalho de processamento

- O Job Tracker consulta o NameNode a fim de saber a localização dos blocos de dados nas máquinas do cluster

- Os task trackers se comunicam com os DataNodes para obter os dados do disco, executar o processamento e então retornar o resultado ao Job Tracker

- Essa arquitetura permite armazenar e processar grandes quantidades de dados e assim extrair valor do Big Data atraves da análise de dados

### Soluções de armazenamento e processamento Paralelo

Na nuvem: 

- Azure HDInsight
- Amazon EMR

- Databricks foi a mesma equipe que desenvolveu o SPARK para criar lakehouse plataform

----------

##



----------

##



----------

##



----------

##



----------

##



----------

##



----------

##



----------