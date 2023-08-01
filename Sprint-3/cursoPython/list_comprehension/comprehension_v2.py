# troca colchetes por parênteses

generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator)) # saída 0
print(next(generator)) # saída 4
print(next(generator)) # saída 16
print(next(generator)) # saída 36
print(next(generator)) # saída 64
print(next(generator)) # Erro!

# Generator com FOR

generator = (i ** 2 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)

# Dicionário

#{i: i * 2)  i: = chave , i * 2 = valor

dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)

# acessamos chave, valor uzando .items

for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')