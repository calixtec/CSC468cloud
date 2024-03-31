var inventoryDB = db.getSiblingDB('inventory');
inventoryDB.createCollection('items');

inventoryDB.createUser({
    user: "mongoadmin2",
    pwd: "password",
    roles: [{ role: "readWrite", db: "inventory" }]
});

var productsJsonFilePath = "/usr/src/app/data/products.json";
var jsonData = load(productsJsonFilePath);
var result = db.items.insertMany(jsonData);
