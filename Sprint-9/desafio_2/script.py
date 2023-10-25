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


source_path = "s3://desafio-final-compass-uol/Trusted/Tmdb/PARQUET/2023/10/18/todos_filmes_drama_romance_tmdb.parquet"
current_date = datetime.now().strftime("%Y/%m/%d")
s3_refined_path = f"s3://desafio-final-compass-uol/Refined/Tmdb/PARQUET/{current_date}/"


df_filmes = spark.read.parquet(source_path)

# selecioando apenas as colunas relevantes

filmesdf = df_filmes.select("id", "genre_ids", "title", "release_date", "original_title", "original_language")

popularidadedf = df_filmes.select("id", "title", "popularity", "vote_average", "vote_count")

# criando tabelas

filmesdf.write.saveAsTable("fato_f")
popularidadedf.write.saveAsTable("dim_p")

# salvando os arquivos

filmesdf.write.parquet(s3_refined_path, mode="overwrite")
popularidadedf.write.parquet(s3_refined_path, mode="append")

job.commit()