#from app import app

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import db_methods
import pdb
import secrets
import helper_methods

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = secrets.token_urlsafe(16) 

db = SQLAlchemy(app)
#sess = Session()
#sess.init_app(app)
import models.test_model as models
import load_data
import login_form

import pdb

db_methods.get_product_types(db)
db_methods.get_product_info(db,'IL')
db_methods.validate_login(db,'tpxyrc','3qkdWRHp')




#cart is a list of product_ids
session={'user_id': 0, 'state': 'CA', 'cart': [{'product_id': 1001, 'product_name': 'Apple', 'quantity': 3, 'price': 13.48}, {'product_id': 1002, 'product_name': 'Banana', 'quantity': 5, 'price': 2.48}]}
#pdb.set_trace()


@app.route('/')
def index():
    form = login_form.LoginForm()
    return render_template('index.html', form = form)

@app.route('/update-cart', methods=["GET"])
def update_cart():
    product_id = int(request.args.get("product_id", 0))
    quantity = int(request.args.get("quantity", 0))

    for cart_item in session['cart']:
        if cart_item['product_id'] == product_id:
            item = cart_item
            item['quantity'] = quantity
            cart_item.update(item)
    return "success"

@app.route('/add-cart', methods=["GET"])
def add_to_cart():
    product_id = int(request.args.get("product_id", 0))
    product_name = str(request.args.get("product_name", None))
    quantity = int(request.args.get("quantity", 0))
    price = float(request.args.get("price", 0))

    if not helper_methods.validate_cart_request(product_id, product_name, quantity, price):
        print("Invalid Request", product_id, product_name, quantity, price)

    #check if existing
    item = helper_methods.get_existing_item(session['cart'], product_id)
    if(item['product_id'] == None):
        item['product_id'] = product_id
        item['product_name'] = product_name
        item['quantity'] = quantity
        item['price'] = price
        session['cart'].append(item)
    else:
        item['quantity'] += quantity
        for cart_item in session['cart']:
            if cart_item['product_id'] == product_id:
                cart_item.update(item)
    return "success"
    
@app.route('/delete-item-cart', methods=["GET"])
def delete_item():    
    product_id = int(request.args.get("product_id", 0))
    print("test")
    for cart_item in session['cart']:
        if cart_item['product_id'] == product_id:
            item = cart_item
            session['cart'].remove(item)
    return "success"

@app.route('/products', methods=["GET"])
def view_products():
    username = str(request.args.get("username", "no"))
    password = str(request.args.get("password", "no"))
    print(username, password)
    user_id = db_methods.validate_login(db, username, password)
    if user_id == 0:
        form = login_form.LoginForm()
        return render_template('index.html', form = form)
    state = request.args.get("state_select", "CA")
    add_session_variables(user_id, state)
    print(session['user_id'])
    print(session['state'])
    categories = db_methods.get_product_info(db, state)
    #pdb.set_trace()
    return render_template('products.html', state=state, username=username, rows=categories)

@app.route('/view-cart', methods=["GET"])
def view_cart():
    print("arrived")
    return render_template('view_cart.html', cart = session['cart'])

@app.route('/payment-page', methods=["GET"])
def get_payment_page():
    return render_template('payment.html', cart = session['cart'])

@app.route('/init-data')
def init_d():
    load_data.init_data(db)
    return "Initialized Data!"

@app.route('/add-test')
def add():
    try:
        test=models.Test(
            name="name",
            name2="name2",
        )
        db.session.add(test)
        db.session.commit()
        return "Test added. test id={}".format(test.test_id)
    except Exception as e:
	    return(str(e))

@app.route('/heartbeat')
def test():
    return "Hello World"

@app.route('/test-input')
def test_input():
    name = request.args.get("name", "test")
    return "Hello, " + name

@app.route('/logout')
def logout():
   # remove all session variables
   session['user_id'] = 0
   session['state'] = 'CA'
   return redirect(url_for('index'))

def add_session_variables(user_id, state):
    session['user_id'] = user_id
    session['state'] = state

if __name__ == '__main__':
    app.run()