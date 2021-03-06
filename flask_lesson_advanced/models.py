import uuid
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField
from wtforms.validators import DataRequired


class Product_class:
    def __init__(self, name, description, price, img_name):
        self.name = name
        self.description = description
        self.img_name = img_name
        self.price = price
        self.id = str(uuid.uuid4())


class Supermarket_class:
    def __init__(self, name, location, img_name):
        self.name = name
        self.location = location
        self.img_name = img_name
        self.id = str(uuid.uuid4())
