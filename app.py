#from app import app

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import db_methods
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models.test_model as models
import load_data
import login_form
@app.route('/')
def index():
    form = login_form.LoginForm()
    return render_template('index.html', form = form)

@app.route('/products', methods=["GET"])
def view_products():
    username = request.args.get("username", "no")
    password = request.args.get("password", "no")
    if not db_methods.validate_login(username, password):
        form = login_form.LoginForm()
        return render_template('index.html', form = form)
    state = request.args.get("state_select", "CA")
    products = [{'name': 'Apple'},{'name': 'Ice Cream'}, {'name': 'Banana'} ]
    return render_template('products.html', state=state, username=username, products=products)

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

if __name__ == '__main__':
    app.run()