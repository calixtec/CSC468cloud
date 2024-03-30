mongod --auth &


sleep 5


mongoimport --db inventory --collection items --file /usr/src/app/data/products.json --jsonArray
