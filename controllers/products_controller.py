# controllers/products_controller.py
from flask import Blueprint
import repository.products_repository as ProductRepository

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/', methods=['GET'])
def get_all_products_controller():
    return ProductRepository.get_all_products()

@products_bp.route('/<id>', methods=['GET'])
def get_product_controller(id):
    return ProductRepository.get_poduct(id)

@products_bp.route('/<id>', methods=['PUT'])
def update_product_controller(id):
    return ProductRepository.update_poduct(id)

@products_bp.route('/<id>', methods=['DELETE'])
def delete_product_controller(id):
    return ProductRepository.delete_poduct(id)

@products_bp.route('/', methods=['POST'])
def add_product_controller():
    return ProductRepository.add_poduct()
