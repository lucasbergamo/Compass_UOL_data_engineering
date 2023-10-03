import requests
import json


api_key = ""

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

response = requests.get(url)
data = response.json()

nome_arquivo = "dados_tmdb_com_ident_4_e_todos.json"


with open(nome_arquivo, "w", encoding="utf-8") as arquivo_json:
    json.dump(data, arquivo_json, ensure_ascii=False, indent=4)
