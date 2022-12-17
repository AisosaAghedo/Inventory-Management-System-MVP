#!/usr/bin/python3
"""This is the product class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Product(BaseModel, Base):
    """This is to create a table for the products"""
    __tablename__ = 'products'
    Serial_number = Column(Integer,primary_key=True)
    category = Column(String(45), nullable=False)
    price =  Column(Integer, nullable=False)
    expiry_date = Column(nullable=False)
