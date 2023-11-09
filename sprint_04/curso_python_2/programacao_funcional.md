**Sumário**

[Retornar](https://github.com/lucasbergamo/Compass_UOL_data_engineering)

<details><summary><strong>Navegação</strong></summary>

- [Recursos Suportados](#recursos-suportados)
- [Função de Primeira Classe](#função-de-primeira-classe)
- [Funções de alta Ordem](#funções-de-alta-ordem)
- [Closure](#closure)
- [Funções Lambda (anônima)](#funções-lambda-anônima)
  - [Alternativa ás Funções Lambda](#alternativa-ás-funções-lambda)
- [Map](#map)
- [Filter](#filter)
- [Reduce](#reduce)
- [Fatorial recursivo (desafio)](#fatorial-recursivo-desafio)
- [Imutabilidade (desafio)](#imutabilidade-desafio)
- [Generators](#generators)
- [Implementando Map](#implementando-map)
- [Desafio Maior Divisor Comum](#desafio-maior-divisor-comum)

</details>

---


## Recursos Suportados

- First class Functions
- High Order Functions
- Closure
- Anonymous Functions
- Recursion
- Immutability
- Lazy Evaluation


## Função de Primeira Classe

[Função de Primeira Classe](./funcao_primeira_classe.py)

```
#!/usr/local/bin/python3

def dobro(x):
    return x * 2

def quadrado(x):
    return x ** 2

if __name__ == '__main':
    
    # Retornar alternadamente o dobro ou quadrado nos números de 1 a 10
    funcs = [dobro, quadrado] * 5
    for func, numero in zip(funcs, range(1,11)):
        print(f'O {func.__name__} de {numero} é {func(numero)} ')
```

## Funções de alta Ordem

[Funções de alta Ordem](./funcao_alta_ordem.py)

```
#!/usr/local/bin/python3
from funcao_primeira_classe import dobro, quadrado

def processar(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))

if __name__ == '__main__':
    processar('Dobros de 1 a 10', range(1, 11), dobro)
    processar('Quadrados de 1 a 10', range(1, 11), quadrado)

```

## Closure

[Closure](./closure.py)

```
#!/usr/local/bin/python3

def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular

if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro, triplo)
    print(f'O triplo de 3 é {triplo(3)}')
    print(f'O dobro de 7 é {dobro(7)}')    
```

## Funções Lambda (anônima)

[Funções Lambda](./funcoes_lambda.py)

```
#!/usr/local/bin/python3
compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)

totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preco'],
        compras
    )
)

print('Preços totais:', totais)
print('Total geral:', sum(totais))
```

### Alternativa ás Funções Lambda

[Alternativa ás Funções Lambda](./funcoes_lambda_alternativa.py)


## Map

[Map](./map.py)

```
#!/usr/local/bin/python3

lista_1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26}
]

so_nomes = map(lambda p: p['nome'], lista_2)
print(list(so_nomes))

so_idades = map(lambda p: p['idade'], lista_2)
print(sum(so_idades))

# Desafio : Usando map retorne frases

frases = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos.', lista_2)
print(list(frases))
```

## Filter

[Filter](./filter.py)

```
#!/usr/local/bin/python3

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17}
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

# Desafio : Filtrar nomes com caracteres maior igual a 7

nomes_grandes = filter(lambda p: len(p['nome']) >= 7, pessoas)
print(list(nomes_grandes))
```

## Reduce

[Reduce](./reduce.py)

```
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

soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
# 1 parametro = acumulador , 2 = itens, 3 = valor inicial do acumulador
print(soma_idades)
```

## Fatorial recursivo (desafio)

[Desafio](./fatorial_recursivo.py)

```
#!/usr/local/bin/python3

def fatorial(n):
    return (n * fatorial(n-1)) if n > 1 else 1

if __name__ == '__main__':
    n = 0
    print(f'{n}! = {fatorial(n)}')

    # 6 semanas em segundos é igual a 10!
    print(6 * 7 * 24 * 60 * 60)
```

## Imutabilidade (desafio)

- Utilizando Lambda
[Imutabilidade](./imutabilidade_v1.py)

- Utilizando Função
[Imutabilidade 2](./imutabilidade_v2.py)

- Modo Imperativo ( estrutural )
[Imutabilidade 3](./imutabilidade_v3.py)

- Funções Imutabilidade
[Funções Imutabilidade](./funcoes_imutabilidade_v1.py)
[Funções Imutabilidade v2](./funcoes_imutabilidade_v2.py)


## Generators

[Generators](./generators_v1.py)
[Generators](./generators_v2.py)

## Implementando Map

[Implementando Map v1](./implementando_map_v1.py)
[Implementando Map v2](./implementando_map_v2.py)

## Desafio Maior Divisor Comum

[Desafio - MDC](./desafio_mdc.py)