FROM mongo:latest


ENV MONGO_INITDB_ROOT_USERNAME=mongoadmin
ENV MONGO_INITDB_ROOT_PASSWORD=secret

RUN mkdir -p /usr/src/app/data


COPY products.json /usr/src/app/data/
COPY init.js /docker-entrypoint-initdb.d/

RUN mongoimport --db mydatabase --collection mycollection --file COPY products.json /usr/src/app/data/products.json/
WORKDIR /usr/src/app

CMD ["mongod", "--auth"]

EXPOSE 27017
