# Moyo Fagbuyi, Tim Ng, Margie Cao
# Systems Level Programming
# SoftDev
# K06 -- 
# 2024-09-17
# time spent: 1

import random

def duckies(str):
    devos = str.split("@@@")
    devos.remove("")
    info = []
    listdict = []
    for x in range(len(devos)):
        info = info + devos[x].split("$$$")
    for x in range(0, len(info), 3): 
        dict = {"pd": 1, "devo": "temp", "ducky": "temp"}
        dict["pd"] = info[x]
        dict["devo"] = info[x+1]
        dict["ducky"] = info[x+2]
        listdict.append(dict)
    x = random.randint(0, len(listdict)-1)
    print(listdict[x]["devo"] + " " + listdict[x]["pd"] + " " + listdict[x]["ducky"])

x = open("krewes.txt", "r")
duckies(x.read())