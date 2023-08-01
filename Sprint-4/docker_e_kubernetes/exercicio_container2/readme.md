-- Criar novo script Python que implementa o algoritmo a seguir:

1 - Receber uma string via input

2 - Gerar o hash  da string por meio do algoritmo SHA-1

3 - Imprimir o hash em tela, utilizando o método hexdigest

4 - Retornar ao passo 1

-- Criar uma imagem Docker chamada mascarar-dados que execute o script Python criado anteriormente

```docker build -t mascarar-dados .```

--  Iniciar um container a partir da imagem, enviando algumas palavras para mascaramento

```docker run -it --name script mascarar-dados```

-- Registrar o conteúdo do script Python, arquivo Dockerfile e comando de inicialização do container neste espaço.