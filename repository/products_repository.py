import sys

# Preventing __pycache__ generation.
sys.dont_write_bytecode = True


from flask import request, jsonify, make_response
from database import db
from entities.products_entity import Product, product_schema, products_schema

def get_all_products():
    """
    Retrieve all products from the database.

    Returns:
        Flask Response: Serialized products with a 200 status code.
        Flask Response: JSON with an error message and a 500 status code if an exception occurs.
    """
    try:
        all_products = Product.query.all()
        serialized_products = products_schema.dump(all_products)
        response = make_response(jsonify({"data": serialized_products}), 200)
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_product(id):
    """
    Retrieve a specific product by its ID from the database.

    Args:
        id (int): Product ID.

    Returns:
        Flask Response: Serialized product with a 200 status code.
        Flask Response: JSON with an error message and a 404 status code if the product is not found.
        Flask Response: JSON with an error message and a 500 status code if an exception occurs.
    """
    try:
        product = Product.query.get(id)
        if product:
            serialized_product = product_schema.dump(product)
            response = make_response(jsonify({"data": serialized_product}), 200)
            return response
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_product():
    """
    Add a new product to the database.

    Returns:
        Flask Response: JSON with a success message and a 201 status code.
        Flask Response: JSON with an error message and a 500 status code if an exception occurs.
    """
    try:
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        quantity = request.json['quantity']

        new_product = Product(name, description, price, quantity)

        db.session.add(new_product)
        db.session.commit()

        response = make_response(jsonify({"message": 'Product was created'}), 201)
        return response
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def update_product(id):
    """
    Update a specific product in the database.

    Args:
        id (int): Product ID.

    Returns:
        Flask Response: Serialized updated product with a 200 status code.
        Flask Response: JSON with an error message and a 404 status code if the product is not found.
        Flask Response: JSON with an error message and a 500 status code if an exception occurs.
    """
    try:
        product = Product.query.get(id)
        if product:
            name = request.json['name']
            description = request.json['description']
            price = request.json['price']
            quantity = request.json['quantity']

            product.name = name
            product.description = description
            product.price = price
            product.quantity = quantity

            db.session.commit()

            serialized_product = product_schema.dump(product)
            response = make_response(jsonify({"data": serialized_product}), 200)
            return response
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def delete_product(id):
    """
    Delete a specific product from the database.

    Args:
        id (int): Product ID.

    Returns:
        Flask Response: JSON with a success message and a 200 status code.
        Flask Response: JSON with an error message and a 404 status code if the product is not found.
        Flask Response: JSON with an error message and a 500 status code if an exception occurs.
    """
    try:
        product = Product.query.get(id)
        if product:
            db.session.delete(product)
            db.session.commit()
            response = make_response(jsonify({"message": 'Product was deleted'}), 200)
            return response
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

