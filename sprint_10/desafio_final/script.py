df_filmes = spark.read.parquet(source_path_1)
df_popularidade = spark.read.parquet(source_path_2)

# alterando nome das colunas

filmesdf = df_filmes.selectExpr("id", "genre_ids AS ids_genero", "title AS titulo", "release_date AS data_lancamento", "original_title AS titulo_original", "original_language AS nacionalidade")

popularidadedf = df_popularidade.selectExpr("id", "title AS titulo", "popularity AS popularidade", "vote_average AS media_votos ", "vote_count AS total_votos")

# alterando datatype de string para data e formato

filmesdf = filmesdf.withColumn("data_lancamento", to_date(filmesdf["data_lancamento"], "yyyy-MM-dd"))
filmesdf = filmesdf.withColumn("data_lancamento", date_format(filmesdf["data_lancamento"], "dd-MM-yyyy"))

# salvando as tabelas

filmesdf.write.saveAsTable("fato_filmes")
popularidadedf.write.saveAsTable("dim_popularidade")

filmesdf.write.parquet(s3_refined_path, mode="overwrite")
popularidadedf.write.parquet(s3_refined_path,  mode="overwrite")