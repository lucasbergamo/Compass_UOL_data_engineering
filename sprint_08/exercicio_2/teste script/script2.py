import requests
import json
import time

tempo_inicio = time.time()

# chave de API do TMDb
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

    # Verificar se há filmes nesta página
    resultados = data.get("results", [])

    if not resultados:
        # Se não houver mais resultados, saia do loop
        break

    todos_filmes.extend(resultados)

    # Avançar para a próxima página
    params["page"] += 1

    print(f"Página: {pagina_atual} , quantidade de filmes processados: {len(todos_filmes)}")
    pagina_atual += 1


print(f"Total de páginas processadas: {pagina_atual - 1}")
# Imprimir o número de filmes encontrados na primeira página

print(f"Total de filmes encontrados: {len(todos_filmes)}")

# Nome do arquivo para salvar os resultados
nome_arquivo = "filmes_drama_romance4.json"

# Salvar os resultados no arquivo JSON
with open(nome_arquivo, "w", encoding="utf-8") as arquivo_json:
    json.dump(todos_filmes, arquivo_json, ensure_ascii=False, indent=4)

tempo_fim = time.time()

tempo_execucao_segundos = tempo_fim - tempo_inicio

print("Requisição armazenada com sucesso!")

print(f"Tempo de execução: {int(tempo_execucao_segundos)} segundos")