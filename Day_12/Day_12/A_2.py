import sqlite3
import pandas as pd
try:
    conn = sqlite3.connect("company.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS departments(
        department_id INTEGER PRIMARY KEY AUTOINCREMENT,
        department_name TEXT NOT NULL)''')
    cursor.execute('''Create table if not exists employees(
    employee_id integer primary key,
    employee_name text not null,
    department_id INTEGER,
    Foreign_key(department_id) REFERENCES departments (department_id))''')

    cursor.execute('CREATE INDEX IF NOT EXISTS idx_employee_name ON employees(employee_name)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_department_name ON departments(department_name)')
    
    cursor.execute("Insert into departments (department_name) VALUES ('HR')")
    cursor.execute("Insert into departments (department_name) VALUES ('Engi')")
    cursor.execute("Insert into departments (department_name) VALUES ('Sales')")
    
    
    cursor.execute("Insert into employees (employee_name,department_id) VALUES ('Mayure',2)")
    cursor.execute("Insert into employees (employee_name,department_id) VALUES ('Yash',2)")
    cursor.execute("Insert into employees (employee_name,department_id) VALUES ('Rahul',1)")
    cursor.execute("Insert into employees (employee_name,department_id) VALUES ('Tarun',1)")
    
    conn.commit()
    print('==================================================')
    print("Employees and their Department")
    
    cursor.execute('''SELECT employee_id,employee_name,department_id from employees''')
    results = cursor.fetchall()
    for i in results:
        print(i)
    print('=============================================================')
    print("Employees and their Department")
    cursor.execute('''SELECT employees.employee_name,departments.department_name FROM employees
    JOIN departments on employees.department_id = departments.department_id''')

    results = cursor.fetchall()
    for i in results:
        print(i)


except sqlite3.Error as e:
    print("An error occurred:", e)



finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()