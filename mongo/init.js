db.createUser({
    user: "mongoadmin",
    pwd: "password",
    roles: [
        { role: "readWrite", db: "inventory" },
        { role: "root", db: "admin" }
    ]
})


