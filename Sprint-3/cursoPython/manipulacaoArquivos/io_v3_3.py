#!/usr/local/bin/python3

#.strip() = remove o item desejado da string

arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()