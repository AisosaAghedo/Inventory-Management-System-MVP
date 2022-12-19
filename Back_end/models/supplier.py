#!/usr/bin/python3
"""This is the Suppliers class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Supplier(BaseModel, Base):
    """This is to create a Table for the  suppliers"""
    __tablename__ = "suppliers"
    name = Column(String(70), nullable=False)
    id = Column(Integer, nullable=False, primary_key=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    product_Sn = Column(Integer, ForeignKey("products.serial_number"))
    product = relationship("Product", backref="supplier", uselist=False)



