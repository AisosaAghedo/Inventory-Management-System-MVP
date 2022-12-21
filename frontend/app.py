#!/usr/bin/python3
""" To run the flask"""
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user
from models.user import User
from models import storage
app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'hyyuekdjhfgeksdcmnf'


@login_manager.user_loader
def load_user(username):
    """ """
    return storage.get(User, None, username)

@app.route('/login', strict_slashes=False)
def login():
    """ returns the login page"""
    return(render_template('login.html'))

@app.route('/login', methods=['POST'], strict_slashes=False)
def login_post():
    """ if the login details are correct load this login post """

    username = request.form.get('username')
    password = request.form.get('password')

    user = storage.get(User, None, username)
    if not user or not user.confirm_pwd(password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))
    
    """if the above check passes, then we know
    the user has the right credentials"""
    
    login_user(user)
    return redirect(url_for('what ever you name our home page')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
