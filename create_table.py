import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# INTEGER PRIMARY KEY : create auto increment column for id
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

connection.commit()
connection.close()
