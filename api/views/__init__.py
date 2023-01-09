#!/usr/bin/python3
""" 
Importing 'Blueprint' from 'flask'
"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api")
""" importing the modules in the init.py file to make it a package"""
from api.views.product import *
from api.views.supplier import *

