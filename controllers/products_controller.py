# controllers/products_controller.py
from flask import Blueprint
import repository.products_repository as ProductRepository

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/', methods=['GET'])
def get_all_products_controller():
    """
    Retrieve all products.

    Returns:
        Flask Response: Serialized products with a 200 status code.
        Flask Response: JSON with an error message and a 500 status code if an exception occurs.

    Endpoint: GET /products
    """
    return ProductRepository.get_all_products()

@products_bp.route('/<id>', methods=['GET'])
def get_product_controller(id):
    """
    Retrieve a specific product by ID.

    Args:
        id (int): Product ID.

    Returns:
        Flask Response: Serialized product with a 200 status code.
        Flask Response: JSON with an error message and a 404 status code if the product is not found.
        Flask Response: JSON with an error message and a 500 status code if an exception occurs.

    Endpoint: GET /products/<id>
    """
    return ProductRepository.get_product(id)

@products_bp.route('/<id>', methods=['PUT'])
def update_product_controller(id):
    """
    Update a specific product by ID.

    Args:
        id (int): Product ID.

    Returns:
        Flask Response: Serialized updated product with a 200 status code.
        Flask Response: JSON with an error message and a 404 status code if the product is not found.
        Flask Response: JSON with an error message and a 500 status code if an exception occurs.

    Endpoint: PUT /products/<id>
    """
    return ProductRepository.update_product(id)

@products_bp.route('/<id>', methods=['DELETE'])
def delete_product_controller(id):
    """
    Delete a specific product by ID.

    Args:
        id (int): Product ID.

    Returns:
        Flask Response: JSON with a success message and a 200 status code.
        Flask Response: JSON with an error message and a 404 status code if the product is not found.
        Flask Response: JSON with an error message and a 500 status code if an exception occurs.

    Endpoint: DELETE /products/<id>
    """
    return ProductRepository.delete_product(id)

@products_bp.route('/', methods=['POST'])
def add_product_controller():
    """
    Add a new product.

    Returns:
        Flask Response: JSON with a success message and a 201 status code.
        Flask Response: JSON with an error message and a 500 status code if an exception occurs.

    Endpoint: POST /products
    """
    return ProductRepository.add_product()

