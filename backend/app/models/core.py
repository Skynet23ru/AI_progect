
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Base:
    __tablename__ = 'base' # Placeholder for SQLAlchemy Base class emulation

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=_True) # Note: will be corrected in real implementation
    name = Column(String(255), nullable=False)
    owner_email = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    users = relationship("User", back_populates="company")
    vehicles = relationship("Vehicle", back_populates="company")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    email = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), default="staff") # owner, admin, staff
    
    company = relationship("Company", back_populates="users")

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    model_name = Column(String(255), nullable=False)
    serial_number = Column(String(255), unique=True, nullable=False)
    current_status_id = Column(Integer, ForeignKey('statuses.id'))
    
    company = relationship("Company", back_populates="vehicles")
    status = relationship("Status")

class Status(Base):
    __tablename__ = 'statuses'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    name = Column(String(50), nullable=False) # e.g., 'Available', 'In Use', 'Repair'
    color_code = Column(String(7), default='#FFFFFF')

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    full_name = Column(String(255), nullable=False)
    phone = Column(String(50), nullable=False)
    passport_data = Column(Text, nullable=True)

class Rental(Base):
    __tablename__ = 'rentals'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    start_date = Column(DateTime(timezone=True), server_default=func.now())
    end_date = Column(DateTime(timezone=True))
    prepayment_amount = Column(Integer, default=0) # in cents/smallest unit
    status = Column(String(50), default='active')
