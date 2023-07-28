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