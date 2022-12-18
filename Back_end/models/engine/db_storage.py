#!/usr/bin/python3
"""This is the definition of the database class """
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker
from models.product import Product
from models.customer import Customer
from models.supplier import Supplier
classes = {"Product": Product, "Supplier": Supplier, "Customer": Customer}


class DBStorage:
    """ Class DBStorage handles storage using DB"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor """
        user = getenv("MYSQL_USER")
        pwd = getenv("MYSQL_PWD")
        dbase = getenv("MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(user, pwd, dbase),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """ return all instances of the class if not
        null else, return all obj"""
        new_dict = {}

        if cls is None:
            for key in classes.keys():
                sesh = self.__session.query(classes[key]).all()
                for obj in sesh:
                    key1 = key + "." + obj.id
                    new_dict[key1] = obj.to_dict()
        else:
            if cls.__name__ in classes:
                sesh = self.__session.query(cls).all()
                for obj in sesh:
                    key1 = cls.__name__ + "." + obj.id
                    new_dict[key1] = obj.to_dict()
        return new_dict

    def new(self, obj):
        """add new objects to the database"""
        self.__session.add(obj)

    def save(self):
        """commit all new changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesh)
        self.__session = Session()

    def close(self):
        """ updating DB storage """
        self.__session.close()
