FROM php:8-apache

WORKDIR /var/www/html/

COPY . .

EXPOSE 80

RUN chown -R www-data:www-data /var/www
# comando para dar a permissão para todos os arquivos a quem vai executar
# temos que usar ao utilizar apache