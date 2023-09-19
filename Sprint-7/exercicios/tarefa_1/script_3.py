import pandas as pd

tabela = pd.read_csv(r"actors.csv")

maior_media_filme = tabela['Average per Movie'].max()
ator_com_maior_media_filme = tabela[tabela['Average per Movie'] == maior_media_filme]['Actor'].values[0]

print(f"O ator/atriz com a maior média por filme é {ator_com_maior_media_filme} com uma média de {maior_media_filme:.2f}")