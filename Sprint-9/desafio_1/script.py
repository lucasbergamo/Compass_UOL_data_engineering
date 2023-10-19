# encontrei problemas para salvar o arquivo com o nome correto, tentei inúmeras formas
# e não obtive sucesso, tive que renomear ele 

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

# entrada (JSON)
source_path = "s3://desafio-final-compass-uol/Raw/Tmdb/JSON/2023/10/18/todos_filmes_drama_romance_tmdb.json"

# saída (Parquet)
nome_arquivo = "todos_filmes_drama_romance_tmdb.parquet"
current_date = datetime.now().strftime("%Y/%m/%d")
target_path = f"s3://desafio-final-compass-uol/Trusted/Tmdb/PARQUET/{current_date}/{nome_arquivo}"

# Ler os dados JSON
df = spark.read.json(source_path)

# Salvar os dados Parquet
df.write.format("parquet").save(target_path)

job.commit()