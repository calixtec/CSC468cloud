FROM mongo:latest


ENV MONGO_INITDB_ROOT_PASSWORD=password

COPY init.js /docker-entrypoint-initdb.d/

CMD mongosh -u $MONGO_USERNAME -p $MONGO_PASSWORD --authenticationDatabase $MONGO_AUTH_DATABASE
