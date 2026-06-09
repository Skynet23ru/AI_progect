
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime_utils import get_now # hypothetically

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Vehicle(Base):
    __cl_id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    model = Column(String)
