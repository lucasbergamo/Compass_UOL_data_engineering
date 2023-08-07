-- Criar novo script Python que implementa o algoritmo a seguir:

1 - Receber uma string via input

2 - Gerar o hash  da string por meio do algoritmo SHA-1

3 - Imprimir o hash em tela, utilizando o método hexdigest

4 - Retornar ao passo 1

-- Criar uma imagem Docker chamada mascarar-dados que execute o script Python criado anteriormente

```cd exercicio container```

```docker build -t mascarar-dados .```

--  Iniciar um container a partir da imagem, enviando algumas palavras para mascaramento

```docker run -it --name mascarar-container mascarar-dados```

-- Registrar o conteúdo do script Python, arquivo Dockerfile e comando de inicialização do container neste espaço.

```
import hashlib

def gen_sha1_hex(input_string):
    sha1_hash = hashlib.sha1(input_string.encode())
    return sha1_hash.hexdigest()

def main():
    while True:
        print_string = input("Digite uma string: ")
        sha1_hash_hex = gen_sha1_hex(print_string)
        print(f"O hash SHA-1 da string: '{print_string}' é:, {sha1_hash_hex}")

if __name__ == "__main__":
    main()
```