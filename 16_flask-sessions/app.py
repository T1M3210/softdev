# Margie Cao, Moyo Fagbuyi, Tim Ng
# System Level Programming
# SoftDev
# 2024-10-09
# o

from flask import Flask, render_template, request, session #this one stores like verything
import os 
from utl import ants


app = Flask(__name__)
app.secret_key = ants.poop()

@app.route("/",  methods=['GET','POST'])
def disp_loginpage():
    if 'username' and 'password' in session:
        return render_template('response.html')
    return render_template( 'login.html' ) #renders homepage


@app.route("/auth", methods=['POST'])
def post():
    session['username'] = request.form['username']
    session['password'] = request.form['password']
    name = session['username']
    return render_template('response.html', name = name)

#@app.route("/login", methods =['GET', 'POST'])
#def disp_loggedin():
#    return "hello"

@app.route("/logout", methods = ['GET', 'POST'])
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return render_template('login.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()