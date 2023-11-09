**Sumário**

[Retornar](https://github.com/lucasbergamo/Compass_UOL_data_engineering)

<details><summary><strong>Navegação</strong></summary>

- [Introdução](#introdução)
  - [O que é Docker?](#o-que-é-docker)
  - [Por quê Docker?](#por-quê-docker)
  - [Qual versão utilizar?](#qual-versão-utilizar)
  - [Instalação Docker Windows](#instalação-docker-windows)
  - [Extensão Docker no VScode](#extensão-docker-no-vscode)
  - [Alternativa ao terminal do Windows](#alternativa-ao-terminal-do-windows)
    - [Windows Terminal](#windows-terminal)
  - [Rodando um container no Docker](#rodando-um-container-no-docker)
- [Trabalhando com Containers](#trabalhando-com-containers)
  - [O que são containers?](#o-que-são-containers)
  - [Container x Imagem](#container-x-imagem)
  - [Rodando um Container](#rodando-um-container)
  - [Verificar containers que já executados ou em execução](#verificar-containers-que-já-executados-ou-em-execução)
  - [Rodando container no modo iterativo ( -it )](#rodando-container-no-modo-iterativo---it-)
  - [Container x VM ( Virtual Machine )](#container-x-vm--virtual-machine-)
  - [Rodando container em background ( detached )](#rodando-container-em-background--detached-)
  - [Expondo portas de container](#expondo-portas-de-container)
  - [Parando containers](#parando-containers)
  - [Reiniciando Containers](#reiniciando-containers)
  - [Definindo nome para um container](#definindo-nome-para-um-container)
  - [Acessando os logs de um container](#acessando-os-logs-de-um-container)
  - [Removendo container](#removendo-container)
- [Criando Imagens e avançando em containers](#criando-imagens-e-avançando-em-containers)
  - [O que é uma imagem?](#o-que-é-uma-imagem)
  - [Como escolher uma boa imagem](#como-escolher-uma-boa-imagem)
  - [Criando uma imagem](#criando-uma-imagem)
  - [Rodando nossa imagem em um container](#rodando-nossa-imagem-em-um-container)
  - [Alterando uma imagem](#alterando-uma-imagem)
  - [Cache de camadas](#cache-de-camadas)
  - [Download de imagens](#download-de-imagens)
  - [Mais informações sobre os comandos](#mais-informações-sobre-os-comandos)
  - [Múltiplas aplicações do mesmo container](#múltiplas-aplicações-do-mesmo-container)
  - [Nomeando Imagens](#nomeando-imagens)
  - [Nomeando imagem no build](#nomeando-imagem-no-build)
  - [Reiniciando Container com iteratividade ( start interativo )](#reiniciando-container-com-iteratividade--start-interativo-)
  - [Removendo imagens](#removendo-imagens)
  - [Removendo imagens e containers não utilizados](#removendo-imagens-e-containers-não-utilizados)
  - [Removendo container após utilização](#removendo-container-após-utilização)
  - [Copiando arquivos entre containers](#copiando-arquivos-entre-containers)
  - [Verificando informações de processamento de container](#verificando-informações-de-processamento-de-container)
  - [Inspecionar dados do container](#inspecionar-dados-do-container)
  - [Verificando processamento do docker](#verificando-processamento-do-docker)
  - [Autenticação no terminal](#autenticação-no-terminal)
  - [Encerrando autenticação](#encerrando-autenticação)
  - [Enviando imagens para o Docker Hub](#enviando-imagens-para-o-docker-hub)
  - [Atualizando imagens no Hub](#atualizando-imagens-no-hub)
  - [Baixando e utilizando nossa imagem](#baixando-e-utilizando-nossa-imagem)
- [Introduzindo volumes aos nossos containers](#introduzindo-volumes-aos-nossos-containers)
  - [O que são Volumes?](#o-que-são-volumes)
  - [Tipos de volumes](#tipos-de-volumes)
  - [Criando o projeto para trabalhar com volumes](#criando-o-projeto-para-trabalhar-com-volumes)
  - [O problema da persistência de dados](#o-problema-da-persistência-de-dados)
  - [Volumes Anônimos](#volumes-anônimos)
  - [Volumes Nomeados](#volumes-nomeados)
  - [Bind mounts](#bind-mounts)
  - [O poder extra do Bind mount](#o-poder-extra-do-bind-mount)
  - [Criando volumes manualmente](#criando-volumes-manualmente)
  - [Listando volumes](#listando-volumes)
  - [Inspecionando volumes](#inspecionando-volumes)
  - [Removendo volumes](#removendo-volumes)
  - [Remoção de volumes em massa](#remoção-de-volumes-em-massa)
  - [Volume somente leitura](#volume-somente-leitura)
- [Conectando containers com networks](#conectando-containers-com-networks)
  - [O que são networks?](#o-que-são-networks)
  - [Tipos de conexão](#tipos-de-conexão)
  - [Tipos de rede (Drivers)](#tipos-de-rede-drivers)
  - [Listando Networks (redes)](#listando-networks-redes)
  - [Criando redes](#criando-redes)
  - [Removendo redes](#removendo-redes)
  - [Removendo redes não utilizadas](#removendo-redes-não-utilizadas)
  - [Instalando o Postman](#instalando-o-postman)
  - [Conexão Externa](#conexão-externa)
  - [Conexão com máquina host](#conexão-com-máquina-host)
  - [Conexão entre containers](#conexão-entre-containers)
  - [Conexão entre containers](#conexão-entre-containers-1)
  - [Desconectando um container](#desconectando-um-container)
  - [Inspecionando redes](#inspecionando-redes)
- [Introdução ao YAML](#introdução-ao-yaml)

</details>

## Introdução

### O que é Docker?

- O **Docker** é um software que **reduz a complexidade de setup** de aplicações;
- Onde **configuramos containers**, que são como servidores para rodar nossas aplicações;
- Com facilidade, podemos criar **ambientes independentes** e que funcionam em diversos SO's;
- E ainda deixa os projetos **perfomáticos**;

### Por quê Docker?

- O **Docker** proporciona mais velopcidade na configuração do ambiente de um dev;
- **Pouco tempo gasto em manutenção**, containers são executados como configurados;
- **Performance** para executar aplicação, mais performático que uma VM;
- Nos livra da **Matrix from Hell**;

### Qual versão utilizar?

- O **Docker** é dividido em duas versões: **CE x EE**
- CE é a **Community Edition**, edição gratuita, que nos possibilita utilizar o Docker normalmente, é a que vamos optar;
- EE é a **Enterprise Edition**, edição paga, há uma garantia maior das versões que são disponibilizadas e você tem suporte do time do Docker;

### Instalação Docker Windows

- Para windows vamos instalar um software chamado **Docker Desktop**;
- Com ele virá a possibilidade também de rodar **Docker no terminal**, que é onde aplicaremos a maioria dos comandos durante o curso;
- Docker Desktop é uma **interface** para trabalhar com o Docker;
- Obs: Há duas versões, a que você vai instalar **depende da versão do seu windows**;

- [Docker Download](https://www.docker.com/products/docker-desktop/)
  - Habilitar Hyper-v

- [WSL](https://learn.microsoft.com/pt-br/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
- [WSL2](https://learn.microsoft.com/pt-br/windows/wsl/install)
- O Docker exige o Wsl 2 no windows

após instalar o docker -> reiniciar -> instalar o wsl -> abrir o docker;

usar esses comandos no cmd para verificar se está funcionando:
  - ```docker ps```
  - ```docker version```

### Extensão Docker no VScode

- Procurar e instalar extensão **Docker**

### Alternativa ao terminal do Windows

- Git bash pode apresentar problemas, nao indicado utilizar
- temos uma alternativa chamada comander( [cmder](https://cmder.app/) )

#### Windows Terminal

- Baixar Windows Terminal pela microsoft store
- Configurar o terminal para abrir automaticamente no WSL. Selecionar a sua distro no menu da primeira opção Ubuntu 22.04 LTS.
- No menu Interaction, basta marcar a primeira opção (copy selection to clipboard)
- adicionar o tema Dracula, clicando em Open JSON file, e copiando o schema do [Dracula](https://draculatheme.com/windows-terminal)

- Para mais dicas, vizualizar o tutorial : 

  [Configuração do Windows para desenvolvimento](https://dev.to/1cadumagalhaes/configuracao-do-windows-para-desenvolvimento-blk)


### Rodando um container no Docker

- Vamos testar o Docker utilizando uma **imagem real**;
- Para rodar containers utilizamos o comando ```docker run```;
- Neste comando **podemos passar diversos parâmetros**;
- Neste exemplo vamos passar apenas o nome da imagem que é **docker/whalesay**
- Um comando chamado **cowsay** e uma mensagem

Abrir o terminal:
  - verificar se as instancias estao sendo executadas
  - ```wsl.exe -l -v```
  - ```docker run docker/whalesay cowsay Hello_World```

__Exemplificando:__

- vai rodar uma imagem whalesay do diretório do hub do docker, com o comando cowsay e uma saida hello_World, porém vai rodar e parar pois não tem a flag -it

## Trabalhando com Containers

### O que são containers?

- Um **Pacote de código que pode executar uma ação**, por exemplo: rodar uma aplicação de Node.js, PHP, Python e etc;
- Ou seja, os nossos projetos serão executados dentro dos containers que criarmos/utilizarmos;
- **Containers utilizam imagens** para poderem ser executados;
- **Múltiplos containers podem rodar juntos**, exemplo: um para PHP e outro para MySQL;


### Container x Imagem

- **Imagem e Container** são recursos fundamentais do Docker;
- Imagem é o **"Projeto"** que será executado pelo container, todas as instruções estarão declaradas nela;
- Container é o **Docker rodando alguma imagem**, consequentemente executando algum código proposto por ela;
- O fluxo é: programamos uma imagem e a executamos por meio de um container;


### Rodando um Container

- Vamos encontrar imagens no repositório do [Docker](https://hub.docker.com)
- Nesse site podemos verificar quais as imagens existem da tecnologia que estamos procurando, por exemplo: Node.js, Ubuntu;
- E também **aprender a como utilizá-las**;
- Vamos executar uma imagem em um container com o comando: ```docker run <imagem>```
- O comando RUN, sempre cria um novo container

Passo a passo:
- ```docker run ubuntu``` ( cria e interrompe a imagem, não acontece nada pois não foi dito oq era pra ser feito )
- ```docker run -it ubuntu``` ( criou e continua rodando a imagem)
- agora temos acesso ao terminal da nova imagem instalada do ubuntu
- podemos utilizar o ```docker ps``` para checar o status das que estão sendo executadas

### Verificar containers que já executados ou em execução

- O comando ```docker ps``` ou ```docker container ls``` exibe quais containers estão sendo executados no momento;
- Utilizando a flag **-a**, temos também todos os containers ja executados na máquina;
- Este comando é útil para **entender o que está sendo executado e acontece** no nosso ambiente;
- Exemplo : ```docker ps -a``` ```docker container ls -a```

### Rodando container no modo iterativo ( -it )

- Podemos rodar um container e deixá-lo **executando no terminal**;
- com isso o terminal ficará travado no container
- Vamos utilizar a **flag -it**;
- Desta maneira **podemos executar comandos disponíveis no container** que estamos utilizando o comando run;
- Podemos utilizar a imagem do ubuntu para isso!
  
- ```docker run -it node``` vai criar e baixar uma imagem do nodejs rodando no terminal
- para sair : **Ctrl c + Ctrl c**

### Container x VM ( Virtual Machine )

- **Container é uma aplicação que serve para um determinado fim**, não possui sistema operacional, seu tamanho é de alguns mbs;
- VM possui sistema operacional próprio, tamanho de gbs, **pode executar diversas funções ao mesmo tempo**
- Containers acabam gastando menos recursos para serem executados, por causa do seu uso específico
- VMs gastam mais recursos, porém podem exercer mais funções;

### Rodando container em background ( detached )

- Quando iniciamos um container que persiste (-it), **ele fica ocupando o terminal**;
- Podemos executar um container em background, para não precisar ficar com diversas abas de termminal aberto, utilizamos a **flag -d(detached)**;
- Verificamos **containers em background com docker ps** também;
- Podemos utilizar o __nginx ( servidor web, identico ao apache )__ para este exemplo!
- Inicia um container em background: ```docker run -d nginx```
- parando um container utilizando o dado em NAMES```docker stop charming_fermi``` 

### Expondo portas de container

- porta 80 é a porta padrão do acesso web.
- Os **containers de docker não tem conexão com nada de fora deles;
- Por isso precisamos expor portas, a flag é a **-p** e podemos fazer assim:
  - -p 80:80;
- Desta maneira **o container estará acessível na porta 80**;
- Podemos testar este exemplo com o nginx !


O primeiro número é a porta que está expondo o pc e a segunda é a do container
  - pc:container

```docker run -d -p 80:80 nginx``` (localhost:80/)
```docker run -d -p 3000:80 nginx``` (localhost:3000/)

### Parando containers

- Podemos para um container com o comando ```docker stop <id ou nome>```;
- Desta maneira estaremos liberando recursos que estão sendo gastos pelo mesmo:
- Podemos verificar os containers rodando com o comando ```docker ps```;
- ```docker stop afb6e877c259```

### Reiniciando Containers

- Aprendemos já a parar um container com o stop, para voltar a rodar um container usar o comando ```docker start <id>```;
- Lembre-se que **o run sempre cria um novo container**;
- Então caso seja necessário aproveitar um antigo, opte pelo start;
- podemos selecionar o conteiner com os 4 primeiros caracteres do ID
  ```docker stop afb6```

### Definindo nome para um container

- Podemos definir um nome do container com a flag **--name**;
- Se não colocarmos, **recebemos um nome aleatório**, o que pode ser um problema para uma aplicação profissional;
- A flag run é inserida junto do **comando run**;

__Exemplificando:__

1- Nome
2- Imagem nginx
- ```docker run -d -p 80:80 --name nginx_app nginx```
- ```docker stop nginx_app```

### Acessando os logs de um container

- Podemos **verificar o que aconteceu em um container** com o comando logs;
- Utilizamos da seguinte maneira: ```docker logs <id>```
- As últimas ações realizadas no container, serão **exibidas no terminal**;
- flag **-f**, trava o terminal e imprime os logs em tempo real no terminal
  ```docker logs -f nginx_app```
- para parar Crtl + c

### Removendo container

- Podemos **remover um container da máquina** que estamos executando o Docker;
- O comando é ```docker -rm <id>```;
- Se o container ainda estiver rodando, podemos utilizar a flag **-f** (force);
- ```docker -rm -f <id>```
- O container removido não é mais listado em ```docker ps -a```;

```
docker rm nginx_app
docker rm -f nginx_app
```
## Criando Imagens e avançando em containers

### O que é uma imagem?

- Imagens **são originadas de arquivos que programamos** para que o Docker crie uma estrutura que execute determinadas ações em containers;

- Elas contém informações como:
  - imagens base
  - diretório base
  - comandos a serem executados
  - porta da aplicação e etc

- Ao rodar um container baseado na imagem, **as instruções serão executadas em camadas**;

### Como escolher uma boa imagem

- Podemos fazer o download das imagens em: [hub docker](https://hub.docker.com);
- Porém **qualquer um pode fazer upload de uma imagem**, isso é um problema:
- Devemos então nos atentar as **imagens oficiais**;
- Outro parâmetro interessante é a **quantidade de downloads** e a **quantidade de stars**;
- [apache](https://hub.docker.com/_/httpd)

### Criando uma imagem

- Para criar uma imagem vamos precisar de um arquivo **Dockerfile** em uma pasta que ficará o projeto
- Este arquivo vai precisar de algumas instruções para poder ser executado:

- **FROM**: imagem base;
- **WORKDIR**: diretório da aplicação;
- **EXPOSE**: porta da aplicação;
- **COPY**: quais arquivos precisam ser copiados;

  1 - criamos uma pasta e pelo terminal digitamos: ```npm init -y```, vai iniciar um projeto de node e um package.json, onde instalaremos nossas dependências
  
  2 - caso não tenha instalado o npm: ```sudo apt install nodejs``` e ```sudo apt install npm```
  
  3 - ```npm install express```  framework para acessar essa aplicação no nosso navegador
  
  4 - criamos o ```app.js```, arquivo principal da nossa aplicação

  5 - ![app.js](./1_imagens_e_containers/app.js)==
  
  ```
  const express = require('express')
  const app = express()
  const port = 3000

  app.get('/', (req, res) => {
    res.send('Olá Minha Imagem')
  });

  app.listen(port, () => {
    console.log(`Executando na porta: ${port}`)
  });
  ```
6 - ```node app.js``` irá rodar o script, se já estiver um container rodando na porta 3000 irá gerar um erro ao tentar utilizar.

7 - criar arquivo Dockerfile ( nosso arquivo da imagem )

8 - ![Dockerfile](./1_imagens_e_containers/Dockerfile)
```
FROM node
# puxar uma imagem de base para aplicação: node

WORKDIR /app
# diretório que vai ser utilizado para executar a aplicação

COPY package*.json .
# copiaremos tudo do package.json e package-lock.json

RUN npm install /app
# ele vai instalar o projeto com express no container do docker

# utilizar . ou /app terá a mesma função pois o workdir já abre o arquivo app.js do diretório

COPY . .
# essa expresão significa: copia tudo que eu tenho aqui para o meu container
# copia o app.js para o /app

EXPOSE 3000
# porta 3000 exposta, igual a do const no app.js

CMD ["node", "app.js"]
# comando para executar a aplicação, só aceita parâmetros em listas []
```
  
- cada linha desse código é uma camada e ele vai criar um cache em cada um, se alterarmos o valor da porta ele vai executar a partir do EXPOSE, pois foi onde teve a alteração

- Devemos criar o arquivo ```.gitignore``` e dentro dele colocar : 
```node_modules/*```

- só assim conseguiremos subir nosso código para o github.

### Rodando nossa imagem em um container

- Para executar a imagem primeiramente **vamos precisar fazer o build**;
- O comando é ```docker build <diretório da imagem>```;
- ou ```docker build .``` se o terminal estiver na pasta do dockerfile
- Depois vamos utilizar o ```docker run <imagem>``` para executá-la;

- no terminal, entramos na pasta e digitamos: ```docker build .```
- ele criou o cache para cada comando
- para verificar as imagens, utilizamos ```docker image ls```
- utilizamos ```docker run 1a07c5705f42``` no Id da imagem criada
- ele não vai funcionar pois não conseguiu expor a imagem
- damos um ```docker stop 1a07```
- e agora utilizamos o comando completo ```docker run -d -p 3000:3000 1a07c5705f42```
- agora especificando a porta no comando run ele vai estar exposto
- agora rodando o mesmo comando e colocando um nome
- ```docker run -d -p 3000:3000 --name meu_node 1a07c5705f42```

### Alterando uma imagem

- Sempre que alteramos o código de uma imagem **vamos precisar fazer o build novamente**;
- Para o docker é como se fosse **uma imagem completamente nova**;
- Após fazer o build vamos executá-la por o outro id único criada com o docker run;

__Exemplificando:__

- Por exemplo alteramos a mensagem no app.js para: 'Olá Minha Imagem!'
- Precisamos parar essa imagem e fazer um build com essa alteração para poder surtir efeito
- futuramente vamos aprender a fazer o código da aplicação ser atualizado sem precisar fazer o build

- alteramos a porta no app.js para 3001
- agora teremos que fazer a build assim, utilizando um novo nome de versão: 
- ```docker build .```
- ```docker run -d -p 3001:3001 --name meu_node2 1a07c5705f42```

### Cache de camadas

- As imagens do Docker são divididas em **camadas** ( layers );
- Cada instrução no Dockerfile **representa um layer**;
- Quando algo é atualizado **apenas as layers depois da linha atualizada são refeitas**;
- O resto permanece em cache, tornando o **build mais rápido**;

### Download de imagens

- Podemos **fazer o download de alguma imagem** do hub e deixá-la disponível em nosso ambiente;
- Vamos utilizar o comando ```docker pull <imagem>```;
- Desta maneira, caso se use em outro container, **a imagem já estará pronta para ser utilizada**;

__Exemplificando:__

- Queremos baixar a imagem do python
- ```docker pull python```
- ```docker run -it python```
- agora podemos utilizar python no terminal atraves de uma imagem baixada pelo comando pull;
- ```docker images``` veremos a imagem do python

### Mais informações sobre os comandos

- Todo comando no docker tem acesso a uma **flag --help**;
- Utilizando desta maneira, **podemos ver todas as opções disponíveis nos comandos**;
- Para relembrar algo ou executar uma tarefa diferente com o mesmo;
- Ex: ```docker run --help```

### Múltiplas aplicações do mesmo container

- Podemos inicializar **vários containers com a mesma imagem**;
- As aplicações funcionarão em paralelo;
- Para testar isso, podemos determinar uma **porta diferente** para cada um, e rodar no **modo detached**;

__Exemplificando:__

- ```docker run -d -p 3000:3000 --name meu_node6 1a07c5705f42```
- ```docker run -d -p 4000:3000 --name meu_node7 1a07c5705f42```
- Temos 2 projetos rodando em background simultâneamente em portas diferentes e utilizando a mesma imagem com os nomes diferentes

### Nomeando Imagens

- Podemos **nomear imagem** que criamos;
- vamos utilizar o comando ```docker tag <id> <novonome>``` para isso;
- Também podemos **modificar a tag**, que seria como uma versão da imagem, semelhante ao git
- Para inserir a tag utilizamos: ```docker tag <id ou nome>:<tag>```

- __agora a imagem 1a07c5705f42 terá o nome minha_imagem__
```docker tag 1a07c5705f42 minha_imagem```

- __agora a imagem 1a07c5705f42 terá o nome minha_imagem e a tag minhatag__
```docker tag 1a07c5705f42 minha_imagem:minhatag```

- podemos utilizar pull para baixar a minha_imagem com a tag que seria uma nova versão
```docker pull minha_imagem```
```docker pull minha_imagem:minhatag```

### Nomeando imagem no build

- Podemos **nomear a imagem já na sua criação**;
- Vamos utilizar a **flag -t**;
- É possível inserir o nome e a tag, na sintaxe: **nome:tag**
- Isso torna o processo de nomeação mais simples;

- vai fazer o build . e criar a imagem com o nome meunode_diferente 
```docker build -t meunode_diferente .```

- vai fazer o build . e criar a imagem com o nome meunode_diferente e a 
  tag minhatag_diferente
```docker build -t meunode_diferente:minhatag_diferente .```

### Reiniciando Container com iteratividade ( start interativo )

- A **flag -it** pode ser utilizada com o comando start também;
- Ou seja, não precisamos criar um novo container para utilizá-lo no terminal;
- O comando é: ```docker start -it <container>```

- ao utilizar : ```docker start -it meunode_diferente```
saída: Executando na porta: 3000

### Removendo imagens

- Assim como nos containers, **podemos remover imagens com um comando**;
- Ele é o: ```docker rmi <imagem>```
- Imagens que estão sendo utilizadas por um container, apresentarão um erro no terminal;
- Podemos utilizar a **flag -f** para forçar a remoção;

- remove uma imagem em execução de nome minha_imagem e tag minhatag
```docker rmi -f minha_imagem:minhatag```

### Removendo imagens e containers não utilizados

- Com o comando ```docker system prune```;
- Podemos **remover imagens, containers e networks** não utilizados;
- O sistema irá exigir uma confirmação para realizar a remoção;
- Resta apenas as imagens que estão sendo utilizadas;

### Removendo container após utilização

- Um container pode ser automaticamente deletado após sua utilização;
- Quando o comando é utilizado ele não aparece na lista ```docker ps -a```
- Para isso vamos utilizar a **flag --rm**;
- O comando seria: ```docker run --rm <container>```
- Desta maneira **economizamos espaço no computador** e deixamos o ambiente mais organizado;

- Criou um container 1a07c5705f42 temporário com nome node_diferente 
```docker run -d -p 3000:3000 --name node_diferente --rm 1a07c5705f42```

- Ao utilizar o stop, o container é removido
```docker stop 1a07``` 

### Copiando arquivos entre containers

- Para cópia de arquivos entre containers utilizamos o comando: ```docker cp```;
- Pode ser utilizado para copiar um arquivo de um diretório para um container;
- Ou de um container para um diretório determinado;

```docker run -d -p 3000:3000 --name node_diferente2 node```

- especificar o container __node_diferente__ e indicar qual arquivo será copiado __:app/app.js__ e onde será copiado __./copia/__
```docker cp node_diferente2:app/app.js ./copia/```

- copiamos um arquivo de um container rodando para nosso computador

### Verificando informações de processamento de container

- Ideal para quando for entrar em uma nvoa empresa, verificar oq está sendo executado
- Para verificar dados de execução de um container utilizamos: 
  ```docker top <container>```
- Desta maneira temos acesso a quando ele foi iniciado, id do processo, descrição do comando CMD;
- ```docker top meu_node```

### Inspecionar dados do container

- Para verificar diversas informações como: **id, data de ciação, imagem e muito mais**;
- Utilizamos o comando ```docker inspect <container>```
- Desta maneira conseguimos entender como o container está configurado;

### Verificando processamento do docker

- Usado para verificar containers em execução
- Para verificar os processos que estão sendo executados em um container, utilizamos o comando: ```docker stats```
- Desta maneira temos acesso ao andamento do processamento e memória gasta pelo mesmo;

### Autenticação no terminal

- Autenticação no docker hub;
- Para autenticar-se pelo terminal vamos utilizar o comando ```docker login```;
- E então inserir usuário e senha;
- Agora podemos **enviar nossas própias imagens** para o HUB!

### Encerrando autenticação

- Para remover a conexão entre nossa máquina e o Docker Hub, vamos utilizar o comando ```docker logout```;
- Agora não podemos mais enviar imagens, pois não estamos autenticados;

### Enviando imagens para o Docker Hub

- Usuário free tem direito a uma imagem privada;
- Para enviar uma imagem nossa ao Docker Hub utilizamos o comando ```docker push <imagem>```;
- Também será necessário estar **autenticado**;

__Exemplificando:__

1. 
- Navegar até repositórios no docker hub e criar repositório.
- lucasbergamo/nodeteste

2. 
- Agora no terminal vamos até o diretório do build e com o usuário do dockerhub na frente do repositório:
  ```docker build -t lucasbergamo/nodeteste .```

1. 
- Enviando imagem para ficar disponível para download no HUB:
  ```docker push lucasbergamo/nodeteste```

1. 
- Ou com tag name, para identificar a versão:
  ```docker push lucasbergamo/nodeteste:tagname```

5. 
- Podemos apagar para testar
  ```docker rmi lucasbergamo/nodeteste```

1. 
- e para fazer o download em qualquer maquina:
  ```docker pull lucasbergamo/nodeteste```
- ou com tag name
  ```docker pull lucasbergamo/nodeteste:tagname```

### Atualizando imagens no Hub

- Para enviar uma atualização **vamos primeiramente fazer o build**;
- **Trocamos a tag da imagem** para a versão atualizada;
- **Depois vamos fazer um push** novamente para o repositório;
- Assim todas as versões estarão disponíveis para serem utilizadas;

__Exemplificando:__

1. 
- Podemos acessar Dockerfile e mudar o __WORKDIR__ para __/src__
  ```docker build -t lucasbergamo/nodeteste:nova_versao .```

2. 
- Agora por exemplo, quero disponibilizar essa nova versão para minha equipe:
  ```docker push lucasbergamo/nodeteste:nova_versao```

### Baixando e utilizando nossa imagem

- Para baixar a imagem podemos utilizar o comando ```docker pull <imagem>:tag```
- E depois criar um novo container com ```docker run <imagem>```
- E pronto! Estaremos utilizando a nossa imagem com um container;

__Exemplificando:__

- Removi a imagem da minha máquina:
  ```docker rmi lucasbergamo/nodeteste:nova_versao```
- Para verificar:
  ```docker images```

- Não precisamos estar logados para baixar, podemos testar:
  ```docker logout```
  ```docker pull lucasbergamo/nodeteste:nova_versao```

- Agora vamos rodar a imagem:
```docker run --name testando_imagem -p 3000:3000 -d lucasbergamo/nodeteste:nova_versao```

__Exemplificando:__ 

- vai rodar um container com o nome testando_imagem, cria uma instância de um contêiner a partir de uma imagem.

- na porta 3000:3000, Isso significa que qualquer tráfego enviado para a porta 3000 do host será redirecionado para a porta 3000 do contêiner.

- executando o -d para ficar rodando em backgroud 

- lucasbergamo/nodeteste:nova_versao: Esse é o nome da imagem que será usada para criar o contêiner. Ele segue a convenção "nome_do_usuário/nome_do_repositório:tag". 

## Introduzindo volumes aos nossos containers

### O que são Volumes?

- Uma **forma prática de persistir dados** em aplicações e não depender de containers para isso;
- **Todo dado criado por um container é salvo nele**, quando o container é removido perdemos os dados;
- Então precisamos dos volumes para gerenciar os dados e também conseguir **fazer backups** de forma mais simples;
- Volume auxilia a guardar dados em uma pasta ou local e compartilhar entre containers e reutilizar em aplicações;

### Tipos de volumes

- **Anônimos (anonymous)**: Diretórios criados pela **flag -v**, porém com um nome aleatório;
- **Nomeados (named)**: São volumes com nomes, podemos nos referir a estes facilmente e saber para que são utilizados no nosso ambiente;
- **Bind mounts**: Uma forma de salvar dados na nossa máquina, sem o gerenciamento do Docker, informamos um diretório para este fim;

### Criando o projeto para trabalhar com volumes

- Se criarmos um container com alguma imagem, **todos os arquivos que geramos dentro dele serão do container**;
- Quando o container for removido, perderemos estes arquivos;
- Por isso precisamos dos **volumes**;
- Vamos criar um exemplo prático: mini aplicação com php para salvar arquivos no volume

1 - criar docker file com php - apache
2 - criar index.php com input
3 - criar o script process.php
4 - criamos a pasta messages para armazenar as messagens vindas do script process
5 - no diretório 2_volumes
6 - ```docker build -t phpmessages .```
7 - ```docker run -d -p 80:80 --name phpmessages_container phpmessages```
8 - abrir localhost:80
9 - digitar uma mensagem e submeter
10 - agora para verificar a mensagem, vamos digitar: localhost/messages/msg-0.txt

- criamos um projeto que salva dados no container

### O problema da persistência de dados

- Se utilizarmos o ```docker stop phpmessages_container```
- e depois um ```docker start phpmessages_container```
- os dados continuam salvos, porém se removermos : 
  ```docker rm phpmessages_container```
- e depois rodar um novo container : 
  ```docker run -d -p 80:80 --name phpmessages_container --rm phpmessages```
- quando vamos acessar os dados de mensagems no localhost, aparece um erro not found, **esse é o problema da persitência que vamos resolver com volumes**;

### Volumes Anônimos

- Podemos criar um volume anônimo (**anonymous**) da seguinte maneira:
  ```docker run -v /data```
- Onde **/data** será o diretório que contém o volume anônimo;
- E este container estará atrelado ao volume anônimo;
- Com o comando ```docker volume ls```, podemos ver todos os volumes do nosso ambiente;

__Exemplificando:__

- ```docker run -d -p 80:80 --name phpmessages_container --rm -v /data phpmessages```
- agora vamos abrir o localhost:80 e colocar uma nova mensagem
- ```docker volume ls``` vamos ter um volume com um nome aleatório que caracteriza um volume anônimo
- e como saber se estamos salvando dados nesse volume anônimo?
- ```docker inspect phpmessages_container```

```"Volumes": {"/data": {}}```
- isso indica que o volume foi criado

### Volumes Nomeados

- Podemos criar um volume nomeado (**named**) da seguinte maneira:
  ```docker run -v nomedovolume:/data```
- Agora o volume tem um nome e pode ser facilmente referenciado;
- Em ```docker volume ls``` podemos verificar o container nomeado criado;
- Da mesma maneira que o anônimo, este volume tem como função armazenar arquivos;

__Exemplificando:__

- criando container com volume nomeado 
  ```docker run -d -p 80:80 --name phpmessages_container -v phpvolume:/var/www/html/messages --rm phpmessages```

- e onde está a diferença entre o anonymous?
  ```docker stop phpmessages_container```

- rodamos o mesmo container e a imagem persiste
  ```docker run -d -p 80:80 --name phpmessages_container -v phpvolume:/var/www/html/messages --rm phpmessages```

- rodamos outro container com a porta 81 e nome diferente
  ```docker run -d -p 81:80 --name phpmessages_container2 -v phpvolume:/var/www/html/messages --rm phpmessages```

- a mensagem salva da porta 80, aparece na porta 81.
- comunicação entre containers
- duas aplicações distintas acessando o mesmo volume, persistindo dados

### Bind mounts

- **Bind mount** também é um volume, porém ele fica em um diretório que nós especificamos(no host);
- Então não criamos um volume e sim, **apontamos um diretório**;
- O comando para criar um bind mount é: ```docker run /dir/data:data```
- ```/dir/data``` é o diretório onde vai ser salvo as mensagens no nosso pc
- ```:data``` e esse é o diretório onde estamos recebendo as mensagens do container
- Desta maneira o diretório **/dir/data** no nosso computador, será o volume deste container;

__Exemplificando:__

- vamos reutilizar o run e colocar o diretório atual (pasta messages)
- clicar com o botão direito na pasta message e **copiar o caminho**
  ```docker run -d -p 80:80 --name phpmessages_container -v C:\Users\Lucas\Documents\Compass_UOL_data_engineering\Sprint-4\docker_e_kubernetes\2_volumes\messages:/var/www/html/messages --rm phpmessages```

- ao rodar no wsl gera um erro, devemos utilizar o terminal padrão do windows

### O poder extra do Bind mount

- **Bind mount** não serve apenas para volumes!
- Podemos utilizar esta técnica para **atualização em tempo real do projeto**;
- Sem ter que refazer o build a cada atualização do mesmo;

__Exemplificando:__

- vamos copiar o diretório pai do projeto, no caso a pasta 2_Volumes
- e mudamos o diretorio para o workdir ao inves do /messages 
  ```docker run -d -p 80:80 --name phpmessages_container -v C:\Users\Lucas\Documents\Compass_UOL_data_engineering\Sprint-4\docker_e_kubernetes\2_volumes\:/var/www/html/ --rm phpmessages```
- ao inserir uma mensagem, ele continua salvando na pasta messages
- agora se eu alterar o html, ele muda em tempo real na aplicação, sem precisar buildar a imagem novamente

### Criando volumes manualmente

- Podemos criar volumes manualmente também;
- Utilizamos o comando: ```docker volume create <nome>```
- Desta maneira temos um **named volume** criado, podemos atrelar a algum container na execução do mesmo

__Exemplificando:__

- ```docker volume ls```
- ```docker volume create volumeteste```

- ao invés de criar o volume ele vai reaproveitar o volume
  ```docker run -d -p 80:80 --name phpmessages_container -v volumeteste:/var/www/html/ --rm phpmessages```

### Listando volumes

- Com o comando: ```docker volume ls``` listamos todos os volumes, sendo utilizados ou não
- Desta maneira temos acesso aos **anonymous e os named volumes**;
- Interessante para saber quais volumes estão criados no nosso ambiente;

### Inspecionando volumes

- Podemos verificar os detalhes de um volume em específico com o comando: 
  ```docker volume inspect <nome>```
- Desta forma temos acesso ao **local em que o volume guarda dados**, nome, escopo e muito mais;
- O docker salva os dados dos volumes em algum diretório do nosso computador, desta forma podemos saber qual é;

__Exemplificando:__

- ```docker volume inspect phpvolumes```
- retorna:

"CreatedAt": "2023-08-01T02:40:06Z",
"Driver": "local",
"Labels": null,
"Mountpoint": "/var/lib/docker/volumes/phpvolume/_data",
"Name": "phpvolume",
"Options": null,
"Scope": "local"

- "Mountpoint" é onde fica savo os arquivos, é fácil achar no linux porém no windows precisa procurar onde o docker foi instalado

### Removendo volumes

- Podemos também remover um volume existente de forma fácil;
- Vamos utilizar o comando ```docker volume rm <nome>```
- Observe que **os dados serão removidos todos também**, tome cuidado com este comando;

__Exemplificando:__

- ```docker volume rm volumeteste```
- ```docker volume rm phpvolume```
- ```docker volume rm 9cffd107d61fef51ac5cb9179fe497dfee4592c5307d4be7fa543e7216c319fd```

### Remoção de volumes em massa

- Podemos **remover todos os volumes que não estão sendo utilizados** com apenas um comando
- O comando é: ```docker volume prune```
- Semelhante ao prune que remove imagens e containers, visto anteriormente;

__Exemplificando:__

- iremos criar alguns volumes para apagar em massa
- ```docker volume create vol1```
- ```docker volume create vol2```
- ```docker volume create vol3```
- ```docker volume create vol4```
- ```docker volume create vol5```
- ```docker volume ls```
- ```docker volume prune```

==complemento a aula== : 

- Se você criou volumes personalizados usando o comando ```docker volume create``` ou montou volumes manualmente ao iniciar contêineres, esses volumes também não serão removidos pelo ```docker volume prune```, mesmo que não estejam associados a nenhum contêiner. O comando ```docker volume prune``` é projetado para remover apenas os volumes "dangling".

- O uso da opção **--force** pode garantir que qualquer cache de volumes seja limpo antes de listar os volumes novamente
  ```docker volume prune --force```

- mesmo assim não conseguir apagar todos, tive de apagar de um por um utilizando o comando ```docker volume rm vol1```

### Volume somente leitura

- Podemos criar um volume que tem **apenas permissão de leitura**, isso é útil em algumas aplicações;
- Para realizar esta configuração devemos utilizar o comando 
  ```docker run -v volume:/data:ro```
- Este **:ro** é a abreviação de read only;

__Exemplificando:__

- vamos criar um volume de leitura:
  ```docker run -d -p 80:80 --name phpmessages_container -v volumeleitura:/var/www/html:ro --rm phpmessages```

- ao abrir o local host: 

Warning: fopen(./messages/msg-0.txt): Failed to open stream: Read-only file system in /var/www/html/process.php on line 11

Fatal error: Uncaught TypeError: fwrite(): Argument #1 ($stream) must be of type resource, bool given in /var/www/html/process.php:14 Stack trace: #0 /var/www/html/process.php(14): fwrite(false, 'asda') #1 {main} thrown in /var/www/html/process.php on line 14

## Conectando containers com networks

### O que são networks?

- **Uma forma de gerenciar a conexão do Docker** com outras plataformas ou até mesmo entre containers;
- As redes ou networks são **criadas separadas do containers**, como os volumes;
- Além disso existem alguns **drivers de rede**, que veremos em seguida;
- Uma rede deixa muito simples a comunicação entre containers;
- Teoricamente criamos uma rede para os containers utilizarem, o modo bridge é o mais utilizado

### Tipos de conexão

- Os containers costumam ter três principais tipos de comunicação;
- **Externa:** conexão com uma API de um servidor remoto;
- **Com o host:** comunicação com a máquina que está executando o Docker;
- **Entre containers:** comunicação que utiliza o driver bridge e permite a comunicação entre dois ou mais containers;

### Tipos de rede (Drivers)

- **Bridge:** o mais comum e default do Docker, utilizado quando containers precisam se conectar (na maioria das vezes optamos por este driver);
- **Host:** permite a conexão entre um container a máquina que está hosteando o Docker
- **Macvlan:** permite a conexão a um container por um MAC address;
- **None:** remove todas conexões de rede de um container;
- **Plugins:** permite extensões de terceiros para criar outras redes;

### Listando Networks (redes)

- Podemos verificar todas as redes do nosso ambiente com : ```docker network ls```
- **Algumas redes já estão criadas**, estas fazem parte da configuração inicial do docker

### Criando redes

- Para criar uma rede vamos utilizar o comando ```docker network create <nome>```
- Esta rede será do tipo **bridge**, que é o mais utilizado;
- Podemos criar diversas redes; 
```docker network create minharedeteste```
- utilizamos a **flag -d** para especificar um driver (host, macvlan, none, plugins)
- criando uma rede com um driver específico:
  ```docker network create -d macvlan meumacvlan```

### Removendo redes

- Podemos remover redes de forma simples também: ```docker network rm <nome>```
- Assim **a rede não estará mais disponível** para utilizarmos;
- Devemos tomar cuidado com containers já conectados;
  ```docker network rm meumacvlan```
  ```docker network rm minharedeteste```

### Removendo redes não utilizadas

- Podemos remover redes de forma simples também: ```docker network prune```
- Assim **todas as redes não utilizadas** no momento serão removidas;
- Todas as redes padrão do docker só podem ser removidas manualmente com o rm;
- Receberemos uma mensagem de confirmação do docker antes da ação ser executada
- Tomar cuidado, se utilizarmos o comando rm no container podemos apagar a rede junto

### Instalando o Postman

- Vamos criar uma **API** para testar a conexão entre containers;
- Para isso vamos utilizar o software **Postman**, que é o mais utilizado do mercado para desenvolvimentos de APIs;
- [Link](https://www.postman.com/downloads)
- Fazer o download e instalar normalmente

### Conexão Externa

- Os containers **podem se conectar livremente ao mundo externo**;
- Um caso seria: uma API de código aberto;
- Podemos acessá-la livremente e utilizar seus dados;
- Vamos testar!

__Exemplificando:__

Criando o Dockerfile
- [Dockerfile](./3_networks/1_externa/Dockerfile)

- Depois criando o app.py

- agora vamos buildar a imagem:
  ```docker build -t flaskexterna .```

- agora vamos rodar um container baseado na imagem:
  ```docker run -d -p 5000:5000 --name flaskexternocontainer --rm flaskexterna```

- abrir o postman:
  - New / http
  - GET / http://localhost:5000/
  - SEND

- Criamos uma API de Flask baseada em um container de docker que conecta com o mundo externo com sucesso

### Conexão com máquina host

- Podemos também **conectar um container com o host do Docker**;
- **Host** é a máquina que está executando o Docker;
- Como ip de host utilizamos: **host.docker.internal**
- No caso pode ser a nossa mesmo!

__Exemplificando:__

- precisamos de mysql instalado no pc para ver funcionando
- agora vamos criar um docker file e app.py
- vamos até a nova pasta e
- ```docker build -t flaskhost```

- agora vamos até o sql e criamos um banco de dados
- name = flaskhost
- e criamos uma tabela de user com: id(INT(11)), name(VARCHAR(255))

- agora vamos rodar um container baseado na imagem:
  ```docker run -d -p 5000:5000 --name flaskhostcontainer --rm flaskhost```

- abrir o postman:
  - New / http
  - GET / http://localhost:5000/
  - SEND

- new / http
- POST / http://localhost:5000/inserthost
- SEND

### Conexão entre containers

- No exemplo acima os dados foram salvos no computador, agora será salvo no container
- Podemos estabelecer uma **conexão entre containers**;
- Duas imagens distintas rodando em **containers separados que precisam se conectar para inserir um dado no banco**, por exemplo;
- Vamos precisar de uma rede **bridge**, para fazer esta conexão;
- Agora nosso container de flask vai inserir dados em um MySQL que roda pelo Docker também

__Exemplificando:__

- Criamos um diretório mysql com um schema e um dockerfile
- navegamos até a pasta 3_conexoes_entre_containers/mysql
- ```docker build -t mysqlnetworkapi .```
- ```docker network create flasknetwork```
- ```docker run -d -p 3306:3306 --name mysql_api_container --rm --network flasknetwork -e MYSQL_ALLOW_EMPTY_PASSWORD=True mysqlnetworkapi```
- agora temos mysql rodando dentro do container de docker
- agora vamos no arquivo app.py dentro do diretório flask
- colocamos para o mysql se conectar ao container ao inves do host
  ```app.config['MYSQL_HOST'] = 'mysql_api_container'```
- depois de alterar vamos precisar fazer o build dessa imagem novamente
- ```docker build -t flaskapinetwork .```
- precisamos externalizar esse container pois vamos acessar via postman
- ```docker run -d -p 5000:5000 --name flask_api_container --rm --network flasknetwork flaskapinetwork```
- vamos abrir o postman e testar a rota de GET http://localhost:5000/
- adicionamos outra  aba: POST http://localhost:5000/inserthost

### Conexão entre containers

- Podemos conectar um container a uma rede;
- Vamos utilizar o comando ```docker network connect <rede> <container>```
- Após o comando o container estará dentro da rede!

__Exemplificando:__

- ```docker network connect flasknetwork d50423d1926c```
- ao utilizar o inspect no container, veremos que ele foi conectado a rede
  ```docker inspect d50423d1926c```

### Desconectando um container

- Podemos desconectar um container a uma rede também;
- Vamos utilizar o comando ```docker network disconnect <rede> <container>```
- Após o comando o container estará fora da rede!

__Exemplificando:__

- ```docker network disconnect flasknetwork d50423d1926c```
- ao utilizar o inspect no container, veremos que ele foi desconectado a rede
  ```docker inspect d50423d1926c```

### Inspecionando redes

- Podemos analisar os detalhes de uma rede com o comando: 
  ```docker network inspect <nome>```
- Vamos receber informações como: data de criação, driver, nome e muito mais!
- ao entrar em uma empresa podemos inspecionar a rede para conhecer a rede.

__Exemplificando:__

- ```docker network inspect flasknetwork```

## Introdução ao YAML