db.createUser({
    user: "mongoadmin",
    pwd: "secret",
    pwd: "password",
    roles: [{ role: "root", db: "admin" }]
});
