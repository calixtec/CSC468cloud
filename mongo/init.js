db.createUser({
    user: "mongoadmin",
    pwd: "secret",
    pwd: "password",
    roles: [{ role: "root", db: "admin" },{ role: "root", db: "inventory" }]
});

db = db.getSiblingDB('inventory');
db.createCollection('items');



