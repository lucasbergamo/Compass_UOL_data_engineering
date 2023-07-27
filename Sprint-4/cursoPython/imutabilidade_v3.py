#!/usr/local/bin/python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name

# Português do Brasil
setlocale(LC_ALL, 'pt_BR')

# Exemplo SQL de forma Declarativa e Imperativa(passo a passo)

# declarativo : você diz oq quer e o programa faz a convenção
# imperativo : é preciso dizer passo a passo como deve ser feito

# primeiro:

# select nome, rua from clientes

# segundo:

# clientes = ler_arquivo()
# resultados = []
# for cliente in clientes:
#     resultados.append({'nome': cliente.nome, 'rua': cliente.rua})
# return resultados


# Listar todos os meses do ano com 31 dias

# normalmente esse é mais utilizado 
print('Meses com 31 dias:')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'- {month_name[mes]}')