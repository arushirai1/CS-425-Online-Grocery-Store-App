To clone the repo:

```git clone https://bitbucket.org/arai4/online-grocery-store/ ```

Then create a virtual env to keep our dependencies isolated by running the following commands:
```python3 -m venv venv```

and activate it:
```source venv/bin/activate```

It should look like this:
![alt-text][./info.png "Title"]

Now, run ```pip3 install -r requirements.txt``` to install Flask and it's dependencies!

If you install anything use pip3, do ```pip3 freeze > requirements.txt```. This is also why activating your virtual env is important. We only want to store required dependencies!

Run the app by:
```python3 app.py```

#Set up DB
#in psql terminal
create database grocery;

#run in bash
export DATABASE_URL="postgresql://localhost/grocery"
export APP_SETTINGS="config.DevelopmentConfig"

"Note that Flask-SQLAlchemy uses a "snake case" naming convention for database tables by default. For the User model above, the corresponding table in the database will be named user. For a AddressAndPhone model class, the table would be named address_and_phone. If you prefer to choose your own table names, you can add an attribute named __tablename__ to the model class, set to the desired name as a string." - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database





