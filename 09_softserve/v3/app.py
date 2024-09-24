# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                   #where will this go?
    return "No hablo queso!"

app.debug = True # what is this??? It prints out debug mode and a pin in the terminal. How do you use the pin? 
app.run() # OHHHHHHHHH you can make edits live!! After we closed out of thonny confused, terminal said "restarting" which made us think it was automatically updating!!
