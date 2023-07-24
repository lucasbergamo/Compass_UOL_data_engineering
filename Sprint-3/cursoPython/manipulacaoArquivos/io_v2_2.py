#!/usr/local/bin/python3

# Método stream, consome os dados que for necessário, não carrega tudo na memória

arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.split(',')))
arquivo.close()