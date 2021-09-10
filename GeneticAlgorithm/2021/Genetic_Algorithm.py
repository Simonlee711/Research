'''
A Python module that performs the Genetic Algorithm
'''
__author__ = 'Simon Lee, siaulee@ucsc.edu'
import random
import copy
import math
import matplotlib.pyplot as plt

#inititialization
POPULATION_SIZE = 20
CITIES_SIZE = 20
TOUR_SIZE = 21
NUM_EXECUTIONS = 9999
population = []
x = []
y = []

tour = [[0 for x in range(TOUR_SIZE)] for y in range(TOUR_SIZE)]
dCidade = [[0 for x in range(POPULATION_SIZE)] for y in range(POPULATION_SIZE)]
distances = [0 for x in range(POPULATION_SIZE)]
parentsOne = None
parentsTwo = None
costByExecution = []

''' Generates the first population'''
def generateFirstPopulation():
    # for each position, generates a new possible path
    for _ in range(1, POPULATION_SIZE + 1):
        generatePossiblePath()


''' Generate a new possible path for a population'''
def generatePossiblePath():
    path = []
    for _ in range(1, CITIES_SIZE + 1):
        # generates a new number between 1 - 20
        randomNum = random.randint(1,20)
        # while the generated number exists in the list, generates a new one
        while(numberExistsInPath(path, randomNum)):
            randomNum = random.randint(1, 20)
        path.append(randomNum)
    population.append(path)


''' Method to verify if the number is already in the path'''
def numberExistsInPath(path, number):
    for i in path:
        if i  == number:
            return True
    return False


''' Generates the X and Y arrays which represents the distances in the x 
and y axis used to calculate the identity matrix in the fitnress function'''
def generateXandY():
    for _ in range(CITIES_SIZE):
        randomNumber = random.random()
        randomNumber = round(randomNumber, 2)
        x.append(randomNumber)

        randomNumber = random.random()
        randomNumber = round(randomNumber, 2)
        y.append(randomNumber)

'''
Generates the tour matrix, which is the same matrix as the population
but with the first column duplicated at the end of it, afterall, the traveler
always have to arrive at the same place of where it started. The hamiltonian cycle
'''
def generateTour():
    global tour
    tour = copy.deepcopy(population)
    for ways in tour:
        first = ways[0]
        ways.append(first)

'''
Generates an array with the sum of each path in the population array based on the tour matrix
'''
def calculateDistances():
    global distances
    distances = [0 for x in range(CITIES_SIZE)]
    for i in range(len(population)):
        for j in range(len(population[i])):
            firstPos = 19 if tour[i][j] == 20 else tour[i][j]
            secondPos = 19 if tour[i][j+1] == 20 else tour[i][j+1]
            distances[i] += round(dCidade[firstPos][secondPos], 4)
    dict_dist = {i: distances[i] for i in range(0, len(distances))}
    distances = copy.deepcopy(dict_dist)
    return sorted(distances.items(), key=lambda kv: kv[1])


'''
Generates the identity matrux (dCidade) based on the x and y arrays
and then call the calculateDistances() method to generate the array with the sum
of each path to user later in the cycle process
'''
def FitnessFunction():
    for i in range(len(population)):
        for j in range(len(population)):
            dCidade[i][j] = round(math.sqrt(((x[i] -x[j]) ** 2) + ((y[i] - y[j]) ** 2)), 4)
    return calculateDistances()


'''
Performs the roulette function, generating two arrays with 5 parents each,
which will be used later to do the cycle process
'''
def rouletteFunction(sorted_x):
    global parentsOne
    global parentsTwo
    arr = []
    rouletteArr =[]
    for i in range(10):
        arr.append(sorted_x[i][0])
    for j in range(len(arr)):
        for _ in range(10 - j):
            rouletteArr.append(arr[j])
    parentsOne = createParents(rouletteArr)
    parentsTwo = createParents(rouletteArr)


