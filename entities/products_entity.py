import sys

# Preventing __pycache__ generation.
sys.dont_write_bytecode = True

from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import mapped_column
from database import db
from marshmallow import Schema

class Product(db.Model):
    __tablename__ = "products"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100))
    description = mapped_column(String(200))
    price = mapped_column(Float)
    quantity = mapped_column(Integer)

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class ProductSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'quantity')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
