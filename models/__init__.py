#!/usr/bin/python3
"""This module instantiates an object of class DBStorage"""

from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.product import Product
from models.supplier import Supplier
from models.user import User

""" creating a variable to store the DBstorage method in"""
storage = DBStorage()
storage.reload()
