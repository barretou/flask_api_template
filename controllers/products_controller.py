# controllers/products_controller.py
from flask import Blueprint
import services.products_service as ProductService

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/', methods=['GET'])
def get_all_products_controller():
    return ProductService.get_all_products_service()

@products_bp.route('/<id>', methods=['GET'])
def get_product_controller(id):
    return ProductService.get_product_service(id)

@products_bp.route('/<id>', methods=['PUT'])
def update_product_controller(id):
    return ProductService.update_product_service(id)

@products_bp.route('/<id>', methods=['DELETE'])
def delete_product_controller(id):
    return ProductService.delete_product_service(id)

@products_bp.route('/', methods=['POST'])
def add_product_controller():
    return ProductService.add_product_service()
