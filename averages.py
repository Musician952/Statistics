from statTypes import DataFile
from statTypes import AverageAndWeight
from user_prompts import *

# The average of all numerical values
def calculateMean(collection: list[float]) -> float:
    sum: float = 0.0
    count = len(collection)
    for num in collection:
        sum += num
    return sum / count

def calculateTrimmedMean(collection: list[float], trimPercentage: int = 5) -> float:
    decimalPercent = trimPercentage / 100
    deleteEndCount = round(len(collection) * decimalPercent)
    if (deleteEndCount * 2) >= len(collection):
        return None
    collection.sort()
    for i in range(deleteEndCount):
        collection.pop(0)
    newLen = len(collection)
    for i in range(deleteEndCount):
        collection.pop(newLen - 1)
        newLen = len(collection)
    return calculateMean(collection)

def calculateHarmonicMean(values: list[float]) -> float:
    dividend = len(values)
    divisor = 0.0
    for value in values:
        divisor += (1 / value)
    return dividend / divisor

def calculateWeightedAverage(AveragesAndWeights: list[AverageAndWeight]) -> float:    
    dividend = 0.0
    divisor = 0.0
    for pair in AveragesAndWeights:
        dividend += (pair.average * pair.weight)
        divisor += pair.weight
    return dividend / divisor

# The middle value (when collection can be sorted)
# Must pass an already sorted collection
def calculateMedian(collection: list[any]) -> any:
    count = len(collection)
    if count % 2 == 0:
        index1 = (count // 2) - 1
        index2 = index1 + 1
        return (collection[index1] + collection[index2]) / 2
    index = (count // 2) - 1
    return collection[index]

# The value that occurs the most (if applicable)
def calculateMode(collection: list[any]) -> any:
    highestCount: int = 0
    topValue: any = None
    for value in collection:
        count = collection.count(value)
        if count > highestCount:
            topValue = value
            highestCount = count
        elif count == highestCount and value != topValue:
            topValue = None
    return topValue

def __print(mean: float, median: any, mode: any, trimmedMean: float):
    print('\n'
          f'mean: {mean}\n'
          f'median: {median}\n'
          f'mode: {mode}\n'
          '\n'
          f'trimmed mean (5%): {trimmedMean}\n'
          '\n')

if __name__ == "__main__":
    userInput = input('For normal average calculations, input 1.\n'
          'For weighted averages, input 2.\n'
          'For harmonic average, input 3: ')

    if userInput == "1":
        dataPath = getDataFilePath()
        dataFile = DataFile(dataPath)
        collection = dataFile.getNumberData() # For now, only accepts float data
        collection.sort()

        mean = calculateMean(collection)
        median = calculateMedian(collection)
        mode = calculateMode(collection)
        trimmedMean = calculateTrimmedMean(collection)

        __print(mean, median, mode, trimmedMean)
    elif userInput == "2":
        averagesAndWeights = getAveragesAndWeights()
        weightedAverage = calculateWeightedAverage(averagesAndWeights)
        print(f'Weighted Average: {weightedAverage}')
    elif userInput == "3":
        averages = getListOfAverages()
        harmonicAverage = calculateHarmonicMean(averages)
        print(f'Harmonic Average: {harmonicAverage}')
              
    print('End of program.')