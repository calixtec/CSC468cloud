#!/bin/bash

mongo --username $MONGO_INITDB_ROOT_USERNAME --password $MONGO_INITDB_ROOT_PASSWORD --authenticationDatabase admin /docker-entrypoint-initdb.d/init.js

mongod --auth &

sleep 10


mongoimport --db inventory --collection items --file /usr/src/app/data/products.json
exec "$@"
