############ employeee code #############
import sqlite3
import pandas as pd
try:
    conn = sqlite3.connect('company.db')
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS department(
        department_id INTEGER PRIMARY KEY AUTOINCREMENT,
        department_name TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS employees(
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES department(department_id))''')

    cursor.execute('CREATE INDEX IF NOT EXISTS idx_employee_name ON employees (employee_name)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_department_name ON department (department_name)')

    cursor.execute("INSERT into department (department_name) VALUES ('HR')")
    cursor.execute("INSERT into department (department_name) VALUES ('Engineering')")
    cursor.execute("INSERT into department (department_name) VALUES ('Sales')")
    cursor.execute("INSERT into department (department_name) VALUES ('IT')")


    cursor.execute("INSERT into employees (employee_name, department_id) VALUES ('Dai',2)")
    cursor.execute("INSERT into employees (employee_name, department_id) VALUES ('DBDA',3)")
    cursor.execute("INSERT into employees (employee_name, department_id) VALUES ('Dac',1)")


    conn.commit()
    print("Employees & their departments")
    cursor.execute('''SELECT employee_id, employee_name, department_id FROM employees ''')
    results = cursor.fetchall()
    for row in results:
        print(row)

    print("=================================================================================================")
    print("Employees & their departments")
    cursor.execute('''SELECT employees.employee_name, department.department_name FROM employees
     JOIN department ON employees.department_id = department.department_id ''')
    results = cursor.fetchall()
    for row in results:
        print(row)

    print("=================================================================================================")
except sqlite3.Error as e:
    print(f"SQLite error: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()