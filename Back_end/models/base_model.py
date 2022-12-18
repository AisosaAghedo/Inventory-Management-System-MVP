#!/usr/bin/python3

import uuid
import models
from datetime import datetime

def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                        setattr(self, key, value)
            if "id" not in kwargs:
                    self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                    self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                    self.updated_at = datetime.now()
            else:
                self.id = str(uuid.uuid4())
                self.created_at = self.updated_at = datetime.now()
        
        def __str__(self):
            '''returns 
            a string of 
            class name, id, and dictionary'''
            return f"{self.__name__} {self.id} {self.__dict__}"

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

