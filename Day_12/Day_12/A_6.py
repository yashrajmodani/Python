import sqlalchemy
from sqlalchemy import create_engine, MetaData, Integer, String, Float, Sequence, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

#set up the database and the base class
engine = create_engine('sqlite:///company_orm1.db')
Base = sqlalchemy.orm.declarative_base()

#define he student model
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    subject = Column(String(50))
    marks = Column(Float)

# create the tables in the database
metadata = MetaData()
metadata.reflect(bind=engine)
Base.metadata.create_all(engine)
employees = metadata.tables['employees']

#Reflect the emplyees table to retrieve the data
inspector = inspect(engine)
columns =  inspector.get_columns('employees')#list of dictionaries

#print table details
print("Table 'students'Details:")
for column in columns:
    print(f"Column: {column['name']} - Type: {column['type']}")

#crete  a session
Session = sessionmaker(bind=engine)
session = Session()

#add student records
employees = [
    Student(name = 'Arun', age= 30, subject = 'HR', marks=  70),
    Student(name = 'Radhika', age= 30, subject = 'IT', marks=  80),
    Student(name = 'Chetan', age= 30, subject = 'FINANCE', marks=  20)
]
session.add_all(employees)
session.commit()

#query the database
all_employees = session.query(Student).all()
for std in all_employees:
    print(f"{std.id}:{std.name}- {std.subject}-${std.marks}")