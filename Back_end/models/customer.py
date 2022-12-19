#!/usr/bin/python3
"""This is the customers class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Customer(BaseModel, Base):
    """This is to create the table for the customers"""
    __tablename__ =  "customers"
    name = Column(String(120), nullable=False)
    id = Column(Integer,nullable=False, primary_key=True)
    quantity = Column(Integer,nullable=False)
    product_Sn = Column(Integer, ForeignKey("products.serial_number"))
    product = relationship("Product", backref="customer")


