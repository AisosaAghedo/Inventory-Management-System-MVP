#!/usr/bin/python3
"""This is the user class"""
from models.base_model import Base
from sqlalchemy import Column, String
from flask_login import UserMixin
import models
import hashlib
from uuid import uuid4

class User(Base, UserMixin):
    """This is to create a table for the admin user"""
    __tablename__ = 'user'
    id = Column(String(60), default=uuid4())
    username = Column(String(50), primary_key=True)
    password = Column(String(45), nullable=False)

    def __init__(self, *args, **kwargs):
        """this function initializes user"""
        if kwargs.get('password') is not None:
            pwd = kwargs['password']
            del kwargs['password']
            self.__secure_password(pwd)
        super().__init__(*args, **kwargs)

    def __secure_password(self, pwd):
        """encrypts user password to md5"""
        secure = hashlib.md5()
        secure.update(pwd.encode("utf-8"))
        self.password = secure.hexdigest()

    def confirm_pwd(self, pwd):
        """checks if password is correct"""
        secure = hashlib.md5()
        secure.update(pwd.encode("utf-8"))
        pwd = secure.hexdigest()
        if pwd == self.password:
            return True
        return False
