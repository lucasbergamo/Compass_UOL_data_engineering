import requests
import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')

bucket_name = 'desafio-final-compass-uol'

storage_layer = 'Raw/TMDB/JSON'

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

    
    # Se a lista de filmes atingir 100 registros, salve em um arquivo separado
    if len(todos_filmes) >= 100:
        nome_arquivo = f"filmes_drama_romance_pagina_{pagina_atual - 1}.json"

        with open(nome_arquivo, "w", encoding="utf-8") as arquivo_json:
            json.dump(todos_filmes, arquivo_json, ensure_ascii=False, indent=4)

        s3.upload_file(nome_arquivo, 'desafio-etl', nome_arquivo)

        # Limpe a lista de filmes
        todos_filmes = []

# Avance para a próxima página
    params["page"] += 1

    print(f"Página {pagina_atual} processada com sucesso! ")
    pagina_atual += 1

# Verifique se ainda há alguns filmes restantes não salvos
if todos_filmes:
    nome_arquivo = f"filmes_drama_romance_pagina_{pagina_atual}.json"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo_json:
        json.dump(todos_filmes, arquivo_json, ensure_ascii=False, indent=4)

    s3.upload_file(nome_arquivo, 'desafio-etl', nome_arquivo)

print(f"Total de páginas processadas: {pagina_atual - 1}")

# Imprimir o número de filmes encontrados na primeira página
print(f"Total de filmes encontrados: {pagina_atual * 20}")
print("Requisição armazenada com sucesso!")

