FROM node
#FROM node:14
WORKDIR /src

COPY package*.json .

RUN npm install
# utilizar . ou /app terá a mesma função pois o workdir já abre o arquivo app.js do diretório

COPY . .
# essa expresão significa: copia tudo que eu tenho aqui para o meu container

EXPOSE 3000

CMD ["node", "app.js"]
#comando para executar a aplicação, só funciona em listas []