#!/usr/local/bin/python3
from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17}
]

# para somar apenas as idades dos menores
menores = filter(lambda p: p['idade'] < 18, pessoas)
soma_idades = reduce(lambda idades, p: idades + p['idade'], menores, 0)
print(soma_idades)

soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
# 1 parametro = acumulador , 2 = itens, 3 = valor inicial do acumulador
print(soma_idades)

# map filter e reduce no mesmo exemplo:

so_idades = map(lambda p: p['idade'], pessoas) 
#  pegou apenas os valores de idade do dicionário
menores = filter(lambda idade: idade < 18, so_idades)
# o resultado do map foi passado no filter para pegar só as menores de 18
soma_idades = reduce(lambda idades, idade: idades + idade, menores, 0)
# passou o resultado das menores pro reduce somando as idades
print(soma_idades)
