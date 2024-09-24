import sqlite3

# 1. establish connection with the DB
conn = sqlite3.connect('DAIBatch2024.db')

# 2. create a cursor object
cursor = conn.cursor()

# 3. create a table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,name TEXT,age INTEGER)''')

# 4. Insert some data
cursor.execute("INSERT INTO users (name, age) VALUES ('Mayura',30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Mayuresh',25)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Sugandha',30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Srujan',25)")

# 5. cursor the data
conn.commit()
print("All Records\n")

# 6. Query the ORDER by
cursor.execute("SELECT * FROM users")
print("order by clause\n")
cursor.execute("SELECT * FROM users ORDER BY age")
print("=====================================")
while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(row)
print("=====================================")
# 7. Query with group by

print("\nUsers grouped by age with count:")
cursor.execute("SELECT age, COUNT(*) as count FROM users GROUP BY age")
results = cursor.fetchall()
for row in results:
    print(row)
print("=====================================")
cursor.execute("UPDATE users SET age = 22 WHERE name = 'Mayura'")
results = cursor.fetchall()
for row in results:
    print(row)

print("=====================================")

cursor.execute("SELECT * FROM users WHERE name like 'Mayura'")
results = cursor.fetchall()
print(results)
print("=====================================")
# 8. close the ursor and connection
cursor.close()
conn.close()