# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
#what does imported mean?
#clearly on debug mode because the name is in fact '__main__'
#we think that Flask has built in app settings that you can change by using a different name.
#It seems that the '__name__' is not just for show because if u get rid of a letter, it does not work, meaning it is not just cosmetic