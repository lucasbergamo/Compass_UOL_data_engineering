1. criei um crawler que vai mapear a pasta trusted no bucket s3
2. após criar o crawler, definir a role, criar o database, verificar os dados
3. agora irei criar a modelagem multidimensional


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



- entender os dados, trazer  por exemplo os melhors 5 filmes por década e atingir um público alvo específico, pegar bilheteria

- imdb pro para puxar dadops de bilheteria, como seria a ingestão?

- pode realizar webscraping?


- job que estava tentando realizar no glue
  
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# definindo a tabela Trusted como um DynamicFrame

trusted_dyf = glueContext.create_dynamic_frame.from_catalog(
    database = "trusted-data",  # nome banco de dados
    table_name = "trusted"  # nome da tabela Trusted
)



# seleciondo apenas as colunas relevantes

selected_filmes = trusted_dyf.select_fields(["id", "genre_ids", "popularity", "title", "vote_average", "vote_count", "original_title", "original_language"])

selected_popularidade = trusted_dyf.select_fields(["id", "popularity", "title", "vote_average", "vote_count", "original_title", "original_language"])

# convertendo o DynamicFrame em DataFrame

trusted_df = selected_filmes.toDF()

# tabelas para as dimensões e a fato

trusted_df.createOrReplaceTempView("fato_filmes")  # Tabela fato

trusted_df.createOrReplaceTempView("dim_filme")  # Tabela dimensão

trusted_df.createOrReplaceTempView("dim_popularidade")  # Tabela dimensão

# Views para as dimensões

spark.sql("""
    CREATE OR REPLACE VIEW vw_dim_filme AS
    SELECT id, title
    FROM dim_filme
""")

spark.sql("""
    CREATE OR REPLACE VIEW vw_dim_popularidade AS
    SELECT id, title
    FROM dim_popularidade
""")

job.commit()