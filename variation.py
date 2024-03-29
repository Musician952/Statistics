from math import sqrt
from statTypes import NumberData
from averages import calculateMean

def calculateRange(values: list[float]) -> float:
    return NumberData(values).range()

def calculateSampleVariance(values: list[float]) -> float:
    avgX = calculateMean(values)
    n = len(values)
    sumOfDeviationSquares = 0
    for x in values:
        sumOfDeviationSquares += (x - avgX)**2
    return sumOfDeviationSquares / (n - 1)

def calculatePopulationVariance(values: list[float]) -> float:
    avgMew = calculateMean(values)
    N = len(values)
    sumOfDeviationSquares = 0
    for x in values:
        sumOfDeviationSquares += (x - avgMew)**2
    return sumOfDeviationSquares / N

def calculateStandardDeviationOfSample(values: list[float]) -> float:
    return sqrt(calculateSampleVariance(values))

def calculateStandardDeviationOfPopulation(values: list[float]) -> float:
    return sqrt(calculatePopulationVariance(values))

def calculateCoefficientOfSampleVariation(values: list[float]) -> float:
    x = calculateMean(values)
    s = calculateStandardDeviationOfSample(values)
    return (s / x) * 100

def calculateCoefficientOfPopulationVariation(values: list[float]) -> float:
    x = calculateMean(values)
    s = calculateStandardDeviationOfPopulation(values)
    return (s / x) * 100

def __getDataset() -> list[float]:
    userInput = input('Input a dataset, seperated by commas(,) to determine variations and standard deviations: ')
    try:
        strValues = userInput.split(',')
        values: list[float] = []
        for string in strValues:
            values.append(float(string))
        return values
    except:
        print('Invalid input. Try again.')
        return __getDataset()

if __name__ == "__main__":
    dataset = __getDataset()
    numberData = NumberData(dataset)
    range = numberData.range()
    sumOfValues = numberData.sumOfAllValues()
    mean = calculateMean(dataset)
    sSquared = calculateSampleVariance(dataset)
    s = calculateStandardDeviationOfSample(dataset)
    CVs = calculateCoefficientOfSampleVariation(dataset)
    sigmaSquared = calculatePopulationVariance(dataset)
    sigma = calculateStandardDeviationOfPopulation(dataset)
    CVsigma = calculateCoefficientOfPopulationVariation(dataset)

    print(f'\nRange of Data: {range}')
    print(f'Sum of Data: {sumOfValues}')
    print(f'Mean of Data: {mean}')
    print(f'Sample Variance: {sSquared}')
    print(f'Standard Deviation of Sample: {s}')
    print(f'Coefficient of Sample Variation: {round(CVs,4)}%')
    print(f'Population Variance: {sigmaSquared}')
    print(f'Standard Deviation of Population: {sigma}')
    print(f'Coefficient of Population Variation: {round(CVsigma,4)}%\n')