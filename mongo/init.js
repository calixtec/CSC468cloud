// var inventoryDB = db.getSiblingDB('inventory');
// inventoryDB.createCollection('items');

// inventoryDB.createUser({
//     user: "mongoadmin2",
//     pwd: "password",
//     roles: [{ role: "readWrite", db: "inventory" }]
// });
// var products = [
//     { product: "headphones", price: 20, date: "March 30, 2024" },
//     { product: "macbook", price: 1000, date: "March 30, 2024" },
//     { product: "mouses", price: 15, date: "March 30, 2024" }
// ];

// var result = db.items.insertMany(products);


var inventoryDB = db.getSiblingDB('inventory');

// Check if the collection exists
if (!inventoryDB.items) {
    inventoryDB.createCollection('items');
}

// Check if the collection is empty
if (inventoryDB.items.count() === 0) {
    inventoryDB.createUser({
        user: "mongoadmin2",
        pwd: "password",
        roles: [{ role: "readWrite", db: "inventory" }]
    });

    var products = [
        { product: "headphones", price: 20, date: "March 30, 2024" },
        { product: "macbook", price: 1000, date: "March 30, 2024" },
        { product: "mouses", price: 15, date: "March 30, 2024" }
    ];

    var result = db.items.insertMany(products);
    print("Data inserted successfully.");
} else {
    print("Collection 'items' is not empty. Data insertion skipped.");
}
