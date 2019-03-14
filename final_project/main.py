import sys, time, os, math, signal

# from src import *
# from models import *
# from models import *

def Distance(a,b):
    return int(round(math.sqrt((math.pow(a['i'] - b['i'],2))+(math.pow(a['j'] - b['j'],2)))))

def ReadFile(inFile):
    # base = os.path.basename(inFile)
    # print(base)
    # base = os.path.basename("data/"+inFile)
    # print(base)
    inFile = open(inFile, 'r')

    cities = []
    for eachLine in inFile:
        eachCity = eachLine.split()
        thisCity = {'city':int(eachCity[0]), 'i':int(eachCity[1]), 'j':int(eachCity[2])}
        cities.append(thisCity)
    inFile.close()
    return cities

def WriteFile(outFile, order, minLength):
    outFile = open(outFile + '.tour', 'w')
    outFile.write(str(minLength) + '\n')
    listCities = iter(order)
    for eachCity in listCities:
        outFile.write(str(eachCity) + '\n')
    outFile.close()

def KNN(inFile):
    cities = ReadFile(inFile)
    matrix = [[-1 for x in range(len(cities))] for y in range(len(cities))]
    minLength = sys.maxsize
    order = []
    for x in range(len(cities)):
        allCities = [z for z in cities]
        route = []
        route.append(allCities[x]['city'])
        allCities.remove(allCities[x])
        length = 0
        while len(allCities) > 0:
            current = cities[route[len(route)-1]]
            minDistance = sys.maxsize
            minCity = -1
            for y in range(len(allCities)):
                currentDistance = matrix[current['city']][allCities[y]['city']]
                if currentDistance == -1:
                    currentDistance = Distance(current, allCities[y])
                    matrix[current['city']][allCities[y]['city']] = currentDistance
                    matrix[allCities[y]['city']][current['city']] = currentDistance
                if currentDistance < minDistance:
                    minDistance = currentDistance
                    minCity = allCities[y]
            route.append(minCity['city'])
            allCities.remove(minCity)
            length += minDistance
        currentDistance = matrix[cities[route[0]]['city']][cities[route[len(route)-1]]['city']]
        if currentDistance == -1:
            currentDistance = Distance(cities[route[0]], cities[route[len(route)-1]])
            matrix[cities[route[0]]['city']][cities[route[len(route)-1]]['city']] = currentDistance
            matrix[cities[route[len(route)-1]]['city']][cities[route[0]]['city']] = currentDistance
        length += currentDistance
        if length < minLength:
            minLength = length
            order = [x for x in route]
            WriteFile(inFile, order, minLength)

def KNN(inFile):
    cities = ReadFile(inFile)
    matrix = [[-1 for x in range(len(cities))] for y in range(len(cities))]
    minLength = sys.maxsize
    order = []
    for x in range(len(cities)):
        allCities = [z for z in cities]
        route = []
        route.append(allCities[x]['city'])
        allCities.remove(allCities[x])
        length = 0
        while len(allCities) > 0:
            current = cities[route[len(route)-1]]
            minDistance = sys.maxsize
            minCity = -1
            for y in range(len(allCities)):
                currentDistance = matrix[current['city']][allCities[y]['city']]
                if currentDistance == -1:
                    currentDistance = Distance(current, allCities[y])
                    matrix[current['city']][allCities[y]['city']] = currentDistance
                    matrix[allCities[y]['city']][current['city']] = currentDistance
                if currentDistance < minDistance:
                    minDistance = currentDistance
                    minCity = allCities[y]
            route.append(minCity['city'])
            allCities.remove(minCity)
            length += minDistance
        currentDistance = matrix[cities[route[0]]['city']][cities[route[len(route)-1]]['city']]
        if currentDistance == -1:
            currentDistance = Distance(cities[route[0]], cities[route[len(route)-1]])
            matrix[cities[route[0]]['city']][cities[route[len(route)-1]]['city']] = currentDistance
            matrix[cities[route[len(route)-1]]['city']][cities[route[0]]['city']] = currentDistance
        length += currentDistance
        if length < minLength:
            minLength = length
            order = [x for x in route]
            WriteFile(inFile, order, minLength)

if __name__ == "__main__":
    startTime = time.time()

    # Timout code copied from https://stackoverflow.com/questions/24921527/option-for-ssh-to-timeout-after-a-short-time-clientalive-connecttimeout-dont/24921763#24921763
    class TimeoutException(Exception):   # Custom exception class
        pass

    def TimeoutHandler(signum, frame):   # Custom signal handler
        raise TimeoutException

    # Change the behavior of SIGALRM
    OriginalHandler = signal.signal(signal.SIGALRM,TimeoutHandler)

    # Start the timer. Once 5 seconds are over, a SIGALRM signal is sent.
    selectedTime = 5
    if(len(sys.argv[1:]) == 3):
        selectedTime = int(sys.argv[3])
    stopTime = (selectedTime*60)-1
    print(stopTime)
    signal.alarm(stopTime)

    # This try/except loop ensures that you'll catch TimeoutException when it's sent.
    try:
        inFile = sys.argv[2]
        if(sys.argv[1] == "knn"):
            KNN(inFile)
        elif(sys.argv[1] == "ga"):
            GA(inFile)
        else:
            print("Wrong arguments\n python3 [algorithm] [file]\n [algoirthm]:\n        knn = K-Nearest Neighbors\n        ga = Genertic Algorithm\n [file]: must be in data/ folder. \n")
    except TimeoutException:
        print("Program ended within "+str(selectedTime)+" minutes.")

    # Reset the alarm stuff.
    signal.alarm(0)
    signal.signal(signal.SIGALRM,OriginalHandler)

    print("Time:", (time.time()-startTime))