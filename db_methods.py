
import pdb

def validate_login(db,username, password):
    sql_string="select u_id,username,user_password from Users;"
    results= db.engine.execute(sql_string)
    for row in results:
        user_id=row.u_id
        #pdb.set_trace()
        if username == row.username and password == row.user_password:
            return user_id
    return 0


def get_products(db):
	sql_string = "select * from Product;"
	return db.engine.execute(sql_string)

def get_product_types(db):
	sql_string="select distinct product_type from Product;"
	a=[]
	results = db.engine.execute(sql_string)
	for row in results:
		a.append(row.product_type)

	return a

def get_product_info(db, stateArg):
	keys = get_product_types(db)
	products = []
	#products = dict.fromkeys(keys)

	#create empty product list
	for key in keys:
		newdict = {'category': key, 'items':[]}
		products.append(newdict)

	#pdb.set_trace()
	#fill product list
	count = 0

	for key in keys:
		sql_string="select product_id, product_type, size, product_name, alcohol_content, nutritional_value, price from Product natural join Pricing where product_type = '"+key+"' AND postal_state= '"+ stateArg+"';"
		results = db.engine.execute(sql_string)
		for row in results:
			product_id = row.product_id
			product_name = row.product_name
			price = row.price

			product_data = {'product_ID': product_id, 'name': product_name, 'price': price, 'product_type': row.product_type, 'size': row.size, 'alcohol_content': row.alcohol_content, 'nutritional_value': row.nutritional_value}
			if(product_data['alcohol_content'] == None):
				product_data['alcohol_content'] = 0.0
			products[count]['items'].append(product_data)
		count=count+1


	return products
#[{column: value for column, value in rowproxy.items()} for rowproxy in resultproxy]

def get_payment_details(db, user_id):
	sql_string="select * from credit_card where customer_id=" + str(user_id) + ";"
	print(sql_string)
	results = db.engine.execute(sql_string)
	products=[]
	for row in results:
		product_data = {'customer_id': row.customer_id, 'credit_id': row.credit_id, 'card_number': row.card_number, 'street_address': row.street_address, 'city': row.city, 'postal_state': row.postal_state, 'zip': row.zip}
		products.append(product_data)

	return products 

def add_credit_card(db,user_id,card_number,street_address,city,state,zip_code):
	sql_max="Select max(credit_id) from Credit_card;"
	max_id=db.engine.execute(sql_max)
	print("test")
	row=max_id.fetchone()  #loop only runs once
	next_primary_key=row.max +1  
	
	sql_string="insert into Credit_card values( "+ str(next_primary_key)+ "," + str(user_id) + "," + str(card_number) + ",'"  + str(street_address) + "','"  + str(city)+ "','"  + str(state) + "',"  + str(zip_code) + ");"

	db.engine.execute(sql_string)

def delete_card(db, credit_id):
	sql_string="delete from credit_card where credit_id="+str(credit_id)+";"
	db.engine.execute(sql_string)

def delete_address(db, customer_id, street_address, zip_code):
	sql_string="delete from customer_address where customer_id="+str(customer_id)+" and street_address='" + str(street_address)+"' and zip="+str(zip_code)+";"
	db.engine.execute(sql_string)

def max_quantity(db, product_id):
	sql_string="select product_ID,sum(quantity) from Stock group by product_ID having product_ID=" +str(product_id)+ ";"
	row=db.engine.execute(sql_string).fetchone()
	return row.sum

def is_available(db,product_id, quantity):
    sql_string="select product_ID,sum(quantity) from Stock group by product_ID having product_ID=" +str(product_id)+ ";"
    results=db.engine.execute(sql_string)
    for row in results:
    	if row.sum>=quantity:
    		return True
    return False

def get_card_number(db, card_id):
	sql_string="select card_number from credit_card where credit_id=" + str(card_id) + ";"
	result=db.engine.execute(sql_string)
	row = result.fetchone()
	print(row.card_number)
	return row.card_number

def create_order(db, customer_id, card_id, cart_content):	
	print(customer_id, card_id, cart_content)
	sql_max="Select max(order_id) from Orders;"
	max_id=db.engine.execute(sql_max)
	#next_primary_key=0
	row = max_id.fetchone()
	next_primary_key=row.max +1 
	
	card_number = get_card_number(db, card_id)

	sql_string="insert into Orders values( "+ str(next_primary_key)+ "," + str(customer_id) + "," + str(card_number)   + ");"
	db.engine.execute(sql_string)

	for item in cart_content:
		product=item["product_id"] 
		quantity=item["quantity"]
		print(product,quantity)
		sql_order_items="insert into Order_items values(" + str(next_primary_key) + "," + str(product) + "," + str(quantity) + ");"
		db.engine.execute(sql_order_items)

