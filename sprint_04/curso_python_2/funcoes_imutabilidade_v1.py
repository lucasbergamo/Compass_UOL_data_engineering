#!/usr/local/bin/python3
from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]

# o conteúdo da lista foi mudado ( passando um função dentro da lista) 
#valores.sort()
#valores.reverse()
#print(valores)

# a lista não é alterada
print(sorted(valores))
print(valores)
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(reversed(valores))
print(list(reversed(valores)))
print(valores)