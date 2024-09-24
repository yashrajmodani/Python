#########STUDENT DATABASE######
import sqlite3
import pandas as pd
# try:
conn = sqlite3.connect("student.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS subjects(
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    subject_id INTEGER,
    FOREIGN KEY(subject_id) REFERENCES subjects (subject_id))''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_student_name ON students(student_name)')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_subject_name ON subjects(subject_name)')
    
cursor.execute("Insert into subjects (subject_name) VALUES ('AI')")
cursor.execute("Insert into subjects (subject_name) VALUES ('ML')")
cursor.execute("Insert into subjects (subject_name) VALUES ('DL')")
    
    
cursor.execute("Insert into students (student_name,subject_id) VALUES ('Mayur',2)")
cursor.execute("Insert into students (student_name,subject_id) VALUES ('Yash',2)")
cursor.execute("Insert into students (student_name,subject_id) VALUES ('Rahul',1)")
cursor.execute("Insert into students (student_name,subject_id) VALUES ('Tarun',1)")
    
conn.commit()
print('==================================================')
print("student and their subjects")
    
cursor.execute('''SELECT student_id,student_name,subject_id from students''')
results = cursor.fetchall()
for i in results:
    print(i)
print('=============================================================')
print("students and their subjects")
cursor.execute('''SELECT students.student_name,subjects.subject_name FROM students
JOIN subjects on students.student_id = subjects.subject_id''')

results = cursor.fetchall()
for i in results:
    print(i)


# except sqlite3.Error as e:
#     print("An error occurred:", e)
#
#
#
# finally:
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()