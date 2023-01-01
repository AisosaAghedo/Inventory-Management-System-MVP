#!/usr/bin/python3
""" To run the flask"""
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, current_user,logout_user 
from models.user import User
from models import storage
from models.product import Product
from datetime import datetime
from uuid import uuid4
app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'hyyuekdjhfgeksdcmnf'


@login_manager.user_loader
def load_user(user_id):
    """ """
    return storage.get(User, user_id)

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
    return redirect(url_for('products'))


@app.route('/products', strict_slashes=False)
@login_required
def products():
    """ to ensure just people with password can access the product page"""
    current_time = datetime.utcnow().strftime("%d/%m/%Y")
    products = list(storage.all(Product).values())
    total_category = []
    for product in products:
        if product.category not in total_category:
            total_category.append(product.category)

        expiry_date =  product.expiry_date.strftime("%d/%m/%Y")

    return render_template('product.html', products=products, total_category=len(total_category), current_time=current_time,
            total_product=len(products), cache_id=str(uuid4()), expiry_date=expiry_date )

@app.route('/add_product', strict_slashes=False)
@login_required
def add_product():
    """ to ensure just people with password can access the add product page"""
    return render_template('add_product.html', cache_id=str(uuid4()))

@app.route('/update/<product_sn>', strict_slashes=False)
@login_required
def update_product(product_sn):
    """ update the products"""
    return render_template('update_product.html', cache_id=str(uuid4()), product_sn=product_sn)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, threaded=True)
