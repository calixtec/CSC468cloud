db.createUser({
    user: "mongoadmin",
    pwd: "password",
    roles: [{ role: "root", db: "admin" }]
});
