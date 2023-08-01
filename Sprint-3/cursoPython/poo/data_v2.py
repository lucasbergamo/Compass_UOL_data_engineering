class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        print('opa')

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

d1 = Data(5, 12, 2019)
#d1.dia = 5
#d1.mes = 12
#d1.ano = 2019
print(d1)

d2 = Data(29, 12, 2002)
#d2.dia = 5
#d2.mes = 12
#d2.ano = 2019
print(d2)