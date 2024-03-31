var inventoryDB = db.getSiblingDB('inventory');
inventoryDB.createCollection('items');

inventoryDB.createUser({
    user: "mongoadmin2",
    pwd: "password",
    roles: [{ role: "readWrite", db: "inventory" }]
});

var productsJsonFilePath = '/usr/src/app/data/products.json';
var importResult = inventoryDB.items.insertMany(
    JSON.parse(cat(productsJsonFilePath))
);
