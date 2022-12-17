#!/usr/bin/python3
"""This is the Suppliers class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Supplier(BaseModel, Base):
    """This is to create a Table for the  suppliers"""
    __tablename__ = "suppliers"
    Name = Column(String(70), nullable=False)
    Id = Column(Integer, nullable=False)
    Quantity = Column(Integer, nullable=False)
    Price = Column(Integer, nullable=False)
    Product_Sn = Column(Integer, ForeignKey("products.Serial_number"))
    product = relationship("Product", back_ref="supplier", uselist=False)



