**Sumário**

[Retornar](https://github.com/lucasbergamo/Compass_UOL_data_engineering)

<details><summary><strong>Navegação</strong></summary>

- [Primeira Etapa - Sprint 7](#primeira-etapa---sprint-7)
  - [Implementar código Python:](#implementar-código-python)
  - [Dockerfile](#dockerfile)
  - [Script de ETL Python](#script-de-etl-python)
- [Segunda Etapa - Sprint 8](#segunda-etapa---sprint-8)
- [Terceira Etapa - Sprint 9](#terceira-etapa---sprint-9)
  - [Job glue ETL](#job-glue-etl)
  - [Modelagem de Dados da Camada Refined](#modelagem-de-dados-da-camada-refined)
  - [Processamento Refined Usando Glue](#processamento-refined-usando-glue)
  - [Querrys no aws athena](#querrys-no-aws-athena)
- [Etapa Final - Sprint 10](#etapa-final---sprint-10)
  - [Modelagem do desafio final](#modelagem-do-desafio-final)
  - [Pré processamento local](#pré-processamento-local)
- [Problema encontrado, startwith x col.filter](#problema-encontrado-startwith-x-colfilter)
  - [Dashboard](#dashboard)

</details>




# Primeira Etapa - Sprint 7


![Etapa 1](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/1_desafio_final.png)


## Implementar código Python

- ler os 2 arquivos (filmes e series) no formato CSV inteiros, ou seja, sem filtrar os dados

- utilizar a lib boto3 para carregar os dados para a AWS

- acessar a AWS e gravar no S3, no bucket definido com RAW Zone


1) Criar um container Docker com um volume para armazenar os arquivos CSV e executar o processo Python implementado.

2) Executar localmente o container docker para realizar a carga dos dados ao S3.

## Dockerfile

```
DOCKERFILE
 
FROM python:3.8
 
LABEL maintainer="Lucas Bérgamo"
 
RUN apt-get update && apt-get upgrade -y
 
RUN pip install boto3
 
WORKDIR /app
 
COPY . /app
 
CMD ["python", "script.py"]
```
 
## Script de ETL Python

 ```
import boto3
from datetime import datetime
 
data = datetime.now().strftime('%Y-%m-%d')
 
series_files = 'series.csv'
movies_files = 'movies.csv'
series_dir = f'Raw/Local/CSV/Series/{data}/series.csv'
movies_dir = f'Raw/Local/CSV/Movies/{data}/movies.csv'
 
aws_access_key = 'chave de acesso'
aws_secret_key = 'chave secreta'
region = 'us-east-1' 
nome_bucket = 'desafio-etl-1-lucas-uol'
 
s3 = boto3.client(
    service_name = 's3',
    aws_access_key_id = aws_access_key,
    aws_secret_access_key = aws_secret_key,
    region_name = region
)
 
s3.upload_file(movies_files, nome_bucket, series_dir)
s3.upload_file(series_files, nome_bucket, movies_dir)
 
print(f"{series_files} e {movies_files}, foram transferidos com sucesso para o bucket: {nome_bucket}, no Amazon S3.")
```

![Ingestão de dados no S3](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/img/1_upload_ok.png)



# Segunda Etapa - Sprint 8

![Etapa 2](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/2_desafio_final.png)

- Ingestão Batch através de uma requisição a API do TMDB, salvando o resultado no S3 Usando lambda.
- Dados salvos na camada RAW do Bucket do desafio-final

1. Criar um Secrets manager para salvar minha chave da API como parâmetro


![Secrets manager](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/img/2_secrets_manager.png)


2. Adicionar as Roles necessárias


![Roles Aws](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/img/3_roles_permission.png)


3.  Criar nova Layer (Request) no AWS Lambda necessárias à ingestão de dados, Boto3 ja é nativo.


![Layer AWS](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/img/1_requests_layer.png)



4. Script Python Localmente para testar a ingestão, adicionei prints e um tempo para ter uma resposta visual e uma noção do tempo médio que levaria o processo no lambda, para não gerar custos adicionais


```
import requests
import json
import time

tempo_inicio = time.time()

# Chave API do TMDb

api_key = ""

# URL base da API

base_url = "https://api.themoviedb.org/3/discover/movie"

# Parâmetros da consulta : Gêneros Drama (18) e Romance (10749), começando na página 1

params = {
    "api_key": api_key,
    "with_genres": "18,10749",  
    "page": 1
}

# Lista para armazenar todos os resultados

todos_filmes = []

pagina_atual = 1

while True:
    response = requests.get(base_url, params=params)
    data = response.json()

    # Verificando se há filmes nesta página
    resultados = data.get("results", [])

    # Se não houver mais resultados, saia do loop
    if not resultados:
        break

    # Adicionar os filmes desta página à lista

    todos_filmes.extend(resultados)

    # Avançar para a próxima página

    params["page"] += 1

# Imprimindo o número da página atual para visualizar o progresso

print(f"Página {pagina_atual} processada")

pagina_atual = 1

nome_arquivo = "filmes_drama_romance.json"

with open(nome_arquivo, "w", encoding="utf-8") as arquivo_json:
    json.dump(todos_filmes, arquivo_json, ensure_ascii=False, indent=4)

print(f"Total de filmes encontrados: {len(todos_filmes)}")
 
tempo_fim = time.time()
tempo_execucao_segundos = tempo_fim - tempo_inicio
print("Requisição armazenada com sucesso!")
print(f"Tempo de execução: {int(tempo_execucao_segundos)} segundos")

```


5. Agora modifiquei o Script para funcionar no Lambda



```
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
    
    caminho_arquivo_s3 = f"Raw/Tmdb/JSON/{datetime.now().strftime('%Y/%m/%d')}/"
    
    s3.put_object(
        Bucket='desafio-final-compass-uol',
        Key=caminho_arquivo_s3,
        Body=json.dumps(todos_filmes, ensure_ascii=False, indent=4),
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

```

![Código Lambda Executado](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/img/3_run_lambda.png)

- Tive problemas ao usar o ident=4 no json, melhora a visualização mas bugou ao consultar, pelo menos ao usar o ident=4 consegui visualizar os generos de drama e romance para solicitar apenas eles


4. Requisição feita a api do tmbd, usando lambda para salvar o request como json num bucket s3 para posterior análise

![Ingestão Batch no S3 Usando lambda](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/img/4_s3_ok.png)



# Terceira Etapa - Sprint 9

![Etapa 3](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/3_desafio_final.png)

- Criar um Job no Glue usando Pyspark para processar os arquivos JSON na raw, transformar e exportar como parquet para a Trusted


##  Job glue ETL

```
# encontrei problemas para salvar o arquivo com o nome correto, tentei inúmeras formas
# e não obtive sucesso, tive que renomear ele manualmente

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# entrada JSON

source_path = "s3://desafio-final-compass-uol/Raw/Tmdb/JSON/2023/10/18/*.json"

# saída PARQUET Trusted

current_date = datetime.now().strftime("%Y/%m/%d")
target_path = f"s3://desafio-final-compass-uol/Trusted/Tmdb/PARQUET/{current_date}/"

# Ler os dados JSON

df = spark.read.json(source_path)

# Salvar os dados Parquet

df.write.format("parquet").save(target_path)

job.commit()
```


## Processamento Refined Usando Glue


- criei o job glue para criar as tabelas e salvar o resultado na pasta Refined
- criei um database no glue chamado refined-data
- criei o crawler, selecionei a pasta Refined como target, selecionei a role, coloquei on-demand
- Rodei o crawler e foram adicionadas as tabelas no refined-data
- agora irei criar a modelagem multidimensional

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime
 
## @params: [JOB_NAME]
 
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
 
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
 
 
source_path = "s3://desafio-final-compass-uol/Trusted/Tmdb/PARQUET/2023/10/18/*.parquet"
current_date = datetime.now().strftime("%Y/%m/%d")
s3_refined_path = f"s3://desafio-final-compass-uol/Refined/Tmdb/PARQUET/{current_date}/"
 
 
df_filmes = spark.read.parquet(source_path)
 
# selecionando apenas as colunas relevantes
 
filmesdf = df_filmes.select("id", "genre_ids", "title", "release_date", "original_title", "original_language")
 
popularidadedf = df_filmes.select("id", "title", "popularity", "vote_average", "vote_count")
 
# criando tabelas
 
filmesdf.write.saveAsTable("fato_f")
popularidadedf.write.saveAsTable("dim_p")
 
# salvando os arquivos
 
filmesdf.coalesce(1).write.saveAsTable(name="fato_filmes",mode="overwrite",path=s3_refined_path',format="parquet")

popularidadedf.coalesce(1).write.saveAsTable(name="fato_filmes",mode="overwrite",path=s3_refined_path,format="parquet")

job.commit()

```

## Querrys no aws athena


```

CREATE TABLE fato_filmes AS
SELECT
    id,
    genre_ids,
    title,
    release_date,
    original_title,
    original_language
FROM trusted


CREATE TABLE dim_popularidade AS
SELECT
    id,
    title,
    popularity,
    vote_average,
    vote_count
FROM trusted
```

![Athena Tables and Views](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/img/athena_tables.png)


# Etapa Final - Sprint 10

- Criar Views e Abrir no Quicksight
- Modelagem do desafio final

## Modelagem do desafio final

## Modelagem de Dados da Camada Refined


![Schema](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/2_schema.jpeg)

![Modelagem Multidimensional](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/1_dimensao.jpeg)

![Querys](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/3_querrs.jpeg)

![starSchema](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/modelo%20de%20dados.jpg)

## Pré processamento local


1. fiz o download dos datasets do IMDB, https://developer.imdb.com/non-commercial-datasets/
   
2. acessei meu wsl 2 com todas as dependências necessárias para rodar o pyspark com jupyter notebook

- ```pip install jupyter```
- ```pip install findspark```
- ```jupyter notebook```

2. pré-processamento local

- [Jupyter Notebook 1](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/img/desafio_final.ipynb)

- [Jupyter Notebook 2](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/img/desafio_final_2.ipynb)


# Problema encontrado, startwith x col.filter

4. filtrando com startswith, ele retornará registros que contenham "actor" ou "actress" seguidos de outros caracteres. Isso resulta em mais registros, pois é mais abrangente.

```
nomes_df = nomes_df.filter(
    (nomes_df["primaryProfession"].startswith("ator")) |
    (nomes_df["primaryProfession"].startswith("atriz"))
)

atores_principais.show(10)
contagem_de_dados = atores_principais.count()
print(f"O DataFrame tem {contagem_de_dados} linhas (dados).")
```

- Ele não considerará registros que tenham caracteres adicionais após "actor" ou "actress", apenas aqueles que correspondem exatamente a essas palavras. Isso resulta em menos registros, pois é mais restritivo.

```
from pyspark.sql.functions import col

atores = names.filter((col("profissao") == "actor") | (col("profissao") == "actress"))

atores_principais.show(10)
contagem_de_dados = atores_principais.count()
print(f"O DataFrame tem {contagem_de_dados} linhas (dados).")
```

5. remover as opções "delimiter" e "header", pois essas opções são específicas para arquivos CSV e não são relevantes para arquivos Parquet.



## Dashboard


[Fimes Martin Scorsese](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/quicksight.pdf)

![Dashboard PNG](https://github.com/lucasbergamo/Compass_UOL_data_engineering/blob/main/sprint_10/desafio_final/dashboard_quicksight.png)












