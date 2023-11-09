
script 1: 

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime #importando datetime
from pyspark.sql.functions import to_date, date_format # importando função de datatype

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_path_1 = "s3://desafio-final-compass-uol/Refined/Tmdb/PARQUET/2023/10/25/part-00000-ae161d33-7df3-4b7a-a88e-c404c3e1634d-c000.snappy.parquet"
source_path_2 = "s3://desafio-final-compass-uol/Refined/Tmdb/PARQUET/2023/10/25/part-00000-8c14bba4-0a8a-43a8-b486-e337aef0b4c9-c000.snappy.parquet"

current_date = datetime.now().strftime("%Y/%m/%d")

s3_refined_path = f"s3://desafio-final-compass-uol/Refined/Tmdb/PARQUET/{current_date}/"

df_filmes = spark.read.parquet(source_path_1)
df_popularidade = spark.read.parquet(source_path_2)

# alterando nome das colunas

filmesdf = df_filmes.selectExpr("id", "genre_ids AS ids_genero", "title AS titulo", "release_date AS data_lancamento", "original_title AS titulo_original", "original_language AS nacionalidade")

popularidadedf = df_popularidade.selectExpr("id", "title AS titulo", "popularity AS popularidade", "vote_average AS media_votos ", "vote_count AS total_votos")

# alterando datatype de string para data

filmesdf = filmesdf.withColumn("data_lancamento", to_date(filmesdf["data_lancamento"], "yyyy-MM-dd"))
filmesdf = filmesdf.withColumn("data_lancamento", date_format(filmesdf["data_lancamento"], "dd-MM-yyyy"))

# salvando as tabelas

filmesdf.write.saveAsTable("refined-data.fato_filmes")
popularidadedf.write.saveAsTable("refined-data.dim_popularidade")

# salvando os arquivo no bucket s3

# filmesdf.write.parquet(s3_refined_path, mode="overwrite")
# popularidadedf.write.parquet(s3_refined_path,  mode="append")

# Trabalhando diretamente com um banco especifico

# spark.sql("USE refined-data")  # Define o banco de dados padrão como "refined-data"

# Agora, você pode consultar tabelas em "refined-data" sem especificar o banco de dados
# spark.sql("SELECT * FROM fato_filmes")
# spark.sql("SELECT * FROM dim_popularidade")

job.commit()



codigo 2 : 

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import to_date, date_format # importando função de datatype

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_path_1 = "s3://desafio-final-compass-uol/Refined/Tmdb/PARQUET/2023/10/25/part-00000-ae161d33-7df3-4b7a-a88e-c404c3e1634d-c000.snappy.parquet"
source_path_2 = "s3://desafio-final-compass-uol/Refined/Tmdb/PARQUET/2023/10/25/part-00000-8c14bba4-0a8a-43a8-b486-e337aef0b4c9-c000.snappy.parquet"

df_filmes = spark.read.parquet(source_path_1)
df_popularidade = spark.read.parquet(source_path_2)

# alterando nome das colunas

filmesdf = df_filmes.selectExpr("id", "genre_ids AS ids_genero", "title AS titulo", "release_date AS data_lancamento", "original_title AS titulo_original", "original_language AS nacionalidade")

popularidadedf = df_popularidade.selectExpr("id", "title AS titulo", "popularity AS popularidade", "vote_average AS media_votos ", "vote_count AS total_votos")

# alterando datatype de string para data

filmesdf = filmesdf.withColumn("data_lancamento", to_date(filmesdf["data_lancamento"], "yyyy-mm-dd"))
filmesdf = filmesdf.withColumn("data_lancamento", date_format(filmesdf["data_lancamento"], "dd-mm-yyyy"))

# salvando as tabelas

filmesdf.write.saveAsTable("refined-data.fato_filmes")
popularidadedf.write.saveAsTable("refined-data.dim_popularidade")

job.commit()



codigo 3 : o erro estava ai indicar o nome do arquivo, quando ele vira tabela fica com _
part_00000_ae161d33_7df3_4b7a_a88e_c404c3e1634d_c000_snappy_parquet


import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import to_date, date_format

## @params: [JOB_NAME]

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

spark.sql("ALTER TABLE refined-data.part_00000_ae161d33_7df3_4b7a_a88e_c404c3e1634d_c000_snappy_parquet RENAME TO refined-data.fato_filmes")
print("Tabela 'fato_filmes' renomeada com sucesso")

spark.sql("ALTER TABLE refined-data.part_00000_8c14bba4_0a8a_43a8_b486_e337aef0b4c9_c000_snappy_parquet RENAME TO refined-data.dim_popularidade")
print("Tabela 'dim_popularidade' renomeada com sucesso")

df_filmes = spark.table(f"refined-data.fato_filmes")
df_popularidade = spark.table(f"refined-data.dim_popularidade")

# alterando nome das colunas

filmesdf = df_filmes.selectExpr("id", "genre_ids AS ids_genero", "title AS titulo", "release_date AS data_lancamento", "original_title AS titulo_original", "original_language AS nacionalidade")

print("Colunas selecionadas em 'filmesdf'")

