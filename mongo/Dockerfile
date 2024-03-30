FROM mongo:latest


ENV MONGO_INITDB_ROOT_USERNAME=mongoadmin
ENV MONGO_INITDB_ROOT_PASSWORD=secret

RUN mkdir -p /usr/src/app/data


COPY products.json /usr/src/app/data/
COPY init.js /docker-entrypoint-initdb.d/
COPY entrypoint.sh /usr/src/app/entrypoint.sh


WORKDIR /usr/src/app

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

EXPOSE 27017
