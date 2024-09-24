import sqlalchemy
from sqlalchemy import create_engine, MetaData, Integer, String, Float, Sequence, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

#set up the database and the base class
engine = create_engine('sqlite:///company_orm1.db')
Base = sqlalchemy.orm.declarative_base()

#define he employee model
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, Sequence('employee_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    department = Column(String(50))
    salary = Column(Float)

# create the tables in the database
metadata = MetaData()
metadata.reflect(bind=engine)
Base.metadata.create_all(engine)
employees = metadata.tables['employees']

#Reflect the emplyees table to retrieve the data
inspector = inspect(engine)
columns =  inspector.get_columns('employees')#list of dictionaries

#print table details
print("Table 'employees'Details:")
for column in columns:
    print(f"Column: {column['name']} - Type: {column['txype']}")

#crete  a session
Session = sessionmaker(bind=engine)
session = Session()

#add employee records
employees = [
    Employee(name = 'Arun', age= 30, department = 'HR', salary=  70000),
    Employee(name = 'Radhika', age= 30, department = 'IT', salary=  80000),
    Employee(name = 'Chetan', age= 30, department = 'FINANCE', salary=  120000)
]
session.add_all(employees)
session.commit()

#query the database
all_employees = session.query(Employee).all()
for emp in all_employees:
    print(f"{emp.id}:{emp.name}- {emp.department}-${emp.salary}")