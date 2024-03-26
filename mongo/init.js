db.auth('root', 'password')
db = db.getSiblingDB('test-database')

db.createUser({
  user: 'root',
  pwd: 'password',
  roles: [
    {
      role: 'root',
      db: 'test-database',
    },
  ],
});