def get_shipping_address(db, user_id):
	sql_string="select street_address,city,postal_state,zip from Customer_address where customer_id=" + str(user_id) + ";"
	results = db.engine.execute(sql_string)
	products=[]
	count=0
	for row in results:
		product_data = {'address_id': count, 'street_address': row.street_address, 'city': row.city, 'postal_state': row.postal_state, 'zip': row.zip}
		products.append(product_data)
		count+=1

	return products

def is_staff(db, user_id):
	sql_string="select staff_id from Staff;"
	results= db.engine.execute(sql_string)
	for row in results:
		if user_id == row.staff_id:
			return True
	return False

def add_balance(db,user_id,order_total):
	sql_curr_balance="Select balance from Customer where customer_id=" + str(user_id) + ";"
	curr_balance_results=db.engine.execute(sql_curr_balance)
	for row in curr_balance_results:
		curr_balance=row.balance
		#print("before balance " + str(curr_balance))
	new_balance=curr_balance+order_total
	#print(new_balance)
	sql_string="Update Customer set balance ="+str(new_balance)+" where customer_id ="+ str(user_id)+";"
	results=db.engine.execute(sql_string)
	#curr_balance_results=db.engine.execute(sql_curr_balance)  #to test new balance
	#for row in curr_balance_results:
	#	print("new balance " + str(row.balance))
def remove_stock(db, product_id, order_quantity):
    #select warehouse_id with most quantity of product
    sql_a = "select * from stock where product_id = " + str(product_id) + " order by quantity desc;"
    warehouses = db.engine.execute(sql_a)
    warehouse = warehouses.fetchone()
    print(warehouse)
    #update quantity in database
    new_quantity = warehouse.quantity - order_quantity
    if new_quantity >=0:
        sql_b = "update stock set quantity = " + str(new_quantity) + " where warehouse_id = " + str(warehouse.warehouse_id) + "and product_id = " + str(product_id) + ";"
        db.engine.execute(sql_b)
        sql_check="select * from Stock where warehouse_id = " + str(warehouse.warehouse_id) + "and product_id = " + str(product_id) + ";"
        results=db.engine.execute(sql_check)
        print(results.fetchone())
        return True
    else:
        return False

def get_balance(db, user_id):
	sql_string = "select balance from customer where customer_id="+ str(user_id)+";"
	return db.engine.execute(sql_string).fetchone()

def fetch_capacity(db):
	current_capacities = []
	sql_string = "select warehouse_id, sum(quantity) from (select * from warehouse, product) as q natural left outer join stock group by warehouse_id ORDER BY warehouse_id;"
	results = db.engine.execute(sql_string)	

	for row in results:
		item = {'warehouse_id': row.warehouse_id, 'current_capacity': row.sum}
		current_capacities.append(item)
	return current_capacities

def fetch_all_warehouses(db):
	sql_string = "SELECT * FROM warehouse ORDER BY warehouse_id;"
	results = db.engine.execute(sql_string)

	warehouses = []
	for row in results:
		warehouse = {'warehouse_id' : row.warehouse_id, 'max_capacity': row.capacity, 'address': row.street_address + ', ' + row.city + ' ' + row.postal_state + ' ' + str(row.zip) }
		warehouses.append(warehouse)
	return warehouses

def fetch_capacity_for_product(db, product_id):
	sql_string = "select warehouse_id, product_name, coalesce(quantity, 0) as quantity from (select * from warehouse, product) as q natural left outer join stock where product_id=" + str(product_id) + " ORDER BY warehouse_id;"
	results =  db.engine.execute(sql_string)
	product_warehouse_list = []
	warehouses = fetch_capacity(db)
	warehouse_info = fetch_all_warehouses(db)
	for row in results:
		item = {'product_name': row.product_name, 'warehouse_id': row.warehouse_id, 'quantity': row.quantity, 'current_cap': str(warehouses[row.warehouse_id-1]['current_capacity']), 'max_capacity': str(warehouse_info[row.warehouse_id - 1]['max_capacity']), 'address': warehouse_info[row.warehouse_id - 1]['address']}
		product_warehouse_list.append(item)

	return product_warehouse_list

