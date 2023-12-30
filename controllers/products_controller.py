import sys

# Preventing __pycache__ generation.
sys.dont_write_bytecode = True


from flask import jsonify
from flask import Blueprint
from services.products_service import (
                    get_all_products_service,
                    get_product_service,
                    update_product_service,
                    delete_product_service,
                    add_product_service)

products_view = Blueprint('products', __name__)

products_view.route('/', methods=['GET'])
def index():
    return jsonify({ "message": "Hello from flask" })

products_view.route('/products', methods=['GET'])
def get_all_products_controller():
    jsonify(get_all_products_service()) 

products_view.route('/products/<id>', methods=['GET'])
def get_product_controller(id):
    jsonify(get_product_service(id))

products_view.route('/products/<id>', methods=['PUT'])
def update_product_controller(id):
    jsonify(update_product_service(id))

products_view.route('/products/<id>', methods=['DELETE'])
def delete_product_controller(id):
    jsonify(delete_product_service(id))

products_view.route('/products', methods=['POST'])
def add_product_controller():
    jsonify(add_product_service())