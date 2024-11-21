'''
Drizzling - Tim Ng, Endrit 
SoftDev
K23 - API Keys
2024-11-20
time spent: 45 minutes
'''
from flask import Flask, render_template, request
import os, urllib, json, requests

app = Flask(__name__)

def readapi(file_path): # will read the txt file to get api key
    with open(file_path, 'r') as file:
        api_key = file.read().strip()
    return api_key
api_key = readapi("key_nasa.txt")

@app.route("/")
def home_page():
    data = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}").json() # is a dictionary
    print(data)
    url = data["url"]
    return render_template("main.html", url = url)


if __name__ == "__main__":
    app.debug = True
    app.run()


