#!/usr/bin/python3
"""This is the customers class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Customer(BaseModel, Base):
    """This is to create the table for the customers"""
    __tablename__ =  "customers"
    Name = Column(String(120), nullable=False)
    Id = Column(Integer,nullable=False)
    Quantity = Column(Integer,nullable=False)
    Product_Sn = Column(Integer, ForeignKey("products.Serial_number"))
    product = relationship("Product", back_ref="customer")


