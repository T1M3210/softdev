from flask import Flask, render_template, request, session #this one stores like verything
import os

app = Flask(__name__)

def poop():
    app.secret_key = os.urandom(32) # make random sequence for key
    return app.secret_key