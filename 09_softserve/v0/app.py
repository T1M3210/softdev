# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # creates app with default name of '__main__'

@app.route("/")                # defines app location
def hello_world():
    print(__name__)            # prints out '__main__'
    return "No hablo queso!"   # Displays the given text on the app

app.run()                      # Runs the app 
                