'''
Auxiliary method used in the rouletteFunction() to generate the two parents array
'''
def createParents(rouletteArr):
    parentArr =[]
    for _ in range(5):
        parentArr.append(rouletteArr[random.randint(0, 54)])
    return parentArr

'''
makes the swap between two cities in the path with a 2% chance of mutation
'''
def mutate(matrix):
    for i in range(0, len(matrix)):
        for _ in range(0, len(matrix[i])):
            ranNum = random.randint(1,100)
            if ranNum >= 1 and ranNum <= 2:
                indexOne = random.randint(0,19)
                indexTwo = random.randint(0,19)
                auxOne = matrix[i][indexOne]
                auxTwo = matrix[i][indexTwo]
                matrix[i][indexOne] = auxTwo
                matrix[i][indexTwo] = auxOne


'''
Method used in the cycle to see if theres any duplication between cities
'''
def hasDuplicity(auxArray, usedIndexes):
    for i in range(len(auxArray)):
        for j in range(i, len(auxArray)):
            if i != j  and auxArray[i] == auxArray[j]:
                if i in usedIndexes:
                    return j
                else:
                    return i
    return -1


'''
Method that runs the cycle
1. For each two children in the children array, it makes a random swap between
   two children until theres no duplicated element
2. mutate the children that were generated
3. adds the children in the population array
'''

def Cycle(sorted_x):
    global population
    children = []

    for i in range(5):
        parentsOneAux = parentsOne[i]
        parentsTwoAux = parentsTwo[i]
        usedIndexes = []

        randomIndex = random.randint(0, POPULATION_SIZE - 1)
        usedIndexes.append(randomIndex)

        childOne = copy.deepcopy(population[parentsOneAux])
        childTwo = copy.deepcopy(population[parentsTwoAux])

        valAuxOne = childOne[randomIndex]
        valAuxTwo = childTwo[randomIndex]

        childOne[randomIndex] = valAuxTwo
        childTwo[randomIndex] = valAuxOne

        while(hasDuplicity(childOne, usedIndexes) != -1):
            newIndex = hasDuplicity(childOne, usedIndexes)
            usedIndexes.append(newIndex)

            valAuxOne = childOne[newIndex]
            valAuxTwo = childTwo[newIndex]

            childOne[newIndex] = valAuxTwo
            childTwo[newIndex] = valAuxOne
        
        #after generating the children, add them in the childrens array
        children.append(childOne)
        children.append(childTwo)

    #mutate children
    mutate(children)

    #make a temporary copy of the population before changing it
    tempPopulation = copy.deepcopy(population)

    for i in range(10):
        population[i] = copy.deepcopy(tempPopulation[sorted_x[i][0]])
    
    #adjust population
    for j in range(10, POPULATION_SIZE):
        population[j] = copy.deepcopy(children[j - 10])

def main():
    # runs once. generates a population, x and y, and tour matrix
    generateFirstPopulation()
    generateXandY()
    generateTour()

    #runs in a loop 0 - 9999
    for _ in range(NUM_EXECUTIONS):
        sorted_x = FitnessFunction()
        rouletteFunction(sorted_x)
        Cycle(sorted_x)
        generateTour() # generate the tour matrix again as the population is updated
        costByExecution.append(sorted_x[0][1]) # append the cost to the array of costs

    # generates a fitness value for the last population
    sorted_x = FitnessFunction()

    print('Total Population:' + POPULATION_SIZE)
    print('Mutation Probabiltiy: 2%')
    print('Number of Cities:' + CITIES_SIZE)
    print('Optimal path cost: %s' % sorted_x[0][1])
    print('Best Route' + population[0])

    #show the path through a graph
    plt.plot(tour[0])
    plt.plot(tour[0], 'ro')
    plt.axis([0,20,0,20])
    plt.show()

    # show the cost graph
    plt.plot(costByExecution)
    plt.show()

if __name__ == "__main__":
    main()