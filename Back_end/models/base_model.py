#!/usr/bin/python3
""" Base model module where all models inherit from"""
import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, DateTime, Column
Base = declarative_base()

class BaseModel:
    """ The basemode class that initializies the classs """
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime(), nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            created_at: creation date
            updated_at: updated date
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                        setattr(self, key, value)
            if "created_at" not in kwargs:
                    self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                    self.updated_at = datetime.now()
            else:
                self.created_at = self.updated_at = datetime.now()
        
    def __str__(self):
        '''returns a string of class name, and dictionary'''
        return f"{self.__name__} {self.__dict__}"

    def __repr__(self):
        '''string representation function'''
        return self.__str__()

    def save(self):
        '''this to update public instance attribute(updated_at) to current'''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''this creates a dictionary of class and what they return''' 
        my_dict = dict(self.__dict__)
        my_dict["__class_"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def delete(self):
        '''function to delete an object ''' 
        models.storage.delete(self)       

