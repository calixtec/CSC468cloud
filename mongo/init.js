db.createUser({
    user: "mongoadmin",
    pwd: "secret",
    roles: [
        { role: "root", db: "admin" },
        { role: "dbOwner", db: "inventory" }
    ]
    
});

db = db.getSiblingDB('inventory');
db.createCollection('items');



