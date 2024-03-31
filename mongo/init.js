var inventoryDB = db.getSiblingDB('inventory');
inventoryDB.createCollection('items');

inventoryDB.createUser({
    user: "mongoadmin2",
    pwd: "password",
    roles: [{ role: "readWrite", db: "inventory" }]
});
