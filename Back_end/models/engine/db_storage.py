#!/usr/bin/python3
"""This is the definition of the database class """

import models
from models.base_model import BaseModel, Base
from models.product import Product
from models.customer import Customer
from models.supplier import Supplier
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Product": Product, "Supplier": Supplier, "Customer": Customer}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        MYSQL_USER = getenv('MYSQL_USER')
        MYSQL_PWD = getenv('MYSQL_PWD')
        MYSQL_HOST = getenv('MYSQL_HOST')
        MYSQL_DB = getenv('MYSQL_DB')
        env = getenv('ENV')


        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PWD,
                                             MYSQL_HOST,
                                             MYSQL_DB))

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}

        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    if type(obj).__name__ == 'Product':
                        key = obj.__class__.__name__ + '.' + str(obj.serial_number)
                    else:
                        key = obj.__class__.__name__ + '.' + str(obj.id)
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id=None, name=None):
        """retrieves an object using its id or name"""
        if id is not None:
            obj = self.__session.query(cls).get(id)
            return obj
        if name is not None:
            obj = self.__session.query(cls).filter(cls.name == name).first()
            return obj

    def count(self, cls=None):
        """Returns the number of objects in storage matching the given class.
        If no class is passed, returns the count of all objects in storage"""
        if cls is None:
            return len(self.all())
        return len(self.all(cls))
