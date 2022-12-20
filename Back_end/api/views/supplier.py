#!/usr/bin/python3
"""objects that handle all default RestFul API actions for the class Supplier"""
from api.views import app_views
from models.supplier import Supplier
from models.product import Product
from models import storage
from flask import abort, jsonify, make_response, request

@app_views.route('/suppliers', strict_slashes=False)
def get_suppliers():
    """ returns a list of all suppliers"""
    supplier_list = []
    for supplier in storage.all(Supplier).values():
        supplier_list.append(supplier.to_dict())
    return jsonify(supplier_list)

@app_views.route('/products/<product_serial_number>/suppliers', strict_slashes=False)
def get_supplier(product_serial_number):
    """ retrieves a list of all suppliers of a particular product"""
    product = storage.get(Product, product_serial_number)
    if not product:
        abort(404)
    if len(product.supplier) > 0:
        return jsonify(product.supplier[0].to_dict())

@app_views.route('/suppliers/<supplier_id>', strict_slashes=False)
def get_supplier_by_id(supplier_id):
    """retrieves a supplier using the supplier id"""
    supplier = storage.get(Supplier, supplier_id)
    if not supplier:
        abort(404)
    return jsonify(supplier.to_dict())

@app_views.route('/suppliers/<supplier_id>',methods=['DELETE'], strict_slashes=False)
def del_supplier(supplier_id):
    """ deletes a supplier using the id of the supplier """
    supplier = storage.get(Supplier, supplier_id)
    if not supplier:
        abort(404)
    storage.delete(supplier)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/products/<product_serial_number>/suppliers', methods=['POST'], strict_slashes=False)
def create_supplier(product_serial_number):
    """ creates a supplier """
    product = storage.get(Product, product_serial_number)
    if not product:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    if 'id' not in request.get_json():
        abort(400, description="Missing id")
    if 'quantity' not in request.get_json():
        abort(400, description="Missing quantity of product")
    if 'price' not in request.get_json():
        abort(400, description="Missing price of product")

    data = request.get_json()
    data['product_Sn'] = int(product_serial_number)
    instance = Supplier(**data)
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)
@app_views.route('/suppliers/<supplier_id>',methods=['PUT'], strict_slashes=False)
def update_supplier(supplier_id):
    """ update the supplier information"""
    supplier = storage.get(Supplier, supplier_id)
    if not supplier:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")

    touch_not = ['id', 'product_Sn', 'name',  'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in touch_not:
            setattr(supplier, key, value)
    storage.save()
    return make_response(jsonify(supplier.to_dict()), 200)


