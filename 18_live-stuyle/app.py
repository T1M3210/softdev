# Margie Cao, Moyo Fagbuyi, Tim Ng
# System Level Programming
# K18 - live css page
# SoftDev
# 2024-10-16
# Time Spent: 1 hour

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def display():
    return render_template('index.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()