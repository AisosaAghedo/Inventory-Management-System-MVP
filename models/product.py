#!/usr/bin/python3
"""This is the product class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

class Product(BaseModel, Base):
    """This is to create a table for the products"""
    __tablename__ = 'products'
    name = Column(String(50), nullable=False)
    serial_number = Column(Integer,primary_key=True)
    category = Column(String(45), nullable=False)
    price =  Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    expiry_date = Column(DateTime, nullable=False)
