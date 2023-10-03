import requests
import json

# Sua chave de API do TMDb
api_key = ""

# URL base da API
base_url = "https://api.themoviedb.org/3/discover/movie"

# Parâmetros da consulta
params = {
    "api_key": api_key,
    "with_genres": "18,10749",  # Gêneros Drama (18) e Romance (10749)
    "page": 1  # Comece na página 1
}

# Lista para armazenar todos os resultados
todos_filmes = []


pagina_atual = 1

while True:
    response = requests.get(base_url, params=params)
    data = response.json()

    # Verifique se há filmes nesta página
    resultados = data.get("results", [])

    if not resultados:
        # Se não houver mais resultados, saia do loop
        break

    # Adicione os filmes desta página à lista
    todos_filmes.extend(resultados)

    # Avance para a próxima página
    params["page"] += 1

# Imprima o número da página atual para visualizar o progresso
print(f"Página {pagina_atual} processada")

pagina_atual = 1

nome_arquivo = "filmes_drama_romance.json"


with open(nome_arquivo, "w", encoding="utf-8") as arquivo_json:
    json.dump(todos_filmes, arquivo_json, ensure_ascii=False, indent=4)


# Agora todos_filmes contém todos os filmes com gêneros Drama e Romance
print(f"Total de filmes encontrados: {len(todos_filmes)}")