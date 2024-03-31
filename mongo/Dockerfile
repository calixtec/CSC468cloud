FROM mongo:latest



ENV MONGO_INITDB_ROOT_USERNAME=mongoadmin
ENV MONGO_INITDB_ROOT_PASSWORD=secret






WORKDIR /usr/src/app
COPY products.json /usr/src/app/data/

COPY entrypoint.sh /usr/src/app/
COPY init.js /docker-entrypoint-initdb.d/
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

EXPOSE 27017


