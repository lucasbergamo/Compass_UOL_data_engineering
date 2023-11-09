import random
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import when, rand, udf
from pyspark.sql.types import StringType


spark = SparkSession \
    .builder \
    .master("local[*]")\
    .appName("Exercicio Intro") \
    .getOrCreate()


# 1

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes.show(5)

# 2

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

df_nomes.show(10)

# 3

df_nomes = df_nomes.withColumn("Escolaridade",
                               when(rand() < 0.33, "Fundamental")
                               .when(rand() < 0.66, "Médio")
                               .otherwise("Superior"))

df_nomes.show(10)

# 4

paises_america_do_sul = ["Brasil", "Argentina", "Chile", "Colômbia", "Equador", "Peru", "Uruguai", "Paraguai", "Venezuela", "Bolívia", "Suriname", "Guiana", "Guiana Francesa"]
gerar_paises = lambda: random.choice(paises_america_do_sul)
gerar_paises_udf = spark.udf.register("gerar_pais", gerar_paises)
df_nomes = df_nomes.withColumn("Pais", gerar_paises_udf())

df_nomes.show(10)

# 5

df_nomes = df_nomes.drop("AnoNascimento")
df_nomes = df_nomes.withColumn("AnoNascimento",
                               when(rand() < 0.33, random.randrange(1945, 1980))
                               .when(rand() < 0.66, random.randrange(1981, 2000))
                               .otherwise(random.randrange(2001, 2010)))
df_nomes.show(10)

# 6

df_select = df_nomes.filter(df_nomes["AnoNascimento"] >= 2000)
df_select.show(10)

# 7 

df_nomes.createOrReplaceTempView("pessoas")
spark.sql("select * from pessoas where AnoNascimento >= 2000").show()

# 8 

contagem_millenials = df_nomes.filter((df_nomes["AnoNascimento"] >= 1980) & (df_nomes["AnoNascimento"] <= 1994)).count()
print(f"Quantidade de Millennials: , {contagem_millenials}")

# 9

query1 = "SELECT COUNT(*) FROM pessoas WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994"
contagem_millenials_sql = spark.sql(query1).collect()[0][0]
print("Quantidade de Millennials(Utilizando SparkSQL):", contagem_millenials_sql)

# 10

df_nomes.createOrReplaceTempView("pessoas")

generation_count = spark.sql(
    "SELECT Pais, " +
    "CASE " +
    "  WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers' " +
    "  WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X' " +
    "  WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials' " +
    "  WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z' " +
    "  ELSE 'Outros' " +
    "END AS Geracao, " +
    "COUNT(*) AS Quantidade " +
    "FROM pessoas " +
    "GROUP BY Pais, Geracao " +
    "ORDER BY Pais, Geracao"
)

generation_count.show()


