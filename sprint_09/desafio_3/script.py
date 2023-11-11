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

# selecionado apenas as colunas relevantes

fatodf = df_filmes.select("id_filme", "id_atores", "id_equipe", "id_diretores", "id_popularidade")

popularidadedf = df_filmes.select("id_popularidade", "filmes", "avaliacao_media", "votos_totais")

diretoresdf = df_filmes.select("id_diretores", "nome_diretor", "ano_nascimento", "ano_falecimento")

atoresdf = df_filmes.select("id_atores", "filmes", "nome_ator", "nome_personagem", "ano_nascimento", "ano_falecimento")

filmesdf = df_filmes.select("id_filme", "filmes", "ano_lancamento", "duracao", "genero")

equipedf = df_filmes.select("id_equipe", "filmes", "nome_equipe", "profissao")

# criando tabelas e salvando os arquivos

fatodf.coalesce(1).write.saveAsTable(name="fato_filmes", mode="overwrite", path=s3_refined_path, format="parquet")

popularidadedf.coalesce(1).write.saveAsTable(name="dim_popularidade", mode="overwrite", path=s3_refined_path, format="parquet")

diretoresdf.coalesce(1).write.saveAsTable(name="dim_diretores", mode="overwrite", path=s3_refined_path, format="parquet")

atoresdf.coalesce(1).write.saveAsTable(name="dim_atores", mode="overwrite", path=s3_refined_path, format="parquet")

filmesdf.coalesce(1).write.saveAsTable(name="dim_filmes", mode="overwrite", path=s3_refined_path, format="parquet")

equipedf.coalesce(1).write.saveAsTable(name="dim_equipe", mode="overwrite", path=s3_refined_path, format="parquet")


job.commit()