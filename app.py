#from app import app

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import db_methods
import pdb
import secrets
import helper_methods
import json

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

#db_methods.get_product_types(db)
#db_methods.get_product_info(db,'IL')
#db_methods.validate_login(db,'tpxyrc','3qkdWRHp')
#print(db_methods.get_payment_details(db, '1001'))
#print(db_methods.add_credit_card(db,"1001",5746384567932345,"123_state_st","Chicago","IL", 60647))
#print(db_methods.get_payment_details(db, '1001'))
#print(db_methods.is_available(db,1001, 2))
#print(db_methods.is_available(db,1001, 50000))
#print(db_methods.is_available(db,1001, 2372))
#print(db_methods.create_order(db,1001,5746384567932345, [{'product':1000, 'quantity': 5}, {'product':1001, 'quantity': 5},{'product':1002, 'quantity': 5}]))  
#print(db_methods.get_shipping_address(db,1001))
#print(db_methods.is_staff(db, 1001))
#print(db_methods.is_staff(db, 9003))
#print(db_methods.add_balance(db, 1001, 10))
#print(db_methods.remove_stock(db, 1001, 10))
#print(db_methods.add_products(db, "apple pie" , "food", 2.1, "null" , 800))
#print(db_methods.delete_product(db, 1086))
#print(db_methods.modify_product(db, 1000, 'banana', 'fruit', 2.1, 'null', 200))
#print(db_methods.add_address(db, 1001, "111 state ", "Chicago", "IL", 60647))

#session defaults
session={'user_id': 0, 'state': 'CA', 'cart': []}
#pdb.set_trace()


@app.route('/')
def index():
    form = login_form.LoginForm()
    session['cart'] = []

    return render_template('index.html', form = form)

@app.route('/delete-credit-card', methods=["GET"])
def delete_credit_card():
    credit_id = int(request.args.get("credit_id", 0))
    print("delete card")
    db_methods.delete_card(db, credit_id)

    return "success"

@app.route('/add-address', methods=["GET"])
def add_address():

    zip_code = int(request.args.get("inputZip", 0))
    street_address = str(request.args.get("inputAddress", 0))
    city = str(request.args.get("inputCity", 0))
    postal_state = str(request.args.get("inputState", 0))
    #insert method to add address
    print("Add Address")
    db_methods.add_address(db, session['user_id'], street_address, city, postal_state, zip_code)
    #db_methods.add_credit_card(db,session['user_id'],card_number,street_address,city,postal_state,zip_code)

    return "success"

@app.route('/delete-address', methods=["GET"])
def delete_address():
    addr_id = int(request.args.get("address_id", 0))
    tmp = session['addresses'][addr_id]
    #insert method to delete address
    print("Delete Address: ", tmp['street_address'])
    db_methods.delete_address(db, session['user_id'], tmp['street_address'], tmp['zip'])
    return "success"

@app.route('/submit-order', methods=["GET"])
def submit_order():
    addr_id = int(request.args.get("addr_id", 0))
    credit_id = int(request.args.get("credit_id", 0))
    tmp = session['addresses'][addr_id]
    #insert method to delete address
    print("submit_order")
    db_methods.create_order(db, session['user_id'], credit_id, session['cart'])
    return "success"

'''
Is in the format of:
[{'customer_id': 1001, 'card_number': 5650504164198020, 'street_address': None, 'city': None, 'postal_state': None, 'zip': None}, {'customer_id': 1001, 'card_number': 2546927393697540, 'street_address': None, 'city': None, 'postal_state': None, 'zip': None}, {'customer_id': 1001, 'card_number': 3936766883568310, 'street_address': None, 'city': None, 'postal_state': None, 'zip': None}]
'''
@app.route('/add-credit-card', methods=["GET"])
def add_credit_card():
    print(session['user_id'])

    card_number = int(request.args.get("card_number", 0))
    street_address = str(request.args.get("street_address", 0))
    city = str(request.args.get("city", 0))
    postal_state = str(request.args.get("postal_state", 0))
    zip_code = str(request.args.get("zip", 0))

    db_methods.add_credit_card(db,session['user_id'],card_number,street_address,city,postal_state,zip_code)

    return "success"

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

