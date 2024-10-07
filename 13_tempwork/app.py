# Princeden, Tim 
# SegFault
# SoftDev
# K13 -- Combine
# 2024-09-30
# Time: N/A

from flask import Flask, render_template
app = Flask(__name__)

import csv    # Import required libraries
import random

all_occupations = []  #Creates list of dictionaries for all occupations 

with open("occupations.csv", mode = "r") as file:  # Opens CSV File
    csvFile = csv.reader(file)   # Reads CSV File
    pSum = 0  #Creates pSum variable which will be used as divider
    for line in csvFile:   #Loops through CSV object
        if not(line[0] == "Job Class" or line[0] == "Total"):   #Takes out first and last row
            pSum += float(line[1])*10   #Calculates pSum value
            all_occupations.append({"Job Class": line[0], "Percentage": float(line[1]), "Link": str(line[2]), "pSum": pSum})  #Creates dictionary and adds to list
selected_job = ''        
job = random.randint(0, 998)   #Random Integer
for i in all_occupations:  #Loops through list
    if job < i["pSum"]:   #Finds range the random integer is in
        selected_job = i #Prints the selected occupation
        break   #Breaks out of loop as range was found
print(selected_job)

@app.route("/")
def hello_world():
    return "No hablo queso!"

@app.route("/wdywtbwygp") 
def test_tmplt():
    selected_job = ''        
    job = random.randint(0, 998)   #Random Integer
    for i in all_occupations:  #Loops through list
        if job < i["pSum"]:   #Finds range the random integer is in
            selected_job = i #Prints the selected occupation
            break   #Breaks out of loop as range was found
    print(selected_job)
    return render_template('tablified.html', title = "Occupations", all_occupations = all_occupations, selected_job = selected_job)


if __name__ == "__main__":
    app.debug = True
    app.run()