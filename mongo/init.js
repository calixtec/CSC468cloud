
var adminDB = db.getSiblingDB('admin');


var inventoryDB = db.getSiblingDB('inventory');
inventoryDB.createCollection('items');


adminDB.createUser({
    user: "mongoadmin2",
    pwd: "password",
    roles: [{ role: "readWrite", db: "inventory" }]
});


