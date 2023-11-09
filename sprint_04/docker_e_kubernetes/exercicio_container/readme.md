```
FROM python:3

WORKDIR /app
# sempre que vou rodar python, executar dentro de app

COPY . .
# essa expresão significa: copia tudo que eu tenho na pasta direcionada do workdir para o meu container

EXPOSE 3000

CMD ["python", "app/carguru.py"]
#comando para executar a aplicação, só funciona em listas []
```


1- 




2- Buildando imagem
 ```docker build -t carguru_image .```
 # o "." significa que quero levar tudo da pasta para a imagem

3- Rodando a imagem no terminal
 ```docker run -it carguru_image```
 # quando rodei, o pc lagou e retornou a seguinte mensagem: 
 # Você deve dirigir um Chevrolet Agile


-------

Sim, utilizamos o ```docker start <container>``` ou 

```docker start -it <container>```, para rodar no terminal.