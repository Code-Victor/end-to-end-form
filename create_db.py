import sqlite3


db = sqlite3.connect("database.db")
db.execute("CREATE TABLE IF NOT EXISTS users (first_name TEXT, last_name TEXT)")
db.commit()
db.close()
