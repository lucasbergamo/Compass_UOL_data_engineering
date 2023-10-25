from pyspark.sql.functions import *

filmes.select("id", "popularity", "genre_id").where ((Func.col("popularity") > 5) & (Func.col("genre_id") > 18)).show()


filmes2 = spark.read.load("/home/hadoop/teste/todos_filmes_drama_romance_tmdb.parquet", header=False, format="parquet", inferSchema=True)

novodf = filmes.withColumnRenamed("id", "ids")
novodf.columns

- exportando

dffilmes.write.format("parquet").save("/home/lucas/dfimport.parquet")


- importando

mudnado nome do arquivo
mv nomedoarquivo novonome.parquet

nododf = spark.read.format("parquet").load("/home/lucas/novonome.parquet")
novodf.show()
novodf.schema

/home/hadoop/teste

fornecendo schema =

nododf = spark.read.format("parquet").load("/home/lucas/novonome.parquet", schema=meuschema)



- Abrindo arquivo = gedit nomedoarquivo

filmes3 = filmes2.withColumn("data2", to_timestamp(Func.col("data"), "YYYY-MM-DD"))

filmes3.select("nome", year("data")).orderBy("nome").show()

filmes2.take(1)




- order by 

filmes.show()

filmes.orderBy(Func.col("vendas").desc()).show()

filmes.orderBy(Func.col("vendas").desc(), Func.col("cidade").desc()).show()



- Group by 

filmes.groupBy("cidade").agg(sum("vendas")).show()

filmes.groupBy("cidade").agg(sum("vendas")).orderBy(Func.col("sum(vendas)").desc()).show()

filmes.filter(Func.col("nome") == "deolinda vilela").show()



filmes.select("id", "popularity")

dfnovo = filmes.select("id", "popularity")

dfnovo2 = clientes.select("*").where((Func.col("status")=="gold") | (Func.col("status")=="platinum"))


JOINS

vendas.join(clientes, vendas.ClienteID == clientes.ClienteID).groupBy(clientes.status).agg(sum("total")).orderBy(Func.col("sum(Total)").desc())



1- vou ler o arquivo parquet e importar em um df
2 - vou pegar esse df e selecionar oq euy dewsejo e colocar em outro df
3 - vou pegar esse df e exportar como parquet


spark sql

podemos transformar um df em tabela

from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark.sql("show databases").show()

spark.sql("create database compass")

spark.sql("use compass").show()

- criando schema

meuschema = "id INT, nome STRING, status STRING, cidade STRING, vendas INT, data STRING"

despachantes = spark.read.parquet("/home/lucas/filmes_tmdb.parquet", header=False, schema=arqschema)

- criando tabela a partir de um DF

para transformarmos um df em uma tabela usamos o comando save as table
**criamos a tabela para persistir os dados, já que os dataframes somem quando a sessão do pyspark é encerrada**

filmes.write.saveAsTable("filmes")

- verificando tabelas

spark.sql("select * from filmes").show()
spark.sql("show tables").show()


- Append para adicionar itens ou overwrite para sobescrever a tabela

filmes.write.mode("overwrite").saveAsTable("filmes")

- criando tabela externa

filmes.write.option("path", "home/lucas/filmes").saveAsTable("filmes2")

- se existir um caminho físico para a tabela, ela é externa

spark.sql("show create table filmes").show(truncate=False)
spark.sql("show create table filmes2").show(truncate=False)

spark.catalog.listTables()


* VIEWS OU ALIAS

- view temporaria

filmes.createOrReplaceTempView("filmes_vw")
spark.sql("select * from filmes_vw").show()

- view global

filmes.createOrReplaceGlobalTempView("filmes_vw")
spark.sql("select * from global_temp.filmes_vw").show()


spark.sql("CREATE OR REPLACE TEMP VIEW FILMES_VW AS select * from filmes")
spark.sql("CREATE OR REPLACE GLOBAL TEMP VIEW FILMES_VW AS select * from filmes")
spark.sql("select * from FILMES_VW").show()
spark.sql("select * from global_temp.FILMES_VW").show()


* df x tabelas sql

from pyspark.sql import functions as Func
from pyspark.sql.functions import *


1. 
spark.sql("select * from filmes").show()

x

despachantes.show()



2. 

spark.sql("select nome, vendas from filmes").show()

x

filmes.select("nome", "vendas").show()

3. 

spark.sql("select nome, vendas from filmes where votos > 20").show()

x

filmes.select("nome", "vendas").where(Func.col("votos") > 20).show()


4. 

spark.sql("select cidade, sum(vendas) from filmes group by cidade order by 2 desc").show()

x

filmes.groupBy("cidade").agg(sum("vendas")).orderBy(Func.col("sum(vendas)").desc()).show()


* JOINS

recschema = "idred INT, datarec STRING, iddesp INT"

reclamacoes = spark.read.parquet("/home/lucas/reclamacoes.parquet", header=False, schema = recschema)

reclamacoes.show()

reclamacoes.write.saveAsTable("reclamacoes")

1. 




adult
boolean

backdrop_path
string

genre_ids
array<bigint>

id,original_language,original_title,overview,popularity,poster_path,release_date,title,video,vote_average,vote_count