#!/usr/local/bin/python3

# carrega tudo na memória para depois fazer o for
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
    # print(registro.split(',')) - vai criar uma lista 
    # print(*registro.split(',')) - ao colocar o asterisco, os elementos ficam semi-impressos sem a virgula, apenas com espaçamento

