#!/usr/bin/python3
"""api to interact with the table named users"""
from api.views import app_views
from models.user import User
from models import storage
from flask import abort, jsonify, make_response, request



@app_views.route("/users/<user_id>", methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    returns a user using the user id in JSON format
    """
    user = storage.get(User, user_id)

    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("/users", methods=['GET'],
                 strict_slashes=False)
def get_users():
    """ 
    returns all users.
    """
    users = []
    for user in storage.all(User).values():
        users.append(user.to_dict())
    return jsonify(users)

@app_views.route("/users", methods=['POST'],
                 strict_slashes=False)
def post_users():
    """
    crreates new users.
    """
    req = request.get_json()
    if req is None:
        abort(400, description="Not a json")
    if req.get('username') is None:
        abort(400, description="Missing username")
    if storage.get(User, None, req['username']):
        abort(400, description="Username is in use")
    if req.get("password") is None:
        abort(400, description="Missing password")
    if req.get("confirm_password") is None:
        abort(400, description="Fill out the confirm password field")
    if req['password'] != req['confirm_password']:
        abort(400, 'password does not match confirm password')

    if len(req["password"]) < 5:
        abort(400, "password must be at least 5 characters")
    if req.get("id"):
        del req['id']
    del req['confirm_password']

    user = User(**req)
    user.save()
    return jsonify(user.to_dict()), 201



@app_views.route('/users/<user_id>', methods=["PUT"],
                 strict_slashes=False)
def update_user(user_id):
    """
    updates a user information using it's id
    """
    user = storage.get(User, user_id)
    if user is None:
            abort(404)
    restricted_attr = ['id', 'created_at', 'updated_at']
    req = request.get_json()

    if req is None:
        abort(400, description="Not a json")
    if req['password'] != req['confirm_password']:
        abort(400, 'password does not match confirm password')
    for key in req.keys():
        if key not in restricted_attr:
            setattr(user, key, req[key])
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=["DELETE"],
                 strict_slashes=False)
def delete_user(user_id):
    """
    deletes a user account using the user_id
    """
    user = storage.get(User, user_id)
    storage.delete(user)
    storage.save()
    return jsonify({})


