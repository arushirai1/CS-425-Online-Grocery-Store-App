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

