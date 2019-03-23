import sys, time, os, math, signal

from ..src import *

def KNN(inFile, cities):
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
                    currentDistance = distance(current, allCities[y])
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
            currentDistance = distance(cities[route[0]], cities[route[len(route)-1]])
            matrix[cities[route[0]]['city']][cities[route[len(route)-1]]['city']] = currentDistance
            matrix[cities[route[len(route)-1]]['city']][cities[route[0]]['city']] = currentDistance
        length += currentDistance
        if length < minLength:
            minLength = length
            order = [x for x in route]
            WriteFile(base, listCities)