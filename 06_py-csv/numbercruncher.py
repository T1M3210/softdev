# Naf (Nafiyu Murtaza), Tim (Tim NG)
# Tinfoils
# SoftDev
# K06 -- CSV
# 2024-09-19
# Time: N/A

import random

def randomOcc(str):
    
    infoByLine = str.split("\n")
    
    #split by commas
    conInfo = []
    for info in infoByLine:
        if '"' in info:
            info = info[1:]
            conAdd = info.split('",')
        else:
            conAdd = info.split(",")
        for i in conAdd:
            conInfo.append(i)
    conInfo.remove("Job Class")
    conInfo.remove("Percentage")
    conInfo.remove("Total")
    conInfo.remove("99.8")
    
    jobDict = {}

    for x in range(0, len(conInfo) - 1, 2):
        jobDict[conInfo[x]] = conInfo[x+1]
    
    print (conInfo)
    print(jobDict)
    #print(random.choices(jobDict[x])) 
    

with open("occupations.csv", "r") as file:
    f = file.read()
    randomOcc(f)