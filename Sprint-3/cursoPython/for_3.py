produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793 }

for chave in produto.keys(): # utilizar o .keys é redundante, pois já é o valor padrão
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(f'{chave} = {valor}')