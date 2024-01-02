import sys

# Preventing __pycache__ generation.
sys.dont_write_bytecode = True

from flask import Flask
from models.products_model import db
from controllers.products_controller import products_bp

# Factory app
def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(products_bp)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app