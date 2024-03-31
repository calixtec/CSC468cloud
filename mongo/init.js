

db = db.getSiblingDB('inventory');
db.createCollection('items');

use admin;

db.createUser({
    user: "mongoadmin1",
    pwd: "password", 
    roles: [{ role: "readWrite", db: "inventory" }]
});


