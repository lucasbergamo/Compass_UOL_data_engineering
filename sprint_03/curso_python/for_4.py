# por conta do break o else não sera executado

for i in range(1, 11):
    if i == 6:
        break
    print(i)
else:
    print('Fim!')


# função sortear_dado numeros entre 1 e 6
# se for impar continue
# Se o numero for par e igual ao valor sorteado pela função, imprimir 'ACERTOU'
#e depois chamar o break
# se não acertar chama o else... print('Não acertou o número')

from random import randint

def sortear_dado():
    return randint(1, 6)

for dado in range(1, 7):
    if dado % 2 == 1:
        continue
    
    if sortear_dado() == dado:
        print(f'Acertou: {dado}')
        break
else:
    print('Não acertou o Número!')        