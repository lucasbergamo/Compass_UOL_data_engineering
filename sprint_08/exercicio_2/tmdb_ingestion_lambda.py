import json
import requests
from datetime import datetime
import boto3
import time

def lambda_handler(event, context):
    
    tempo_inicio = time.time()
    
    secrets_manager_client = boto3.client('secretsmanager')
    secret_name = "chave_tmdb"
    
    try:
        
        secret_response = secrets_manager_client.get_secret_value(SecretId=secret_name)

        secret_dict = json.loads(secret_response['SecretString'])

        api_key = secret_dict['tmdb_key']

        url = "https://api.themoviedb.org/3/discover/movie"

        params = {
            "api_key": api_key,
            "with_genres": "18,10749",
            "page": 1
        }

    except Exception as e:
        print(f"Erro ao recuperar segredo do AWS Secrets Manager: {str(e)}")


    pagina_atual = 1
    todos_filmes = []
    
    while True:
        response = requests.get(url, params=params)
        data = response.json()
    
        resultados = data.get("results", [])
    
        if not resultados:
            break
    
        todos_filmes.extend(resultados)
    
        params["page"] += 1
    
        print(f"Página: {pagina_atual} , quantidade de filmes processados: {len(todos_filmes)}")
        pagina_atual += 1
    
    
    print(f"Total de páginas processadas: {pagina_atual - 1}")
    
    print(f"Total de filmes encontrados: {len(todos_filmes)}")
    
    s3 = boto3.client('s3')
    
    caminho_arquivo_s3 = f"Raw/Tmdb/JSON/{datetime.now().strftime('%Y/%m/%d')}"
    
    s3.put_object(
        Bucket='desafio-final-compass-uol',
        Key=caminho_arquivo_s3,
        Body=json.dumps(todos_filmes),
        ContentType='application/json'
    )
    
    tempo_fim = time.time()

    tempo_execucao_segundos = tempo_fim - tempo_inicio

    print("Requisição armazenada com sucesso!")

    print(f"Tempo de execução: {int(tempo_execucao_segundos)} segundos")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }