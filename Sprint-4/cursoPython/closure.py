#!/usr/local/bin/python3

def multiplicar(x): # função que retorna função = High Order
    def calcular(y):
        return x * y
    return calcular

if __name__ == '__main__':
    dobro = multiplicar(2) # função armazernada em variável = First Class
    triplo = multiplicar(3) # laze valuation
    print(dobro, triplo)
    print(f'O triplo de 3 é {triplo(3)}')
    print(f'O dobro de 7 é {dobro(7)}')
