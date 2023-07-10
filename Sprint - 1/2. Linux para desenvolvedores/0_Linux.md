# Sumário

<details><summary><strong>Navegação</strong></summary>

1. [Introdução](#introdução)
2. [Linux Fundamental](#linux-fundamental)
3. [Gerenciamento de diretórios e arquivos](#gerenciamento-de-diretórios-e-arquivos)
4. [Gerenciamento de pacotes e aplicativos](#gerenciamento-de-pacotes-e-aplicativos)
5. [Filtros e buscas de arquivos e diretórios](#filtros-e-buscas-de-arquivos-e-diretórios)
6. [Editores de texto](#editores-de-texto)
7. [Gerenciamento de usuários e grupos](#gerenciamento-de-usuários-e-grupos)
8. [Gerenciamento de Permissões](#gerenciamento-de-permissões)
9. [Gerenciamento básico de redes](#gerenciamento-básico-de-redes)
10. [Compactação e descompactação de arquvos e diretórios](#compactação-e-descompactação-de-arquvos-e-diretórios)

</details>

## Introdução:

- baixar ISO do ubuntu no site oficial - Ou ubuntu server se o pc for mais fraco
- baixar Virtual Box (VM) - windows host
- ou baixar o VmWare

1. aplicativos e recursos
2. programas e recursos
3. ativar ou desativar recursos do Windows
4. Habilitar Plataforma de máquina virtual
5. Plataforma do Hipervisor do Windows

- Usuário: lucas0210
- Senha: ****

- para funcionar o virtual box = 

1. acessar cmd via administrador
2. bcdedit
3. bcdedit /set hypervisorlaunchtype off

- para funcionar o wsl = 

1. acessar cmd via administrador
2. bcdedit
3. bcdedit /set hypervisorlaunchtype auto

- só da para utilizar 1 por vez na máquina

- mudar teclado do linux por linha de comando : 

1. sudo nano /etc/default/keyboard
2. XKBLAYOUT="br"
3. Ctrl + o E Ctrl + x
4. sudo reboot

----------

## Linux Fundamental:

- Comandos básicos;
- Noções do SO;
- Familiaridade com o terminal;

### Comando cd

- cd .. = voltar 1 diretório;
- cd / = voltar para pasta raiz;
- cd /var/log;
- cd ../../var = voltar 2 diretórios e entrar em var;
- cd + tab + tab = mostra as pastas;
- cd + tab = auto complete;
- cd etc && ls = vai abrir a pasta etc e mostrar os arquivos nela;

### Comando ls

- ls = mostra os arquivos;
- ls -l = mostra arquivos e pastas em detalhes;
- na ordem : permissões / usuário e grupo / tamanho / data de criação;
- ls -a =  mostra os arquivos ocultos;
- ls -lh = mostra o tamanho em kbp;
- ls -ltr = mostra data e ordenado de forma crescente;
- ls -l /etc = mostra os arquivos em detalhes da pasta etc;
- ls -R = mostra todas as pastas e arquivos dentro das pastas;
- ls -lS = ordena por itens mais pesado pro mais leve;
- ls -m = lista de diretórios separados por virgula;

### Comando Clear

- clear;

### Comando cat

- cat teste.txt = mostra oq está escrito no arquivo de texto;
- cat teste teste2 > teste3 = vai criar um arquivo teste3 com a junção do teste e teste2;
- cat -n teste3.txt = mostra os numero de linhas que têm na página;
- cat -e teste3.txt = mostra um $ no final de cada linha;
- cat teste >> teste2 = concatena o conteúdo do teste no teste 2;

### Comando Touch

- touch teste5.txt = criar um arquivo de texto com o nome teste5;
- touch a.txt b.txt c.txt = cria múltiplos arquivos;

### Comando man

- man ls = mostra tudo sobre o comando ls;
- man cd = mostra tudo sobre o comando cd;

### Buscando comandos com Ctrl + r

- Ctrl + r = para selecionar comando ja utilizados;

----------

## Gerenciamento de diretórios e arquivos:

### Criando diretórios mkdir

- mkdir dir1 = cria o diretório dir1;
- mkdir js css img = cria 3 diretórios;
- mkdir -v dir1 dir2 dir3 = mostra no termina de comando o status;
- mkdir -p dir5/dir6/dir7/dir8 = flag -p serve para poder criar vários diretórios e subdiretórios;

### Removendo arquivos e diretórios rm

- rm a.txt = apaga o arquivo;
- rm 1.txt 2.txt 3.txt = apaga vários arquivos;
- rm -i a.txt = vai precisar de confirmação para apagar;
- rm -rfv dir1 = remove diretórios e tudo que tiver dentro dele, o r pra apagar tudo, o f para forçar e o v para mostrar informações sobre a remoção;

### Removendo apenas diretórios rmdir

- rmdir teste1 = remove o diretório;
- rmdir teste1/teste2/teste3 = remove os diretórios;

### Copiando diretórios e arquivos cp

- cp doc.txt doc2.txt = copia e cria o arquivo doc2.txt;
- cp c.txt dir5 = copia o arquivo para o diretório dir5;
- cp c.txt doc.txt doc2.txt copia = copia os arquivos para o diretório copia;
- cp -r dir dir2 = copia o diretório dir para dentro do dir2;
- cp dir5/* dirteste = copia todos os arquivos de dir5 para dirteste;
- cp doc* dirteste = copia todos os arquivos doc para o diretório dirteste;

### Movendo diretórios e arquivos mv

- mv doc txt doc3.txt = ele move o conteúdo para o novo arquivo doc3 e o doc deixa de existir;
- mv doc3.txt Downloads/ = move o arquivo para o diretório;

### pwd

- pwd = mostra o caminho do diretório onde estamos;

----------

## Gerenciamento de pacotes e aplicativos:

### Atualizando repositórios

- sudo apt-get update && apt-get upgrade -y;
- atualizando pacotes / aplicativos = sudo apt-get upgrade;

### Instalando pacotes / aplicativos

- sudo apt-get install tree;

### Deletando um pacote/ aplicativo

- sudo apt-get purge tree;

### Atualizando o Linux

- sudo apt-get dist-upgrade;

### Limpando pacotes / aplicativos desnecessários

- sudo apt-get autoremove;

### Buscando pacotes / aplicativos

- apt-cache search htop;
- apt-cache search python;

### Utilizando apenas apt

- sudo apt htop;

### Salvando o estado da máquina (VM)

----------

## Filtros e buscas de arquivos e diretórios:

### Comando head

- head documento.txt;
- head -n 2 documento.txt;
- head -n 1 documento.txt > documento2.txt = transfere a linha 1 para o arquivo2;

### Comando Tail

- tail documento.txt;
- tail -n 2 documento.txt;
- tail -n 3 documento.txt > documento2.txt;
- tail -f documento.txt > mostra as alterações em tempo real;

### Comando Grep

- grep ‘lorem’ documento.txt = mostra o texto com a palavra destacada;
- grep -i ‘lorem  documento.txt = ignora o case sensitive’;
- grep -c ‘lorem’ documento.txt = mostra quantos lorem tem no arquivo;
- grep ‘lorem ipsum’ -r = procura essas palavras em qualquer lugar no sistema;

### Comando find

- find -name ‘documento.txt’ = acha o caminho do arquivo;
- find -iname ‘DOCUMENTO.TXT’;
- find  -iname ‘documento*’ = pesquisa todos os arquivos referente a esse nome;
- find -empty = mostra todos arquivos vazios;
- find -empty -type f = mostra arquivos;
- find -empty -type d = mostra diretórios;

### Comando locate

- locate documento.txt;
- locate -S = mostra o banco de dados do sistema;

### Onde os comandos são executados

- wich nano;
- wich ls;
- o wich faz uma track de onde esse comando está no sistema;

----------

## Editores de texto:

### Nano: criando, salvando e saindo de arquivo

- sudo apt-get install nano;
- nano = abre um editor de texto ou um arquivo;
- nano texto.txt;
- para salvar = Ctrl + O;
- para sair = Ctrl + X;

### Nano: editando arquivo

- ao abrir um arquivo e digitar Ctrl + r e o nome do outro arquivo;
- ele irá inserir o texto do arquivo para o primeiro;

### Nano: copiando, colando e recortando conteúdo

- alt + a = seleciona tudo que a seta tocar;
- alt + 6 = copia o texto selecionado;
- Ctrl + k = recorta o texto selecionado;
- Ctrl + u = cola o texto;

### Nano: movimentação dentro de arquivo

- alt + / = vai para o fim do arquivo;
- alt + \ = vai para o inicio do arquivo;
- alt + g = você escolhe pra qual linha ir;

### Nano: busca e replace

- Ctrl + w = busca palavra ou frase específica;
- alt + r = substituir uma palavra por outra em todo texto;

### Vim: instalação e modos do editor

- sudo apt-get install vim;
- vim arquivonovo.txt;
- tem modo comando e inserção ( apertar i );

### Vim: editando, salvando e fechando arquivo

- :x = vai salvar e sair do arquivo;
- :w = apenas salvar sem sair;
- :q = sair do arquivo;

### Vim: deletando linha, undo e redo

- no modo de comando;
- e + d = apaga a linha;
- d + seta = apaga uma linha no sentido;
- u = desfaz as mudanças = undo;
- ctrl + e = refaz as mudanças = redo;

### Vim: search e replace

- no modo comando
- / + a palavra para procurar = search
- ```:%s/Lorem/Nova/g = replace```, substitui a palavra Lorem por Nova, em todo arquivo;
- ```:s/ipsum/Trocar/g``` = substitui a palavra ipsum por Trocar apenas na linha selecionada;

### Dica: Saindo sem salvar arquivo no Vim

- :q! = sai sem salvar nada que foi alterado;

----------

## Gerenciamento de usuários e grupos: 

### Adicionando usuários ao linux

- sudo adduser pedro;
- sudo adduser maria;
- ls /home/ = checar os usuários;

### Deletando usuários

- sudo userdel –remove pedro;

### Mudando o nome de display do usuário

- mudar o nome do usuário maria para roberta;
- sudo usermod -c “roberta” maria;

### Mudando o nome do diretório base e do usuário no terminal

- sudo usermod -l roberta -d /home/roberta -m maria;
- mudou de maria para roberta;

### Bloqueando e desbloqueando usuários

- sudo usermod -L roberta = bloqueia;
- sudo usermod -U roberta = desbloqueia;

### O que é um grupo no linux

- Contém vários usuários;
- Facilitar gerenciar as permissões;
- Quando um usuário é adicionado ele também é adicionado a um grupo com o seu nome ou um que desejar escolher;

### Criando um grupo no Linux

- getent group = mostra todos os grupos ja criados;
- sudo groupadd -g 9999 devs = criou o grupo devs com id único 9999;

### Deletando um grupo

- sudo groupdel devs;
- getent group;

### Movendo um usuário para outro grupo

- groups roberta = mostra os grupos que roberta está;
- sudo usermod -a -G testando roberta = roberta foi movida para o grupo testando;
- sudo gpasswd -d roberta testando = remove roberta do grupo testando;

### Dica: como virar um super usuário (root);

- sudo su;
- exit = sair do usuário root;

### Dica: trocando a senha do usuário

- passwd = digitar senha atual e nova senha;

----------

## Gerenciamento de Permissões:

### Conceitos fundamentais de permissão

- Possibilidade de alterar 3 propriedades de arquivos e diretórios;
- Leitura: se os usuários poderão ler o arquivo (R - read);
- Escrita: se os usuários poderão escrever no arquivo (W - write);
- Execução: se os usuários poderão executar o arquivo (X - execute);

### Entendendo como funcionam as permissões

- 1 222 333 444 <-> drwxr-xr-x;
- 1 serve para d ou - = diretório ou arquivo;
- 222 = permissões do owner;
- 333 = permissões do grupo ( que o arquivo pertence );
- 444 = permissões dos demais usuários ( que não são donos do arquivo e também não fazem parte do grupo do arquivo );
- r = read / w = write and edit / x = execute / - = sem permissão;
- drw-rw-r– = diretório, owner e grupo com permissão de ler e escrever, demais só com permissão de ler;
- -r–r–r– = arquivo, só a permissão de leitura para todos;
- ls -lh;

### Permissão numérica: teoria

- Comando para alterar permissões: chmod xxx file/dir
- onde ‘x’ representa as permissões em números:
- 0: sem permissão —
- 1: executar –x
- 2: escrever -w-
- 3: ler r–
- 4: escrever e executar -wx
- 5: ler e executar r-x
- 6: ler e escrever rw-
- 7: ler, escrever e executar rwx

### Permissão numérica: prática

- chmod 000 c.txt

### Permissão simbólica: teoria

- Comando para alterar permissões: chmod args file/dir
- Onde “args” pode ser representado por:
- ```+``` : adiciona permissão a um arquivo ou diretório
- ```-``` : remove permissão a um arquivo ou diretório
- u : dono do arquivo (user / owner)
- g : Grupo (group)
- o : Outros (others)
- a : todos (all)
- chmod o=x : concede permissão de executar para outros
- chmod a=rwx : concede todas as permissões a todos
- chmod g-w : removendo permissão de escrever para grupos
- chmod u+rw : concedendo permissão de ler e escrever para o user / owner

### Permissão simbólica: prática


### Alterando o proprietário / owner do arquivo

- chmod 700 c.txt = apenas o dono tem permissão total a esse arquivo
- sudo chown roberta c.txt = agora só roberta pode acessar o arquivo
- sudo chown roberta:dev = apesar de passar para o grupo, apenas o usuário pode 

### Alterando o grupo do arquivo

- sudo chgrp maria.texto.txt

### Dica: copiando e colando no terminal

- Ctrl + shift + c = copiar
- Ctrl + shift + v = colar

### Dica: histórico de últimos comandos digitados

- history

----------

## Gerenciamento básico de redes:

### Como a web funciona?

- Envio de requisição para um domínio ( DNS )
- Verificação do domínio ( DNS = IP )
- Requisição da resposta para o servidor que pertence a este domínio
- Retorno da resposta a quem solicitou

### O que é DNS?

- DNS = Domain Name System
- Traduz o endereço de ip em um domínio
- Não precisamos gravar números de IP, o que seria mais difícil

### Funcionamento:

- Uma pessoa digita um domínio no navegador
- Um servidor lê o DNS digitado; ( DNS Resolver )
- Encontra o servidor pela combinação de DNS e IP
- Retorna ao usuário o site desejado

### O que são portas?

- É um endpoint
- Sempre está associada a um IP
- conexões do site limitadas pelas portas ao invés de outros servidores

* Exemplos de portas:

- 20 : FTP
- 22 : SSH
- 80 : HTTP
- 443 : HTTPS

### O que é TCP?

- Transmission Control Protocol = TCP
- Protocolo utilizado para transmissão de dados pela rede

### O que utiliza o TCP:

- SMTP ( Envio de e-mails )
- FTP ( transferência de arquivos )
- HTTP ( protocolo para navegar na internet ) 

### O que é UDP?

- User Datagram Protocol = UDP
- Espécie de irmão do TCP, serve também para enviar dados
- O UDP se preocupa mais com a velocidade do envio do que a confiabilidade
- Logo o TCP é mais seguro
- UDP é utilizado principalmente para jogos online e streaming que necessitam baixas latência ou ping

### Comando: ping

- receber bytes do site significa que estamos conseguindo acessa-lo
- ping www.google.com
- ping 8.8.8.8

### Comando: netstat

- sudo apt-get install net-tools
- netstat -a = todas conexões que estão sendo feitas (unix são do sistema)
- netstat -at = todas as conexões TCP
- netstat -au = todas as conexões UDP
- netcat -u google.com 80 = vai fazer uma requisição udp a porta 80 do google
- netstat -au = vai mostrar essa nova conexão

### Comando ifconfig ( interface configuration )

- ifconfig
- enp0s3 = 

### Comando nslookup 

- serve para saber o ip através do DNS
- nslookup google.com
- o ip do google pode estar diferente, pois ele utiliza de servidores espalhados pelo mundo para facilitar e diminuir a latência, no caso esse servidor replica o servidor original do google 

### Comando tcpdump

- sudo tcpdump
- consegue ver oq está sendo transferido pelo protocolo TCP da nossa máquina

### Dica: como ver o ip da sua máquina

- ifconfig ou
- hostname -I = mostra apenas o ip

----------

## Compactação e descompactação de arquvos e diretórios:

### Compactando arquivos com tar

- tar -czvf compactado.tar.gz dir6 ( cria um arquivo de nome compactado com o dir6 dentro)
- c: criar arquivo
- z: transformar em zip
- v: mostra o progresso
- f: especificar o nome do arquivo para ser compactado

### Compactando múltiplos arquivos em um só

- tar -czvf compactado2.tar.gz c.txt dir6 documento.txt
- pode juntar arquivos e diretórios

### Descompactando arquivos

- tar -xzvf compactado2.tar.gz
- tar -xzvf compactado2.tar.gz -C descompactar2 ( flag -C, escolhe onde vai ser descompactado)

### Compactação em zip

- zip -r compacto.zip dir6

### Descompactando arquivos em zip

- unzip compacto.zip
- unzip compacto.zip -d videos/ ( o arquivo vai ser descompactado na pasta videos)

### Dica: veja o que tem dentro dos arquivos compactados

- tar -tvf compactado2.tar.gz

----------