import sys, time, os, math, signal
import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt

# KNN algorithm
def ReadFileKNN(inFile):
    inFile = open(inFile, 'r')

    cities = []
    for eachLine in inFile:
        eachCity = eachLine.split()
        thisCity = {'city':int(eachCity[0]), 'i':int(eachCity[1]), 'j':int(eachCity[2])}
        cities.append(thisCity)
    inFile.close()
    return cities

def WriteFileKNN(outFile, order, minLength):
    outFile = open(outFile + '.tour', 'w')
    outFile.write(str(minLength) + '\n')
    listCities = iter(order)
    for eachCity in listCities:
        outFile.write(str(eachCity) + '\n')
    outFile.close()

def Distance(a,b):
    return int(round(math.sqrt((math.pow(a['i'] - b['i'],2))+(math.pow(a['j'] - b['j'],2)))))

def KNN(cities, inFile):
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
            WriteFileKNN(inFile, order, minLength)

# Genertic Algorithm
# This algorithm implementation was inspired by this blog: https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35
# I have used it to compute the right way for the Genertic Algorithm in Python
class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
    
    def distance(self, city):
        # xDis = self.x - city.x
        # yDis = self.y - city.y
        # distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return int(round(math.sqrt((math.pow(self.x - city.x,2))+(math.pow(self.y - city.y,2)))))
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness= 0.0
    
    def routeDistance(self):
        if self.distance ==0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromCity = self.route[i]
                toCity = None
                if i + 1 < len(self.route):
                    toCity = self.route[i + 1]
                else:
                    toCity = self.route[0]
                pathDistance += fromCity.distance(toCity)
            self.distance = pathDistance
        return self.distance
    
    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness
def ReadFileGA(inFile):
    inFile = open(inFile, 'r')
    cities = []
    for eachLine in inFile:
        eachCity = eachLine.split()
        thisCity = City(id=int(eachCity[0]), x=int(int(eachCity[1])), y=int(int(eachCity[2])))
        cities.append(thisCity)
    inFile.close()
    return cities

def WriteFileGA(outFile, listCities, minLength):
    outFile = open(outFile + '.tour', 'w')
    outFile.write(str(int(minLength)) + '\n')
    for eachCity in listCities:
        outFile.write(str(eachCity.id) + '\n')
    outFile.close()

def createRoute(cityList):
    route = random.sample(cityList, len(cityList))
    return route
def initialPopulation(popSize, cityList):
    population = []

    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population
def rankRoutes(population):
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)
def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults
def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool
def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        
    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child
def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,eliteSize):
        children.append(matingpool[i])
    
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children
def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual
def mutatePopulation(population, mutationRate):
    mutatedPop = []
    
    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop
def nextGeneration(currentGen, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGen)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration

def GA(inFile, population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    # print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))
    
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
    
    # print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    WriteFileGA(inFile, bestRoute, 1 / rankRoutes(pop)[0][1])
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
            cities = ReadFileKNN(inFile)
            KNN(cities, inFile)
        elif(sys.argv[1] == "ga"):
            cities = ReadFileGA(inFile)
            GA(inFile, population=cities, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
        else:
            print("Wrong arguments\n python3 [algorithm] [file]\n [algoirthm]:\n        knn = K-Nearest Neighbors\n        ga = Genertic Algorithm\n [file]: must be in data/ folder. \n")
    except TimeoutException:
        print("Program ended within "+str(selectedTime)+" minutes.")

    # Reset the alarm stuff.
    signal.alarm(0)
    signal.signal(signal.SIGALRM,OriginalHandler)

    print("Time:", (time.time()-startTime))