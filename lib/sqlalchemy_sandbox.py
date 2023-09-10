#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker  # Import the sessionmaker

Base = declarative_base()

# Define the Student class and associated table
class Student(Base):
    __tablename__ = 'students'  # Set the table name

    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__':
    # Create a database engine
    engine = create_engine('sqlite:///students.db')  # Use SQLite as the database

    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)  # Bind the session to the engine
    session = Session()

    # Example: Adding a student to the database
    new_student = Student(name="John Doe")
    session.add(new_student)
    session.commit()  # Commit the transaction

    # Example: Querying the database
    students = session.query(Student).all()
    for student in students:
        print(f"Student ID: {student.id}, Name: {student.name}")

    session.close()  # Close the session
