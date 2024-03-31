db.createUser({
    user: "mongoadmin2",
    pwd: "secret",
    roles: [
        { role: "root", db: "admin" },
        { role: "dbOwner", db: "inventory" }
    ]
    
});

db = db.getSiblingDB('inventory');
db.createCollection('items');



