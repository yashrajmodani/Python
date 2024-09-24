import sqlalchemy
from sqlalchemy import create_engine, MetaData, Column , Integer, String, Float, Sequence

from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
import pandas as pd

##set up database and base class
engine = create_engine('sqlite:///example1.db', echo=True)
Base = sqlalchemy.orm.declarative_base()


#### define the employee model
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, Sequence('employee_id_seq'), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    position = Column(String(50), nullable=False)
    salary = Column(Float, nullable=False)


##### Create the table
def create_table():
    Base.metadata.create_all(engine)
    print("table 'employees' created successfully")

#Insert sample data
def insert_data():
    Session = sessionmaker(bind=engine)
    session = Session()
    
    #Sample data
    employees = [
        Employee(name='John', age=30, department='Er', salary=30000),
        Employee(name='Snow', age=40, department='Mr', salary=30000),
        Employee(name='Luffy', age=13, department='tech', salary=30000),
        Employee(name='Zoro', age=25, department='Analyst', salary=30000)

    ]
    
    #Add and commit data
    session.add_all(employees)
    session.commit()
    session.close()
    print("data inserted successfully")

# Read data into pandas df

def read_data():
    #load data into df
    df = pd.read_sql_table('employees', con=engine)
    return df


#Update data in df
def update_salary(df, employee_id, new_salary):
    df.loc[df['id'] == employee_id, 'salary'] = new_salary
    return df

#write updated data back to DB

def write_data(df):
    df.to_sql('employees', con=engine, if_exists='replace', index=False)
    print("data updated successfully")
    
#Main fuc to perform assign task   

def main():
    #Create table and insert data (RUN ONLY ONCE)
    create_table()
    insert_data()
    #Read data
    df = read_data()
    print('Original df')
    print(df)
    df = update_salary(df, 2, 40000)
    print("\n updated df")
    write_data(df)
    print('updated in the db')
    
    #Read Data
    df = read_data()
    print(df)
    
if __name__ == '__main__':
    main()
    