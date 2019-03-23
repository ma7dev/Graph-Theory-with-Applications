# Nearest Neighbor
import sys, time, os, math, signal

def Distance(a,b):
    return int(round(math.sqrt((math.pow(a['i'] - b['i'],2))+(math.pow(a['j'] - b['j'],2)))))

def ReadFile(inFile):
    # base = os.path.basename(inFile)
    # print(base)
    # base = os.path.basename("data/"+inFile)
    # print(base)
    inFile = open("data/"+inFile, 'r')

    cities = []
    for eachLine in inFile:
        eachCity = eachLine.split()
        thisCity = {'city':int(eachCity[0]), 'i':int(eachCity[1]), 'j':int(eachCity[2])}
        cities.append(thisCity)
    inFile.close()
    return cities

def WriteFile(base, listCities):
    outFile = open(base + '.tour', 'w')
    outFile.write(str(minLength) + '\n')
    listCities = iter(order)
    for eachCity in listCities:
        outFile.write(str(eachCity) + '\n')
    outFile.close()