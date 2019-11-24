import models.test_model as models
def init_data(db):
   add_user(db)
   add_customer(db)

def add_user(db):
    try:
        user=models.Users(
            user_id = 1000,
            username = "admin",
            password = "pass"
        )
        db.session.add(user)
        db.session.commit()
        print("User added. test id={}".format(user.user_id))
        return "User added"
    except Exception as e:
	    return(str(e))
def add_customer(db):
    try:
        customer=models.Customer(
            customer_ID = 1000,
            name = "Arushi",
            balance = 1100
        )
        db.session.add(customer)
        db.session.commit()
        return "Customer added. test id={}".format(customer.customer_ID)
        print("Customer added. test id={}".format(customer.customer_ID))
    except Exception as e:
	    return(str(e))