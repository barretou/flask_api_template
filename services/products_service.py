import sys

# Preventing __pycache__ generation.
sys.dont_write_bytecode = True


from flask import request, jsonify, make_response
from models.products_model import Product, db, product_schema, products_schema

def get_all_products_service():
    try:
        all_products = Product.query.all()
        serialized_products = products_schema.dump(all_products)
        response = make_response(serialized_products, 200)
        return response
    except Exception as e:
        return jsonify({"error": str(e)})

def get_product_service(id):
    try:
        product = Product.query.get(id)
        if product:
            serialized_product = product_schema.dump(product)
            response = make_response(serialized_product, 200)
            return response
        else:
            return jsonify({"error": "Product not found"})
    except Exception as e:
        return jsonify({"error": str(e)})

def add_product_service():
    try:
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        quantity = request.json['quantity']

        new_product = Product(name, description, price, quantity)

        db.session.add(new_product)
        db.session.commit()

        response = make_response('Product was created', 201)
        return response
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})

def update_product_service(id):
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
            response = make_response(serialized_product, 200)
            return response
        else:
            return jsonify({"error": "Product not found"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})

def delete_product_service(id):
    try:
        product = Product.query.get(id)
        if product:
            db.session.delete(product)
            db.session.commit()
            response = make_response('Product was deleted', 200)
            return response
        else:
            return jsonify({"error": "Product not found"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})
