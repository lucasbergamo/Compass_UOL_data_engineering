#!/usr/local/bin/python3

# O finally sempre será executado mesmo se o codigo for perigoso e dar erro

try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

except IndexError:
    pass   # serve como um bloco vazio

finally:
    arquivo.close()