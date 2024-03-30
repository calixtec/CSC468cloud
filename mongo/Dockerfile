FROM mongo:latest

ENV MONGO_INITDB_ROOT_USERNAME=mongoadmin
ENV MONGO_INITDB_ROOT_PASSWORD=secret


COPY entrypoint.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/entrypoint.sh



COPY products.json /usr/src/app/
COPY init.js /docker-entrypoint-initdb.d/


WORKDIR /usr/src/app





EXPOSE 27017
