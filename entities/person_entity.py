import sys

# Preventing __pycache__ generation.
sys.dont_write_bytecode = True


from database import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    products = db.relationship('Product', backref='person', lazy=True)