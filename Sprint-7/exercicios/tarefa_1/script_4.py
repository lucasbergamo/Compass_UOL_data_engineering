import pandas as pd

tabela = pd.read_csv(r"actors.csv")

contagem_filmes = tabela['#1 Movie'].value_counts()
filmes_mais_frequentes = contagem_filmes[contagem_filmes == contagem_filmes.max()]
frequencia_mais_frequente = filmes_mais_frequentes.iloc[0]

print("Filme(s) mais frequente(s):")

for filme, frequencia in zip(filmes_mais_frequentes.index, filmes_mais_frequentes):
    print(f"Filme: {filme}, Frequência: {frequencia}")