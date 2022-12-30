#!/usr/bin/python3
"""
Creating the variable 'app' an instance of flask
"""
from flask import Flask, jsonify
from api.views import app_views
import models
from flask_cors import CORS
app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.errorhandler(404)
def error_404(exception):
    """ a handler for 404 errors that returns
    a JSON-formatted 404 status code response"""
    return jsonify(error="Not found"), 404

@app.errorhandler(400)
def handle_400(e):
    """handles code 400 httpexception """
    message = e.description
    return jsonify({'error': message}), 400

@app.teardown_appcontext
def teardown_db(exception):
    """ closes off session with database"""
    models.storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
