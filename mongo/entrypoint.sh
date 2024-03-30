!/bin/bash
mongod --auth &


sleep 10


mongoimport --db inventory --collection items --file /usr/src/app/data/products.json
