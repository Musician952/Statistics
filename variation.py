from math import sqrt
from statTypes import NumberData
from averages import calculateMean

def calculateRange(min: float, max: float) -> float:
    return max - min

def calculateStandardDeviationOfSample(values: list[float]) -> float:
    avgX = calculateMean(values)
    n = len(values)
    sumOfDeviationSquares = 0
    for x in values:
        sumOfDeviationSquares += (x - avgX)**2
    sampleVariance = sumOfDeviationSquares / (n - 1)
    return sqrt(sampleVariance)