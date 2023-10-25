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

