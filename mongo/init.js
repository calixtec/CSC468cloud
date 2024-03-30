db.createUser({
    user: "mongoadmin",
    pwd: "password",
    roles: [{ role: "root", db: "admin" }]
});

db = db.getSiblingDB('inventory');

db.createCollection('items');