@app.route('/delete-product', methods=["GET"])
def delete_products():
    product_id = int(request.args.get("product_id", ""))
    db_methods.delete_product_pricing(db, product_id, session['state'])
    return "success"

@app.route('/update-product', methods=["GET"])
def update_products():
    productId = int(request.args.get("product_id", "0"))
    productName = str(request.args.get("productName", ""))
    productType = str(request.args.get("productType", 0))
    productSize = float(request.args.get("productSize", 0))
    alcoholContent = str(request.args.get("alcoholContent", 0))
    productState = str(request.args.get("product_state", "CA"))
    if(alcoholContent != ""):
        alcoholContent = float(alcoholContent)
    else:
        alcoholContent=0.0
    nutritionalValue = int(request.args.get("nutritionalValue", 0))
    productPrice = float(request.args.get("productPrice", 0.0))
    db_methods.update_products(db, productId, productName, productType, productSize, alcoholContent, nutritionalValue, productPrice, productState)

    return "success"

@app.route('/add-product', methods=["GET"])
def add_products():
    productName = str(request.args.get("productName", ""))
    productType = str(request.args.get("productType", 0))
    productSize = float(request.args.get("productSize", 0))
    alcoholContent = str(request.args.get("alcoholContent", 0))
    productState = str(request.args.get("product_state", "CA"))

    if(alcoholContent != ""):
        alcoholContent = float(alcoholContent)
    else:
        alcoholContent=0.0
    nutritionalValue = int(request.args.get("nutritionalValue", 0))
    productPrice = float(request.args.get("productPrice", 0.0))
    db_methods.add_products(db, productName, productType, productSize, alcoholContent, nutritionalValue, productPrice, productState)

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
    states_raw = db_methods.get_states(db)
    print(states_raw)
    states_str = json.dumps(states_raw)
    print(states_str)
    _states = json.loads(states_str)
    print(_states)
    add_session_variables(user_id, state)

    #pdb.set_trace()
    categories = db_methods.get_product_info(db, state)
    if(db_methods.is_staff(db, user_id)):

        product_types = db_methods.get_product_types(db)
        print(product_types)
        return render_template('staff_product.html', username= username, rows = categories, product_types=product_types, state=session['state'], temp=_states, password=password)
    
    #pdb.set_trace()
    balance = db_methods.get_balance(db, user_id)
    return render_template('products.html', state=state, username=username, rows=categories, balance=balance[0])

@app.route('/warehouse-view')
def view_warehouse():
    product_id = int(request.args.get("product_id", 0))

    warehouse_list = db_methods.fetch_capacity_for_product(db, product_id)
    print(warehouse_list)
    return render_template('warehouse_view.html', warehouses=warehouse_list, product_id=product_id)

@app.route('/update-stock')
def update_warehouse():
    product_id = int(request.args.get("product_id", 0))
    stock_quantity = int(request.args.get("stock_quantity", 0))
    warehouse_id = int(request.args.get("warehouse_id", 0))

    db_methods.update_stock(db, product_id, stock_quantity, warehouse_id)
    return "success"

@app.route('/view-cart', methods=["GET"])
def view_cart():
    print("arrived")
    return render_template('view_cart.html', cart = session['cart'])

@app.route('/payment-page', methods=["GET"])
def get_payment_page():
    cards = db_methods.get_payment_details(db, session['user_id'])
    session['addresses'] = db_methods.get_shipping_address(db, session['user_id'])
    #pdb.set_trace()
    return render_template('payment.html', credit_cards = cards, shipping_addresses = session['addresses'])

@app.route('/init-data')
def init_d():
    load_data.init_data(db)
    return "Initialized Data!"

@app.route('/heartbeat')
def test():
    return "Hello World"

@app.route('/logout')
def logout():
   # remove all session variable
    session['user_id'] = 0
    session['state'] = 'CA'
    form = login_form.LoginForm()
    session['cart'] = []

    return render_template('index.html', form = form)

def add_session_variables(user_id, state):
    session['user_id'] = user_id
    session['state'] = state

if __name__ == '__main__':
    app.run()