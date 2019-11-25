
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

