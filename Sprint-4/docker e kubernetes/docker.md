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
  - [Onde encontrar imagens?](#onde-encontrar-imagens)
  - [Verificar containers executados](#verificar-containers-executados)
  - [Executar container com interação](#executar-container-com-interação)
  - [Container x VM ( Virtual Machine )](#container-x-vm--virtual-machine-)
  - [Executar container em background](#executar-container-em-background)
  - [Expondo portas de container](#expondo-portas-de-container)
  - [Parando containers](#parando-containers)
  - [Reiniciando Containers](#reiniciando-containers)
  - [Definindo nome do container](#definindo-nome-do-container)
  - [Acessando os logs de um container](#acessando-os-logs-de-um-container)
  - [Removendo containers](#removendo-containers)
- [Criando Imagens e avançando em containers](#criando-imagens-e-avançando-em-containers)
  - [O que é uma imagem?](#o-que-é-uma-imagem)
  - [Como escolher uma boa imagem](#como-escolher-uma-boa-imagem)
  - [Criando uma imagem](#criando-uma-imagem)

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

- [WSL2](https://learn.microsoft.com/pt-br/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
  - O Docker exige o Wsl 2 no windows

após instalar o docker -> reiniciar -> instalar o wsl -> abrir o docker;

usar esses comandos no cmd para verificar se está funcionando:
  - docker ps
  - docker version

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
- Para rodar containers utilizamos o comando **docker run**;
- Neste comando **podemos passar diversos parâmetros**;
- Neste exemplo vamos passar apenas o nome da imagem que é **docker/whalesay**
- Um comando chamado **cowsay** e uma mensagem

Abrir o terminal:
  - verificar se as instancias estao sendo executadas
  - ```wsl.exe -l -v```
  - docker run docker/whalesay cowsay Hello_World


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


### Onde encontrar imagens?

- Vamos encontrar imagens no repositório do [Docker](https://hub.docker.com)
- Nesse site podemos verificar quais as imagens existem da tecnologia que estamos procurando, por exemplo: Node.js, Ubuntu;
- E também **aprender a como utilizá-las**;
- Vamos executar uma imagem em um container com o comando: ```docker run <imagem>```

Passo a passo:
- ```docker run ubuntu``` ( cria e interrompe a imagem, não acontece nada pois não foi dito oq era pra ser feito )
- ```docker run -it ubuntu``` ( criou e continua rodando a imagem)
- agora temos acesso ao terminal da nova imagem instalada do ubuntu
- podemos utilizar o ```docker ps``` para checar o status

### Verificar containers executados

- O comando ```docker ps``` ou ```docker container ls``` exibe quais containers estão sendo executados no momento;
- Utilizando a flag **-a**, temos também todos os containers ja executados na máquina;
- Este comando é útil para **entender o que está sendo executado e acontece** no nosso ambiente;
- Exemplo : ```docker ps -a``` ```docker container ls -a```

### Executar container com interação

- Podemos rodar um container e deixá-lo **executando no terminal**;
- Vamos utilizar a ```flag -it```;
- Desta maneira podemos executar comandos disponíveis no container que estamos utilizando o comando run;
- Podemos utilizar a imagem do ubuntu para isso!
- ```docker run -it node``` vai criar e baixar uma imagem do node js
- para sair : **Ctrl c + Ctrl c**

### Container x VM ( Virtual Machine )

- **Container é uma aplicação que serve para um determinado fim**, não possui sistema operacional, seu tamanho é de alguns mbs;
- VM possui sistema operacional próprio, tamanho de gbs, **pode executar diversas funções ao mesmo tempo**
- Containers acabam gastando menos recursos para serem executados, por causa do seu uso específico
- VMs gastam mais recursos, porém podem exercer mais funções;


### Executar container em background

- Quando iniciamos um container que persiste, **ele fica ocupando o terminal**;
- Podemos executar um container em background, para não precisar ficar com diversas abas de termminal aberto, utilizamos a **flag -d**(detached);
- Verificamos **containers em background com docker ps** também;
- Podemos utilizar o nginx( servidor web, identico ao apache ) para este exemplo!
- Inicia um container em background: ```docker run -d nginx```
- parando um container utilizando o dado em NAMES```docker stop charming_fermi```

### Expondo portas de container

- porta 80 é a porta padrão do acesso web.
- Os **containers de docker não tem conexão com nada de fora deles;
- Por isso precisamos expor portas, a flag é a **-p** e podemos fazer assim:
  - -p80:80;
- Desta maneira **o container estará acessível na porta 80**;
- Podemos testar este exemplo com o nginx !


O primeiro número é a porta que está expondo o pc e a segunda é a do container
  - pc:container

```docker run -d -p 80:80 nginx``` [](localhost:80/)
```docker run -d -p 3000:80 nginx``` [](localhost:3000/)


### Parando containers

- Podemos para um container com o comando ```docker stop <id ou nome>```;
- Desta maneira estaremos liberando recursos que estão sendo gastos pelo mesmo:
- Podemos verificar os containers rodando com o comando ```docker ps```;
- ```docker stop afb6e877c259```

### Reiniciando Containers

- Aprendemos já a parar um container com o stop, para voltar a rodar um container usar o comando ```docker start <id>```;
- Lembre-se que **o run sempre cria um novo container**;
- Então caso seja necessário aproveitar um antigo, opte pelo start;
- podemos selecionar o conteiner com os 4 primeiros caracteres do ID```docker stop afb6```

### Definindo nome do container

- Podemos definir um nome do container com a flag **--name**;
- Se não colocarmos, **recebemos um nome aleatório**, o que pode ser um problema para uma aplicação profissional;
- A flag run é inserida junto do **comando run**;


1- novo nome
2- imagem nginx
- ```docker run -d -p 80:80 --name nginx_app nginx```
- ```docker stop nginx_app```

### Acessando os logs de um container

- Podemos **verificar o que aconteceu em um container** com o comando logs;
- Utilizamos da seguinte maneira: **docker logs <id>**
- As últimas ações realizadas no container, serão **exibidas no terminal**;
- flag **-f**, atualiza e imprime os logs no terminal```docker logs -f nginx_app```
- para parar Crtl + c

### Removendo containers

- Podemos **remover um container da máquina** que estamos executando o Docker;
- O comando é **docker -rm <id>**;
- Se o container ainda estiver rodando, podemos utilizar a flag **-f** (force);
- O container removido não é mais listado em ```docker ps -a```;
```
docker rm nginx_app
docker rm -f nginx_app
```

## Criando Imagens e avançando em containers

### O que é uma imagem?

- Imagens **são originadas de arquivos que programamos** para que o Docker crie uma estrutura que execute determiandas ações em containers;

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
- Este arquivovai precisar de algumas instruções para poder ser executado;
- **FROM**: imagem base;
- **WORKDIR**: diretório da aplicação;
- **EXPOSE**: porta da aplicação;
- **COPY**: quais arquivos precisam ser copiados;

  1 - criamos uma pasta e pelo terminal digitamos: ```npm init -y```, vai criar um projeto de node e um package.json, onde instalaremos nossas dependências
  
  2 - caso não tenha instalado o npm: ```sudo apt install nodejs``` e ```sudo apt install npm```
  
  3 - ```npm install express```  framework para acessa essa aplicação no nosso navegador
  
  4 - criamos o ```mkdir app.js```, arquivo principal da nossa aplicação

  5 - 
  ```
  const express = require('express)
  const app = express()
  const port = 3000

  app.get('/', (req, res) => {
    res.send('Olá Minha Imagem')
  })

  app.listen(port, () => {
    console.log(`Executando na porta: ${port}`)
  })
  ```
6 - ```node app.js``` irá rodar o script, se já estiver um container na porta 3000 irá gerar um erro ao tentar utilizar.

7 - criar arquivo Dockerfile

8 - 
```
FROM node

WORKDIR /app

COPY package*.json .

RUN npm install /app
# utilizar . ou /app terá a mesma função pois o workdir já abre o arquivo app.js do diretório

COPY . .
# essa expresão significa: copia tudo que eu tenho aqui para o meu container

EXPOSE 3000

CMD ["node", "app.js"]
#comando para executar a aplicação, só funciona em listas []
```

- Devemos criar o arquivo ```.gitignore``` e dentro dele colocar : 
```node_modules/*```