def update_stock(db, product_id, stock_quantity, warehouse_id):
	sql_string = "select count(*) from stock WHERE product_id="+ str(product_id)+" and warehouse_id="+ str(warehouse_id) +";"
	row = db.engine.execute(sql_string).fetchone()
	count = row.count
	if(count == 0):
		sql_string = "INSERT INTO stock values (" +str(warehouse_id) + ", " + str(product_id) + ", "+ str(stock_quantity) +  ");"
	else:
		sql_string = "UPDATE stock SET quantity=" +str(stock_quantity)+  " WHERE product_id="+ str(product_id)+" and warehouse_id="+ str(warehouse_id) +";"
	print("SQL Str", sql_string)
	db.engine.execute(sql_string)

'''
def fetch_products_in_warehouses(db):
	sql_string = 'select warehouse_id, product_id, product_name from (warehouse natural join stock) natural join product;'
	results = db.engine.execute(sql_string)
	warehouses = fetch_all_warehouses(db)
	products_warehouse_join = []
	#prepopulate
	for w in warehouses:
		tmp = {'warehouse_id': w['warehouse_id'], 'products'}
	for row in results:
		[{}]
		warehouses.append(warehouse)
	return products_warehouse_join
'''

def update_products(db, product_id, product_name, product_type, size, alcohol_content, nutritional_value, price, state):
	sql_string = "UPDATE product SET product_name='"+str(product_name) + "', product_type='" + str(product_type) +  "', size=" + str(size) +  ", alcohol_content=" + str(alcohol_content) +  ", nutritional_value=" + str(nutritional_value) +"where product_id=" + str(product_id)+";"
	db.engine.execute(sql_string)

	sql_string = "UPDATE pricing SET price="+str(price)+" where product_id="+str(product_id)+" and postal_state='"+str(state)+"';"
	db.engine.execute(sql_string)

def get_states(db):
	sql_string = "SELECT distinct postal_state FROM pricing;"
	a=[]
	results = db.engine.execute(sql_string)
	for row in results:
		a.append(row.postal_state)
	return a


def add_products(db, product_name, product_type, size, alcohol_content, nutritional_value, price, state):
	sql_max="Select max(product_id) from Product;"
	max_id=db.engine.execute(sql_max)
	row = max_id.fetchone()
	next_primary_key=row.max +1 
	sql_string="insert into Product values( "+ str(next_primary_key)+ ",'" + str(product_name) + "','" + str(product_type) +  "'," + str(size) +  "," + str(alcohol_content) +  "," + str(nutritional_value) + ");"
	db.engine.execute(sql_string)
	sql_string="insert into Pricing values( "+ str(next_primary_key)+ ",'" + str(state) + "'," + str(price) +");"
	db.engine.execute(sql_string)

	sql_check ="select * from Product where product_id=" +str(next_primary_key)+";"
	results=db.engine.execute(sql_check)
	print(results.fetchone())

def delete_product_pricing(db, product_id, state):
	sql_string="Delete from pricing where product_id=" + str(product_id) + " and postal_state='" + str(state) + "';"
	db.engine.execute(sql_string)

def delete_product(db, product_id):
	sql_a="Select * from product where product_id ="+ str(product_id) + ";"
	product_info=db.engine.execute(sql_a)
	row = product_info.fetchone()
	if row.product_id != None:
		sql_string="Delete from Product where product_id=" + str(product_id) + ";"
		db.engine.execute(sql_string)

		sql_check="Select from Product where product_id=" + str(product_id) + ";"
		results=db.engine.execute(sql_check)
		print(results.fetchone())
		return True
	return False
def modify_product(db, product_id, new_product_name, new_product_type, new_size, new_alcohol_content, new_nutritional_value):
	sql_string="update Product set product_name= '" + str(new_product_name) + "', product_type = '" + str(new_product_type) + "' , size =" + str(new_size) + ", alcohol_content=" +str(new_alcohol_content) + ", nutritional_value =" +str(new_nutritional_value) + ";"
	db.engine.execute(sql_string)
	sql_check="select * from Product where product_id=" +str(product_id) + ";"
	results=db.engine.execute(sql_check)
	print(results.fetchone())

def add_address(db, customer_id, street_address, city, state, zip_code):
	sql_string="insert into Customer_address values( "+ str(customer_id)+ ",'" + str(street_address) + "','" + str(city) +  "','" + str(state) +  "'," + str(zip_code) + ");"
	db.engine.execute(sql_string)
	sql_check="select * from Customer_address where customer_id=" +str(customer_id) + ";"
	results=db.engine.execute(sql_check)
	for row in results:
		print(row)
	#print(results.fetchone())

