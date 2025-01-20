# start

import sqlite3

# 9
db:str="05.01.25.db"

conn = sqlite3.connect(db)

cursor = conn.cursor()

# 1
cursor.execute("CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount INTEGER);")

# 2
cursor.execute('''INSERT INTO shopping (id, name,amount) VALUES
	(2, 'Milk', 2),
	(3, 'Bread', 3),
	(4, 'Chocolate', 8),
    (5, 'Bamba', 5),
    (6, 'Orange', 10)
''')

conn.commit()
# 3
cursor.execute("SELECT * FROM shopping")

rows = cursor.fetchall()

for i in rows:
   print(tuple(i))

# 4
cursor.execute("SELECT * FROM shopping WHERE amount > 5")
rows = cursor.fetchall()

for i in rows:
   print(tuple(i))

# 5
cursor.execute("DELETE from shopping WHERE name like 'Orange';")
conn.commit()

# cursor.execute('''UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'
# UPDATE shopping SET amount=1 WHERE name LIKE 'Milk''')

# 6
cursor.execute("UPDATE shopping SET name = ? WHERE name = ?"
                ,('Bisli','Bamba'))
conn.commit()

cursor.execute("UPDATE shopping SET amount = ? WHERE name = ?"
                ,(1,'Milk'))
conn.commit()

# 7
cursor.execute("SELECT COUNT(*)from shopping")

# 8
cursor.execute("SELECT * FROM shopping WHERE id > 0")
rows = cursor.fetchall()

for i in rows:
   print(tuple(i))