popularidadedf = df_popularidade.selectExpr("id", "title AS titulo", "popularity AS popularidade", "vote_average AS media_votos ", "vote_count AS total_votos")

print("Colunas selecionadas em 'popularidadedf'")


# alterando datatype de string para data

filmesdf = filmesdf.withColumn("data_lancamento", to_date(filmesdf["data_lancamento"], "yyyy-mm-dd"))
filmesdf = filmesdf.withColumn("data_lancamento", date_format(filmesdf["data_lancamento"], "dd-mm-yyyy"))

print("Tipo de data alterado em 'filmesdf'")

# salvando as tabelas

filmesdf.write.saveAsTable(f"refined-data.fato_filmes")
popularidadedf.write.saveAsTable(f"refined-data.dim_popularidade")

job.commit()

O erro indica que a identificação "refined-data" não está sendo reconhecida da maneira que você a usou na instrução SQL. Em SQL, se você usar um identificador que contém caracteres especiais ou espaços, é uma boa prática colocá-lo entre aspas ou entre crases, dependendo do banco de dados. No AWS Glue ETL, você deve usar crases para delimitar identificadores.



codigo 4 


import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import to_date, date_format

## @params: [JOB_NAME]

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

spark.sql("USE refined_data")

# Copie os dados da tabela antiga para a nova tabela "fato_filmes"
df_filmes = spark.table("part_00000_ae161d33_7df3_4b7a_a88e_c404c3e1634d_c000_snappy_parquet")

# Copie os dados da tabela antiga para a nova tabela "dim_popularidade"
df_popularidade = spark.table("part_00000_8c14bba4_0a8a_43a8_b486_e337aef0b4c9_c000_snappy_parquet")

# alterando nome das colunas

filmesdf = df_filmes.selectExpr("id", "genre_ids AS ids_genero", "title AS titulo", "release_date AS data_lancamento", "original_title AS titulo_original", "original_language AS nacionalidade")

print("Colunas selecionadas em 'filmesdf'")

popularidadedf = df_popularidade.selectExpr("id", "title AS titulo", "popularity AS popularidade", "vote_average AS media_votos ", "vote_count AS total_votos")

print("Colunas selecionadas em 'popularidadedf'")

# alterando datatype de string para data

filmesdf_2 = filmesdf.withColumn("data_lancamento", to_date(filmesdf["data_lancamento"], "yyyy-MM-dd"))
filmesdf_3 = filmesdf_2.withColumn("data_lancamento", date_format(filmesdf["data_lancamento"], "dd-MM-yyyy"))

print("Tipo de data alterado em 'filmesdf'")

# salvando as tabelas

filmesdf_3.write.saveAsTable("fato_filmes")
popularidadedf.write.saveAsTable("dim_popularidade")

filmesdf_3.show(10)
popularidadedf.show(10)

filmesdf_3.printSchema()
popularidadedf.printSchema()

print("Tabela salva")

job.commit()


codigo 5 : 

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import to_date, date_format
from datetime import datetime

## @params: [JOB_NAME]

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

spark.sql("CREATE DATABASE IF NOT EXISTS refined_data")


source_path_1 = "s3://desafio-final-compass-uol/Refined/Tmdb/PARQUET/2023/10/25/part-00000-ae161d33-7df3-4b7a-a88e-c404c3e1634d-c000.snappy.parquet"
source_path_2 = "s3://desafio-final-compass-uol/Refined/Tmdb/PARQUET/2023/10/25/part-00000-8c14bba4-0a8a-43a8-b486-e337aef0b4c9-c000.snappy.parquet"

current_date = datetime.now().strftime("%Y/%m/%d")

s3_refined_path = f"s3://desafio-final-compass-uol/Refined/Tmdb/PARQUET/{current_date}/"

df_filmes = spark.read.parquet(source_path_1)

df_popularidade = spark.read.parquet(source_path_2)

# alterando nome das colunas

filmesdf = df_filmes.selectExpr("id", "genre_ids AS ids_genero", "title AS titulo", "release_date AS data_lancamento", "original_title AS titulo_original", "original_language AS nacionalidade")

print("Colunas selecionadas em 'filmesdf'")

popularidadedf = df_popularidade.selectExpr("id", "title AS titulo", "popularity AS popularidade", "vote_average AS media_votos ", "vote_count AS total_votos")

print("Colunas selecionadas em 'popularidadedf'")

# alterando datatype de string para data

filmesdf = filmesdf.withColumn("data_lancamento", to_date(filmesdf["data_lancamento"], "yyyy-MM-dd"))
filmesdf = filmesdf.withColumn("data_lancamento", date_format(filmesdf["data_lancamento"], "dd-MM-yyyy"))

print("Tipo de data alterado em 'filmesdf'")

# salvando as tabelas

filmesdf.write.saveAsTable("fato_filmes")
popularidadedf.write.saveAsTable("dim_popularidade")

filmesdf.show(10)
popularidadedf.show(10)

filmesdf.printSchema()
popularidadedf.printSchema()

print("Tabela salva")

filmesdf.write.parquet(s3_refined_path, mode="overwrite")
popularidadedf.write.parquet(s3_refined_path,  mode="overwrite")

print("arquivos salvos no s3")
job.commit()