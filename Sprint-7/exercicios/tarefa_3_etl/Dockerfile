FROM python:3.8

LABEL maintainer="Lucas Bérgamo"

RUN apt-get update && apt-get upgrade -y

RUN pip install boto3

WORKDIR /app

COPY . /app

CMD ["python", "script.py"]