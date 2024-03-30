mongod --auth &


sleep 30


mongoimport --db inventory --collection items --file /usr/src/app/data/products.json
