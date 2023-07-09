# Sumário

<details><summary><strong>Navegação</strong></summary>

1. [Instalação e Introdução Git](#instalação)
2. [Git Comandos Fundamentais](#git-comandos-fundamentais)
3. [Trabalhando com Branchs, Stash, Tags](#trabalhando-com-branchs-stash-tags)
4. [Compartilhamento e atualizações de repositórios](#compartilhamento-e-atualizações-de-repositórios)
5. [Análise e inspeção de repositórios](#análise-e-inspeção-de-repositórios)
6. [Administração de repositórios](#administração-de-repositórios)
7. [Melhorando os commits do projeto](#melhorando-os-commits-do-projeto)
8. [Explorando e entendendo o GitHub](#explorando-e-entendendo-o-github)
9. [Markdown do básico ao avançado](#markdown-do-básico-ao-avançado)
10. [Projeto: Portifólio com Github Pages](#projeto-portifólio-com-github-pages)

</details>

## Instalação:

Git - Downloads;

Download Visual Studio Code - Mac, Linux, Windows;

### O que é controle de versão?

- Uma técnica que ajuda a gerenciar código-fonte de uma aplicação;
- Registrando todas as modificações de código, podendo também reverter as mesmas;
- Criar versões de um software em diferentes estágios, podendo alterar facilmente entre elas;
- Cada membro da equipe pode trabalhar em uma versão diferente;
- Há ferramentas para trabalhar o controle de versão como: git e SVN;

### O que é git?

- O sistema de controle de versão mais utilizado do mundo atualmente;
- O git é baseado em repositórios , que contém todas as versões do código e também as cópias de cada desenvolvedor;
- Todas as operações do git são otimizadas para ter alto desempenho;
- Todos os objetos do git são protegidos como criptografia para evitar alterações indevidas e maliciosas;
- O git é um projeto de código aberto;
- O github é um servidor que  armazena os repositórios de um  projeto;

### O que é Github?

- É um serviço para gerenciar repositórios, gratuito e amplamente utilizado;
- Podemos enviar nossos projetos para o github e disponibilizá-lo para outros devs;
- O github é gratuito tanto para projetos públicos como privados;
- Vamos criar uma conta em: https://github.com;

### Enviando repositórios para o Github

- Podemos facilmente enviar nossos repos para o Github;
- Precisamos criar o projeto no github, inicializar o mesmo no git em nossa máquina, sincronizar com o GH e enviar;
- E esta sequência que parece ser complexa é facilmente executada por poucos comandos;
- Vale lembrar que só fazemos uma vez por projeto, este fluxo;
- Porém alguns dos comandos utilizados vão ser úteis ao longo do curso;

----------

## Git Comandos Fundamentais:


### O que é um Repositório?

- É onde o código será armazenado;
- Na maioria das vezes cada projeto tem um repositório;
- Quando criamos um repositório estamos iniciando um projeto;
- O repositório pode ir para servidores que são especializados em gerenciar repos, como: Github e Bitbucket;
- Cada um dos desenvolvedores do time pode baixar o repositório e criar versões diferentes em sua máquina;


### Criando Repositórios

- Para criar um repositório utilizamos o comando: git init;
- Desta maneira o git vai criar os arquivos necessários para inicializá-lo;
- que estão na pasta oculta .git; ls -la;
- Após este comando o diretório atual será reconhecido pelo git como um projeto e responderá aos seus demais - comandos;

```
git init
git config –global user.name””
git config –global user.email””
git config –global defaultBranch main
git status
git add .
git commit -m “”
git remote add origin
git push -u origin main
```
### Verificando mudanças de projeto

- As mudanças de projeto podem ser verificadas por: git status;
- Este comando é utilizado muito frequentemente;
- Aqui serão mapeadas todas as alterações do projeto;
- como: arquivos não monitorados e arquivos modificados;
- podemos também dizer que é a diferença do que já está enviado ao servidor ou salvo no projeto;

### Adicionando arquivos ao projeto

- Para adicionar arquivos novos a um projeto utilizamos: git add;
- Podemos adicionar um arquivo específico como também diversos de uma vez só;
- Somente adicionando arquivos eles serão monitorados pelo git;
- Ou seja, se não adicionar ele não estará no controle de versão;
- É interessante usar esse comandos de tempos em tempos para não perder algo por descuido;

### Salvando alterações do projeto

- As alterações salvas do projeto são realizadas por: git commit;
- Podemos commitar arquivos específicos ou vários de uma vez com a flag -a;
- É uma boa prática enviar uma mensagem a cada commit, com as alterações que foram feitas;
- A mensagem pode ser adicionada com a flag -m;

### Enviando código ao repo remoto

- Quando finalizamos uma funcionalidade nova, enviamos o código ao repositório remoto, que é o código-fonte;
- Esta ação é feito pelo git push;
- Após esta ação o código do servidor será atualizado baseando-se nesse código local enviado;

### Recebendo as mudanças

- é comum também ter que sincronizar o local com as mudanças do remoto;
- Esta ação é feita pelo git pull;
- Após o comando  serão buscadas atualizações, se encontradas elas serão unidas ao código atual existente na nossa máquina;

### Clonando repositórios

- O ato de baixar um repositório de um servidor remoto é chamado de clonar repositório;
- Para esta ação utilizamos git clone;
- Passando a referência do repositório remoto;
- Este comando é utilizado quando entramos em um novo projeto, por exemplo;
- git clone <link> <novo nome para o repo>;

### Removendo arquivos do repo

- Os arquivos podem ser deletados da monitoração do git;
- O comando para deletar é git rm;
- Após deletar um arquivo do git ele não terá mais suas atualizações consideradas pelo git;
- Apenas quando for adicionado novamente pelo git add;

### Histórico de alterações

- Podemos acessar um log de modificações feitas no projeto ;
- O comando para este recurso é git log;
- Você receberá uma informação dos commits realizados no projeto até então;

### Renomeando arquivos

- com o comando git mv podemos renomear um arquivo;
- O mesmo também pode ser movido para outra pasta;
- E isso fará com que este novo arquivo seja monitorado pelo git;
- O arquivo anterior é excluído;
- exemplo mover arquivo: git mv rodape.css css/rodape.css;
- exemplo renomear arquivo: git mv css/banner.css css/banner2.css;

### Desfazendo alterações

- O arquivo modificado pode ser retornado ao estado original;
- O comando utilizado é o git checkout;
- Após a utilização do mesmo o arquivo sai do staging;
- Caso não seja feita uma próxima alteração, ele entra em staging novamente;
- git checkout css/syle.css (esse comando cancela as alterações feitas);
- substituirá o conteúdo do arquivo com a versão mais recente commitada no repositório;

### Ignorando arquivos no projeto

- Uma técnica muito utilizada é ignorar arquivos do projeto;
- Devemos inserir um arquivo chamado .gitignore na raiz do projeto;
- Nele podemos inserir todos os arquivos que não devem entrar no versionamento;
- isso é útil para arquivos gerados automaticamente ou arquivos que contém informações sensíveis;
- primeiro adicionar o arquivo ou pasta no .gitignore e depois criar a mesma;
- node_modules/*  = todos arquivos dentro dessa pasta serão ignorados;

### Resetando uma branch / Desfazendo todas as alterações

- com o comando git reset podemos resetar as mudanças feitas;
- Geralmente é utilizado com a flag –hard;
- Todas as alterações commitadas e também as pendentes serão excluídas;
- git reset –hard origin/main;

----------

## Trabalhando com Branchs, Stash, Tags:

### O que é um branch?

- branch é a forma que o git separa as versões dos projetos;
- quando um projeto é criado ele inicia na branch master / main, estamos trabalhando nela até esse ponto do curso;
- Geralmente cada nova feature de um projeto fica em um branch separado / novo;
- após a finalização das alterações os branchs são unidos para ter o código-fonte final;

### Criando e visualizando os branches

Para visualizar os branches disponíveis basta digitar git branch;
Para criar uma branch você precisa utilizar o comando git branch <nome>;
Essas duas operações são muito utilizadas no dia a dia do dev;

### Deletando branches

- Podemos deletar um branch com a flag –d ou –delete;
- Não é comum deletar um branch, normalmente guardamos o histórico do trabalho;
- Geralmente se usa o delete quando o branch foi criado errado;

### Mudando de branch

- Para mudar para outra branch utilizamos git checkout <nome da branch>;
- Podemos mudar para outro branch utilizando o comando git checkout -b <nome>;
- Esse código cria um novo branch e já muda para ele caso não exista;
- Este comando também é utilizado para dispensar mudanças de um arquivo;
- Alterando o branch podemos levar alterações que não foram commitadas junto, tome cuidado!;
- Sempre commitar antes de mudar de branch;

### Unindo branches

- O código de dois branches distintos pode ser unido pelo comando git merge <nome>;
- Outro comando para a lista dos mais utilizados;
- Normalmente é por meio dele que recebemos as atualizações de outros devs;
- Nunca utilizar o merge estando na master/main;

### Stash

- Podemos salvar as modificações atuais para prosseguir com uma outra abordagem de solução e não perder o código;
- O comando para esta ação é o git stash;
- Após o comando o branch será resetado para a sua versão de acordo com o repo;

### Recuperando Stash

- Podemos verificar as stashs criadas pelo comando git stash list;
- git stash apply <0,1,2,3…> aplica a stash novamente ao branch;
- também podemos recuperar a stach com o comando git stash <nome>;
- Desta maneira podemos continuar de onde paramos com os arquivos adicionados a stash;

### Removendo a Stash

- Para limpar totalmente as stash de um branch podemos utilizar o comando git stash clear;
- Caso seja necessário deletar uma stash específica podemos utilizar git stash drop <nome>;

### Utilizando tags

- Podemos criar tags nos branches por meio do comando git tag -a <nome> -m “<msg>”;
- A tag é diferente da stash, serve como um checkpoint de um branch;
- É utilizada para demarcar estágios do desenvolvimento de algum recurso;
- cria um ponto de recuperação para avançar ou retroceder;

### Verificando e alterando tags

- Podemos verificar as tags com o comando git tag;
- Podemos verificar uma tag com o comando git show <nome>;
- Podemos trocar de tags com o comando git checkout <nome>;
- Desta maneira podemos retroceder ou avançar em checkpoints de um branch;

### Enviando e compartilhando tags

- As tags podem ser enviadas para o repositório de código, sendo compartilhada entre os devs;
- O comando é git push origin <nome_da_tag>;
- Ou se você quiser enviar todas as tags git push origin –tags;

----------

## Compartilhamento e atualizações de repositórios:

### Encontrando branches

- Branches novos são criados a todo tempo e o seu git pode não estar mapeando eles
- Com o mando git fetch você é atualizado de todos os branchs e tags
- Este comando é últil para utilizar o branch de algum outro dev do time, por exemplo
git fetch -a, vai juntar tudo;

### Recebendo alterações

- O comando git pull serve para recebermos atualizações do repositório remoto
Cada branch pode ser atualizado com o git pull
- Utilizamos para atualizar a master do repo como também quando trabalhamos em conjunto e queremos receber as atualizações de um dev: 

```
git clone
git checkout master
git pull
git checkout -b “adicionar_html”
git commit -m “inicio_html” - git push
git checkout master
git merge origin/adicionando_css
git merge origin/adicionar_html
git push
git checkout master
git pull
```

### Enviando alterações

- O comando git push faz o inverso do pull, ele envia alterações para o repo remoto;
- Serve também para enviar as atualizações de um branch específico para outro dev;
- Ou quando terminamos uma tarefa e precisamos enviar ao repo;
- não enviar pastas repetidas, utilizar o .gitignore para colocar pastas como node_modules;

### Utilizando o remote

- Com o git remote podemos fazer algumas ações como: adicionar um repo para trackear ou remover;
- Quando criamos um repo remoto, adicionamos ele ao git com:  

```
git remote add origin <link>
git remote -v / git remote rm origin
git remote add origin <link>
```

### Trabalhando com submódulos

- Submódulo é a maneira que temos de possuir dois ou mais projetos em um só repositório;
- Podemos adicionar uma dependência ao nosso projeto atual, porém mantendo suas estruturas separadas;
- Para adicionar o submódulo utilizamos o comando git submodule add <repo>;
- Para verificar os submódulos o comando é git submodule;
- Podemos utilizar o submodulo para colocar bibliotecas e atualiza-las constantemente;

### Atualizando submódulo

- Para atualizar um submódulo , primeiro devemos commitar as mudanças;
- Para enviar para o repo do submódulo utilizamos git push –recurse-submodules=on-demand;
- Este fluxo fará a atualização apenas do submódulo;

----------

## Análise e inspeção de repositórios: 

### Exibindo informações

- O comando git show nos dá diversas informações úteis;
- Ele nos dá as informações do branch atual e também seus commits;
- As modificações de arquivos entre cada commit também são exibidas;
- Podemos exibir as informações de tags também com: git show <tag>;

### Exibindo diferenças

- O comando git diff serve para exibir as diferenças de um branch;
- Quando utilizado as diferenças do branch atual com o remoto serão exibidas no terminal;
- Podemos também verificar a diferença entre arquivos git diff <arquivo> <arquivo_b>;
- git checkout -b “testando_Show” - git commit -m”adicionando”- git diff master;

### Log resumido

- O comando git shortlog nos dá um log resumido do projeto;
- Cada commit será unido por nome do autor;
- Podemos então saber quais commits foram enviados ao projeto e por quem;
- gera informações de todo o projeto, não importa a branch;

----------

## Administração de repositórios: 

### Limpando arquivos untracked

- O comando git clean vai verificar e limpar arquivos que não estão sendo trackeados;
- Ou seja, todos que você não utilizou git add;
- Utilizado para arquivos que são gerados automaticamente, por exemplo, e atrapalham a visualização do que é - realmente importante;
- git clean -f;
- Utilizar o git add antes do git clean para salvar oq deseja;

### Otimizando o repositório

- O comando git gc é uma abreviação para garbage collector;
- Ele identifica arquivos que não são mais necessários e os exclui;
- Isso fará com que o repositório seja otimizado em questões de performance;

### Checando integridade de arquivos

- O comando git fsck é uma abreviação de File System Check;
- Esta instrução verifica a integridade de arquivos e sua conectividade;
- Verificando assim possíveis corrupções em arquivos;
- Comando de rotina, utilizado para ver se está tudo certo com nossos arquivos;

### Reflog

- O git reflog vai mapear todos os seus passos no repositório, até uma mudança de branch é inserida neste log;
- Já o git log, que vimos anteriormente, apenas armazena os commits de um branch;
- Os reflogs ficam salvos até expirar, o tempo de expiração padrão é de 30 dias;
- git reset –hard <hash>;

### Transformando o repo para arquivo

- Com o comando git archive podemos transformar o repo em um arquivo compactado, por exemplo;
- O comando é git archive –format zip –output master_files.zip master;
- E então a master vai estar zipada no arquivo master_files.zip;

----------

## Melhorando os commits do projeto: 

### A importância do commit

- O problema: commits sem sentido atrapalham o projeto;
- Precisamos padronizar os commits, para que o projeto cresça de forma saudável também no versionamento, isso ajuda em:
- Review do Pull Request;
- Melhoria dos log do git log;
- Manutenção do projeto (Voltar código, por exemplo);

### Branches com commits ruins

- Há uma solução chamada private branches;
- Onde criamos branches que não serão compartilhados no repositório, então podemos colocar qualquer commit;
- Ao fim da solução do problema podemos fazer um rebase;
- O comando será: git rebase <atual> <funcionalidade> -i;
- Escolhemos os branches para excluir (squash) e renomear com (reword)
:x!;

### Boas mensagens de commit

- Separar assunto do corpo da mensagem;
- Assunto com no máximo 50 caracteres;
- Assunto com letra inicial maiúscula;
- Corpo com no máximo 72 caracteres;
- Explicar o porque e como do commit, e não como o código foi escrito;
- apagar a ultima aspas da mensagem do commit e apertar enter para escrever mais
git commit -m “
"
![GitCommit!](/Sprint%20-%201/1.%20Git%20-%20Github/gitmCommit.png)
----------

## Explorando e entendendo o GitHub:

### Criando Repositório

- No github inicializamos os repositórios e temos algumas informações importantes para preencher, vamos vê-las em detalhes;
- Algumas delas são: Nome do repo, descrição, licença;
- Tudo poderá ser alterado ao longo do seu projeto, mas é interessante conhecer os detalhes das informações para configurar um projeto;

### A aba Code

- Na aba Code teremos acesso a informações importantes, como o própio código fonte;
- Podemos checar também uma documentação do projeto pelo README.md;
- E os detalhes da licença do projeto;
- Criar branches, adicionar arquivos e muito mais;

### A aba issue

- Na aba issue podemos criar tarefas ou possíveis bugs do projeto;
- Interessante para as organizações se manter ciente do que ainda precisa fazer ou corrigir;
- Normalmente há um padrão para criação de novos issues;
- Podemos utilizar o Markdown no texto também (Igual o README.md);
- A issue deve ter uma label e também um responsável;

### A aba Pull Request

- Na aba Pull Request é onde os colaboradores do projeto enviam código para resolver as issues ou adicionar novas funcionalidades ao projeto;
- A ideia é que o código não seja inserido direto na master e sim passe por um pull request, para ser analisado;
- O pull request vem de um novo branch criado no projeto e enviado para o repo, com o incremento de código;

### A aba actions

- Na aba Actions é onde se cria as automatizações de deploy com integração em outros serviços;
- Incluindo CI / CD ( Continuous integration / Continuous Development);
- Ou seja, podemos criar uma rotina de atualizar a master automaticamente e outros processos;

### Na aba Projects

- Na aba projects podemos criar um projeto e utilizar um quadro de tarefas;
- Este processo é conhecido como kanban e pode ajudar a organizar seu time, criando notas que podem virar issues;
- Estrutura interessante: Backlog, retorno de qualidade, desenvolvimento, teste, finalizadas
A tela lembra muito o software Trello;
- Kanban = fluxos de trabalho utilizando quadros e cartões personalizados;

### A aba Wiki

- Na aba wiki podemos criar uma documentação mais extensa para o projeto;
- Como descrever funcionalidades, bugs conhecidos e não solucionados, entre outras funções;
- A ideia é que seja um repositório de conhecimento sobre o projeto;

### A aba insights

- Na aba insights temos informações detalhadas do projeto, como:
- Quem são os contribuidores, commits, forks e muito mais;
- Interessante para entender com o projeto está andando e a sua evolução desde o início;

### A aba Settings

- Na aba settings temos acesso a diversas configurações do projeto;
- é onde podemos alterar o nome do repo ou remover / adicionar features;
- E também é nela que adicionamos os colaboradores ao projeto;
- O repositório pode  ser removido nessa aba  ;

### Criando um Gist

- Gists são pequenos blocos de código que podem ser hospedados no Github também;
- Você pode armazenar uma solução que achou interessante para algum problema e não quer perder, por exemplo;
- E o link do gist pode ser compartilhado;
- No fim das contas o gist acaba sendo um repositório também;
- https://gist.github.com/lucasbergamo/a684c2bf482cb1d85969b458d3925bcb;

### Encontrando Repositórios

- O github não serve apenas para salvar os nossos projetos, podemos encontrar muitos repos interessantes;
- Podemos até aprender com isso também, olhando o código fonte de desenvolvedores experientes;
- E não para por aí: Você pode dar star nos projetos que gostou ou fork nos que deseja continuar em um repo próprio;
- https://github.com/facebook/react;

----------

## Markdown do básico ao avançado:

### O que é Markdown?

- O markdown é uma forma de adicionar estilo a textos na web;
- O arquivo README.MD aceita markdown;
- Você vai conseguir exibir: trechos de código, links, imagens e muito mais;
- Dando uma melhor experiência para o usuário nas suas documentações;

### Cabeçalhos

- Os cabeçalhos em markdown são determinados pelo simbolo #;
- Cabeçalhos são os famosos títulos ou headings do HTML;
- #=> h1, ## => h2, ###=> h3 e assim por diante;

### Ênfase no texto

- Temos símbolos que podem dar ênfase ao texto;
- Para escrever em negrito: **texto** ou __texto__;
- Para escrever em itálico: *texto* ou _texto_;
- Combinando os dois: _um **texto** combinado_;

### Listas

- Temos as listas ordenadas e não ordenadas em markdown;
- As listas não ordenadas começam com: * item;
- As listas ordenadas com: 1. item;

### Imagens

- É possivel inserir imagens em markdown também;
- Veja a sintaxe: ![Texto Alt](link imagem);
- A imagem pode estar no própio repo ou ser externa;

### Links

- Com o markdown podemos inserir links de forma fácil;
- A sintaxe é a seguinte: [Texto do link](link);
- se for um link do github pode inserir de forma direta: https://www.github.com;

### Código - Github

- Podemos inserir código no markdown também
- A sintaxe é: ``` código```
``` 
javascript 
function soma (a,b) { 
return a + b; 
} 
```
- Esta sintaxe é do markdown especial do github;

### Task list - Github

- Podemos inserir uma lista de tarefas pelo Markdown;
- A sintaxe para tarefas concluídas: - [x] CSS do rodapé;
- Para não concluídas: - [] CSS da página de contatos;
- Esta sintaxe é do markdown especial do github;

----------

## Projeto: Portifólio com Github Pages:

### O que é github pages

- Uma forma de criar uma página estática nos servidores do github;
- Ou seja, uma alternativa gratuita para hospedar nosso portfólio;
- Muito simples de colocar no ar, não precisa de domínio ou servidor;
- Muitas empresas utilizam para apresentar o seu projeto ou a própria documentação ;

### Como criar a página

- Você deve seguir alguns passos simples, veja;
- Criar um repositório com o nome <nomedousuario.github.io>;
- Clonar o repositório no nosso computador;
- Adicionar o código do projeto na branch master;
- Enviar o código por meio de push;
- E pronto, você tem um site em https://nomedousuario.github.io;

----------
