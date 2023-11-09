import requests
import json
import boto3
from datetime import datetime

# Sua chave de API do TMDb
api_key = ""

# URL base da API
url = "https://api.themoviedb.org/3/discover/movie"

# Parâmetros da consulta para a primeira página
params = {
    "api_key": api_key,
    "with_genres": "18,10749",  # Gêneros Drama (18) e Romance (10749)
    "page": 1  # Buscar apenas a primeira página
}

pagina_atual = 1
todos_filmes = []

while True:
    response = requests.get(url, params=params)
    data = response.json()

    # Verifique se há filmes nesta página
    resultados = data.get("results", [])

    if not resultados:
        # Se não houver mais resultados, saia do loop
        break

    todos_filmes.extend(resultados)

    # Avance para a próxima página
    params["page"] += 1

    print(f"Página: {pagina_atual} , quantidade de filmes processados: {len(todos_filmes)}")
    pagina_atual += 1


print(f"Total de páginas processadas: {pagina_atual - 1}")
# Imprima o número de filmes encontrados na primeira página

print(f"Total de filmes encontrados: {len(todos_filmes)}")

# Nome do arquivo onde você deseja salvar os resultados
nome_arquivo = "todos_filmes_drama_romance_tmdb.json"

s3 = boto3.client('s3')

caminho_arquivo_s3 = f"Raw/Tmdb/JSON/{datetime.now().strftime('%Y/%m/%d')}/{nome_arquivo}"

s3.put_object(
    Bucket='desafio-final-compass-uol',
    Key=caminho_arquivo_s3,
    Body=json.dumps(todos_filmes, ensure_ascii=False, indent=4),
    ContentType='application/json'
)

print("Requisição armazenada com sucesso no Amazon S3!")
