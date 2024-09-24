import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY,name TEXT,age INTEGER,grade TEXT)''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (course_id INTEGER PRIMARY KEY,course_name TEXT,instructor TEXT)''')

cursor.execute("INSERT INTO student (name, age,grade) VALUES ('Mayura',30,'B')")
cursor.execute("INSERT INTO student (name, age,grade) VALUES ('Mayuresh',25,'A')")
cursor.execute("INSERT INTO student (name, age,grade) VALUES ('Sugandha',30,'C')")
cursor.execute("INSERT INTO student (name, age,grade) VALUES ('Sonu',25,'A')")
cursor.execute("INSERT INTO student (name, age,grade) VALUES ('Srujan',25,'E')")

print("student table :")
cursor.execute("SELECT * FROM student")
result = cursor.fetchall()
for i in result:
    print(i)
print('-------------------------------------------------------')

cursor.execute("INSERT INTO courses (course_name, instructor) VALUES ('DAI','JOHN')")
cursor.execute("INSERT INTO courses (course_name, instructor) VALUES ('DBDA','BOB')")
cursor.execute("INSERT INTO courses (course_name, instructor) VALUES ('DAC','STUT')")

print("courses table :")
cursor.execute("SELECT * FROM courses")
result = cursor.fetchall()
for i in result:
    print(i)
print('-------------------------------------------------------')

conn.commit()

# # Students with Grade "A'
#
cursor.execute("SELECT * FROM student WHERE grade like 'A'")
results = cursor.fetchall()
print(results)
print('--------------------------------------------------')
# # List all courses

print("order by course_name\n")
cursor.execute("SELECT * FROM courses ORDER BY course_name")

while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(row)

# UPDATE
cursor.execute("UPDATE student SET grade = 'A' WHERE name = 'Srujan'")
print("Updated student table :")
cursor.execute("SELECT * FROM student")
results = cursor.fetchall()
for row in results:
    print(row)
print('--------------------------------------------------')

cursor.execute("UPDATE courses SET instructor = 'Elvish' WHERE course_id = 2")
print("Updated Course table :")
cursor.execute('SELECT * FROM courses')
results = cursor.fetchall()
for row in results:
    print(row)
print('--------------------------------------------------')
# DELETE
cursor.execute("DELETE from student where id = 4")
print("Updated Student Table after deleting student")
cursor.execute("Select * from student")
res = cursor.fetchall()
for i in res:
    print(i)

print('--------------------------------------------------')

cursor.execute("DROP TABLE IF EXISTS student")
cursor.execute("DROP TABLE IF EXISTS courses")

# To check where the tables are deleted or not
# print("student table :")
# cursor.execute("SELECT * FROM student")
# result = cursor.fetchall()
# for i in result:
#     print(i)


# print("courses table :")
# cursor.execute("SELECT * FROM courses")
# result = cursor.fetchall()
# for i in result:
#     print(i)

cursor.close()

conn.close()