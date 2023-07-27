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