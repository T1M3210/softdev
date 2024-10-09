'''
JTC - Jayden Zhang, Caden Khuu, Tim Ng
SoftDev
K15 - Flask-Form - Learning and Experimenting with Flask GET and POST Methods.
2024-10-9
time spent: 1 hrs
'''

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template('login.html')


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    gvp = "The difference between the GET and POST methods lies in the way data is retrieved. GET checks the dictionary (args) for a key that matches the input, while POST essentially pushes your data to the servers POST dictionary (form). Both are sent as QueryStrings REQUESTS."
    if request.method == "POST": # if the method is POST, it should push that data into the form library
        username = request.form["username"] # POST uses request.form.
    elif request.method == "GET": # if the method is GET, it should ask for that data from the args library.
        username = request.args["username"] # GET uses request.form.
    
    return render_template('response.html', gvp=gvp, username=username, request=request.method) #response to a form submission
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
