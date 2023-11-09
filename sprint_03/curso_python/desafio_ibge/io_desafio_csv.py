#!/usr/local/bin/python3

import csv
from urllib import request



def read(url):
    with request.urlopen(url) as entrada: #entrada é o resultado do request url open
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1') # é preciso fazer o decode do arquivo
        print('Dowload completo!')
        for cidade in csv.reader(dados.splitlibes()):
            print(f"{cidade[8]}: {cidade[3]}")


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')   
    
    # o r antes da string usa a url sem formatar caracteres especiais
    # deve utilizar quando trabalhar com url