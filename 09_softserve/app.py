# Will Nzeuton, Danny Huang, Tim (Tim NG)
# What Departure 
# SoftDev
# K09 -- Flask
# 2024-09-24
# Time: N/A

from flask import Flask
import random

jobList = []

def randomOcc(str):
    
    infoByLine = str.split("\n")
    
    #split by commas
    conInfo = []
    for info in infoByLine:
        if '"' in info: # If quotation mark, only add the string starting from after that 
            info = info[1:]
            conAdd = info.split('",') # split by quotation mark and comma 
        else:
            conAdd = info.split(",")
        for i in conAdd:
            conInfo.append(i)
    conInfo.remove("Job Class") # Remove the unneeded information from csv
    conInfo.remove("Percentage")
    conInfo.remove("Total")
    conInfo.remove("99.8")
    
    jobDict = {}

    for x in range(0, len(conInfo) - 1, 2):
        jobDict[conInfo[x]] = float(conInfo[x+1])
    
    global jobList
    jobList = list(jobDict.keys())
        
    return (random.choices(list(jobDict), weights=[6.1, 5.0, 2.7, 1.7, 0.9, 1.6, 0.8, 6.1, 1.7, 5.5, 2.8, 2.3, 8.3, 3.7, 4, 10.2, 15.1, 0.6, 4.3, 3.8, 6.1, 6.5]))
    #^^ chooses a random key (occupation) from jobDict

with open("occupations.csv", "r") as file:
    f = file.read()
    randomOcc(f)
    
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    a = "What Departure Tim Ng, Danny Huang, Will Nzeuton"
    b = str(jobList)
    c = randomOcc(f)
    return f" {a} <br><br> {b} <br><br> {c}" # f string lets you display multiple strings in one line

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()