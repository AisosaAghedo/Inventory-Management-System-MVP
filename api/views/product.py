#!/usr/bin/python3
"""  objects that handle all default RestFul API actions for the class Product"""
from api.views import app_views
from models.product import Product
from models import storage
from flask import abort, jsonify, make_response, request


@app_views.route('/products', strict_slashes=False)
def get_products():
    """
    Retrieves the list of all product
    """
    list_products = []
    for product in storage.all(Product).values():
        list_products.append(product.to_dict())
    return jsonify(list_products)


@app_views.route('/products/<product_serial_number>', strict_slashes=False)
def get_product(product_serial_number):
    """ Retrieves a product """
    product = storage.get(Product, product_serial_number)
    if not product:
        abort(404)

    return jsonify(product.to_dict())


@app_views.route('/products/<product_serial_number>', methods=['DELETE'],
                 strict_slashes=False)
def delete_product(product_serial_number):
    """
    Deletes a product Object
    """
    product = storage.get(Product, product_serial_number)

    if not product:
        abort(404)

    storage.delete(product)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('users/<user_id>/products', methods=['POST'], strict_slashes=False)
def post_product(user_id):
    """
    Creates a new product
    """
    data =  request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if 'name' not in data:
        abort(400, description="Missing name")
    if 'serial_number' not in data:
        abort(400, description="Missing serial_number")
    if 'category' not in data:
        abort(400, description="Missing category")
    if 'price' not in data:
        abort(400, description="Missing price ")
    if 'expiry_date' not in data:
        abort(400, description="Missing expiry_date")
    if 'quantity' not in data:
        abort(400, description="Missing quantity")
    print("i am id" + user_id)
    data["user_id"] = user_id
    instance = Product(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/products/<product_serial_number>', methods=['PUT'], strict_slashes=False)
def put_product(product_serial_number):
    """
    This function Updates the quantity and price of an existing product
    """
    product = storage.get(Product, product_serial_number)

    if not product:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    dont_change = ['name', 'serial_number', 'created_at', 'updated_at', 'category', 'expiry_date']

    data = request.get_json()
    for key, value in data.items():
        if key not in dont_change:
            setattr(product, key, value)
    storage.save()
    return make_response(jsonify(product.to_dict()), 200)

@app_views.route('/products_search', methods=['POST'],
           strict_slashes=False)
def search_product():
    """This function is for searching for a product using query given"""
    req = request.get_json()
    products = []

    if req is None:
        abort(400, description='Not a json')
    if req.get('query') is None:
        abort(400, description='Missing query')
    for product in storage.all(Product).values():
        if (req['query'].lower() in product.name.lower()):
            products.append(product.to_dict())
    return jsonify(products)
