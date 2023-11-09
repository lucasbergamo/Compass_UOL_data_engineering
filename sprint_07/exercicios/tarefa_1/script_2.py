import pandas as pd

tabela = pd.read_csv(r"actors.csv")

media_numero_filmes = tabela['Number of Movies'].mean()

print(f"A média do número de filmes é: {media_numero_filmes:.2f}")