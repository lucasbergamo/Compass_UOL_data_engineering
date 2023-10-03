import random

lista_inteiros = []

for i in range(0,int(250)):
    lista_inteiros.append(random.randrange(250))
    
lista_inteiros.reverse()

print(lista_inteiros)