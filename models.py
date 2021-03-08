from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

"""
Database metadata+table identification
"""
Base = declarative_base()


# Model for the Employee
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(50))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
