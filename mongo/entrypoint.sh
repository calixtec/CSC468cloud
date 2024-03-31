#!/bin/bash

mongosh --username mongoadmin --password secret --authenticationDatabase admin /docker-entrypoint-initdb.d/init.js


mongod --auth &

sleep 10


mongoimport --db inventory --collection items --file /usr/src/app/data/products.json
exec "$@"
