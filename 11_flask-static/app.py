# Clyde 'Thluffy' Sinclair
# SoftDev
# Sep 2024

# DEMO
# basics of /static folder
import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

'''
@app.route("/static/foo.html")
def h():
    print("the __name__ of this module is... ")
    print(__name__)
    return str(random.random())
'''

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

