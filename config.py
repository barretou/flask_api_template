import sys

# Preventing __pycache__ generation.
sys.dont_write_bytecode = True

from flask import Flask
from models.products_model import db

# Factory app
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app