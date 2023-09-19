import boto3
from datetime import datetime

data = datetime.now().strftime('%Y-%m-%d')

series_files = 'series.csv'
movies_files = 'movies.csv'
series_dir = f'Raw/Local/CSV/Series/{data}/series.csv'
movies_dir = f'Raw/Local/CSV/Movies/{data}/movies.csv'

aws_access_key = 'ops'
aws_secret_key = 'ops'
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