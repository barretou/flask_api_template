import sys

# Preventing __pycache__ generation.
sys.dont_write_bytecode = True

from flask import jsonify
from config import create_app
import services.products_service as Service

# Flask Instace
app = create_app()

# Routes
@app.route('/', methods=['GET'])
def index():
    return jsonify({ "message": "Hello from flask" })

@app.route('/products', methods=['GET'])
def get_all_products_controller():
    return Service.get_all_products_service()

@app.route('/products/<id>', methods=['GET'])
def get_product_controller(id):
    return Service.get_product_service(id)

@app.route('/products/<id>', methods=['PUT'])
def update_product_controller(id):
    return Service.update_product_service(id)

@app.route('/products/<id>', methods=['DELETE'])
def delete_product_controller(id):
    return Service.delete_product_service(id)

@app.route('/products', methods=['POST'])
def add_product_controller():
    return Service.add_product_service()

if __name__ == '__main__':
    app.run(debug=True)