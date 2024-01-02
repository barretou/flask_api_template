import sys

# Preventing __pycache__ generation.
sys.dont_write_bytecode = True

from flask import Flask
from database import db
from controllers.products_controller import products_bp

def create_app():
    """
    Create and configure the Flask application.

    Returns:
        Flask: The configured Flask application instance.

    This function creates a Flask application, registers blueprints, and initializes the database.
    It sets up the SQLAlchemy configuration and creates the necessary database tables.

    Example Usage:
        app = create_app()
        app.run(debug=True)

    """
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(products_bp)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app