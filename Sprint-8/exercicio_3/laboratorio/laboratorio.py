import random
import time
import os
import names

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []

for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

dados = []

for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

nome_arquivo = "nomes_aleatorios.txt"

with open(nome_arquivo, "w") as arquivo:
    for nome in dados:
        arquivo.write(nome + "\n")

print(f"O arquivo {nome_arquivo} foi gerado com sucesso!")

os.system(f"notepad.exe {nome_arquivo}")