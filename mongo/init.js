db.createUser({
    user: "mongoadmin",
    pwd: "secret",
    roles: [{ role: "root", db: "admin" }]
});
