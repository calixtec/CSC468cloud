#!/bin/bash

read -sp "Enter MongoDB password: " MONGO_PASSWORD
echo

mongo -u <admin_username> -p "$MONGO_PASSWORD" &

sleep 10


mongoimport --db inventory --collection items --file /usr/src/app/data/products.json
exec "$@"
