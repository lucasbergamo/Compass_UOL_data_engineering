from random import randint

numero_informado = -1
numero_secreto = randint(0, 9) # vai atribuir a numero_secreto um número entre 0 e 9

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o número: '))

print('Número secreto {} foi encontrado!'.format(numero_secreto))

# nunca vai sair do laço se ficar tentando o mesmo número, tem que tentar numeros diferentes