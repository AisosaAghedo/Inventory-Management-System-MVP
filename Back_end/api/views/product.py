#!/usr/bin/python3
""" Pactice to test if my api works """
from api.views import app_views
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def status():
    """ checking for the status of the api """
    return jsonify({'status': 'Ok dokey'})
