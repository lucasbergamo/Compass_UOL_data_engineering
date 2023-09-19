import pandas as pd

tabela = pd.read_csv(r"actors.csv")
maior_numero_filmes = tabela['Number of Movies'].max()
ator_com_maior_numero_filmes = tabela[tabela['Number of Movies'] == maior_numero_filmes]['Actor'].values[0]

print(f"O ator/atriz com maior número de filmes é {ator_com_maior_numero_filmes} com {maior_numero_filmes} filmes.")