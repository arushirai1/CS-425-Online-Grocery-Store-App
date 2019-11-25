
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
		sql_string="select product_id,product_name, price from Product natural join Pricing where product_type = '"+key+"' AND postal_state= '"+ stateArg+"';"
		results = db.engine.execute(sql_string)
		for row in results:
			product_id = row.product_id
			product_name = row.product_name
			price = row.price
			product_data = {'product_ID': product_id, 'name': product_name, 'price': price}
			products[count]['items'].append(product_data)
		count=count+1


	return products
#[{column: value for column, value in rowproxy.items()} for rowproxy in resultproxy]

def get_payment_details(db, user_id):
	sql_string="select * from Credit_card where customer_id=" + user_id + ";"
	results = db.engine.execute(sql_string)
	products=[]
	for row in results:
		product_data = {'customer_id': row.customer_id, 'card_number': row.card_number, 'street_address': row.street_address, 'city': row.city, 'postal_state': row.postal_state, 'zip': row.zip}
		products.append(product_data)

	return products 

def add_credit_card(db,user_id,card_number,street_address,city,state,zip_code):
	sql_max="Select max(credit_id) from Credit_card;"
	max_id=db.engine.execute(sql_max)
	for row in max_id:   #loop only runs once
		next_primary_key=row.max +1  
	
	sql_string="insert into Credit_card values( "+ str(next_primary_key)+ "," + str(user_id) + "," + str(card_number) + ",'"  + str(street_address) + "','"  + str(city)+ "','"  + str(state) + "',"  + str(zip_code) + ");"
	db.engine.execute(sql_string)



def is_available(db,product_id, quantity):
    sql_string="select product_ID,sum(quantity) from Stock group by product_ID having product_ID=" +str(product_id)+ ";"
    results=db.engine.execute(sql_string)
    for row in results:
    	if row.sum>=quantity:
    		return True
    return False

def create_order(db, customer_id, card_number, cart_content):	
	sql_max="Select max(order_id) from Orders;"
	max_id=db.engine.execute(sql_max)
	for row in max_id:   #loop only runs once
		next_primary_key=row.max +1 
	

	sql_string="insert into Orders values( "+ str(next_primary_key)+ "," + str(customer_id) + "," + str(card_number)   + ");"
	db.engine.execute(sql_string)

	#for item in cart_content:
	#	print (item['product'])
	#	print (item['quantity'])
	for item in cart_content:
		product=item["product"] 
		quantity=item["quantity"]
		sql_order_items="insert into Order_items values(" + str(next_primary_key) + "," + str(product) + "," + str(quantity) + ");"


