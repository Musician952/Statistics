class DataFile:
    filePath = ""
    
    def read(self) -> list[str]:
        with open(self.filePath, 'r') as dataFile:
            return dataFile.readlines()
        
    def containsType(self, type) -> bool:
        containsBool = False
        containsInt = False
        containsFloat = False
        containsStr = False
        for value in self.read():
            try:
                type(value)
                if type == bool:
                    containsBool = True
                if type == int:
                    containsInt = True
                if type == float:
                    containsFloat = True
                if type == str:
                    containsStr = True
            except:
                continue
    
    def getNumberData(self) -> list[float]:
        ListFloat = []
        for line in self.read():
            try:
                ListFloat.append(float(line))
            except:
                continue
        return ListFloat
    
    def __init__(self, filePath: str) -> None:
        self.filePath = filePath

from variation import calculateRange
class NumberData:
    data = []

    def minValue(self) -> float:
        min = self.data[0]
        for num in self.data:
            if num < min:
                min = num
        return min
        
    def maxValue(self) -> float:
        max = self.data[0]
        for num in self.data:
            if num > max:
                max = num
        return max
    
    def range(self) -> float:
        return calculateRange(self.minValue, self.maxValue)

    def __init__(self, data: list[float]) -> None:
        self.data = data

class Class:
    lowerLimit = int
    upperLimit = int
    frequency = 0

    def getLowerBoundary(self) -> float:
        return float(self.lowerLimit - 0.5)
    
    def getUpperBoundary(self) -> float:
        return float(self.upperLimit + 0.5)
    
    def getMidPoint(self) -> float:
        return float((self.lowerLimit + self.upperLimit) / 2)

    def __init__(self, lowerLimit: int, upperLimit: int):
        self.lowerLimit = lowerLimit
        self.upperLimit = upperLimit

class ClassData:
    intData = None
    classCount = None
    classes = []

    def classWidth(self) -> int:
        return ((self.intData.getMaxValue() - 
                 self.intData.getMinValue()) // 
                 self.classCount) + 1

    def totalFrequency(self) -> int:
        totalFrequency = 0
        for statClass in self.classes:
            totalFrequency += statClass.frequency
        return totalFrequency
    
    def print(self):
        cumulativeFrequency = 0
        for statClass in self.classes:
            i = self.classes.index(statClass)

            print('\n')
            print(f'Class {i + 1} Limits = {statClass.lowerLimit} - {statClass.upperLimit}')
            print(f'Class {i + 1} Boundaries = {statClass.getLowerBoundary()} - {statClass.getUpperBoundary()}')
            print(f'Class {i + 1} Midpoint = {statClass.getMidPoint()}')
            print(f'Class {i + 1} Frequency = {statClass.frequency}')
            print(f'Class {i + 1} Relative Frequency = {self.getRelativeFrequency(i)}')
            cumulativeFrequency += statClass.frequency
            print(f'Class {i + 1} Cumulative Frequency = {self.getCumulativeFrequency(i)}')
    
    def getRelativeFrequency(self, classIndex: int) -> float:
        return self.classes[classIndex].frequency / self.totalFrequency()
    
    def getCumulativeFrequency(self, classIndex: int) -> int:
        cumulativeFrequency = 0
        for i in range(classIndex + 1):
            cumulativeFrequency += self.classes[i].frequency
        return cumulativeFrequency
    
    def createClasses(self,  
                      numOfClasses: int) -> list[Class]:
        classes = []

        lowerLimit = self.intData.getMinValue()
        upperLimit = (lowerLimit + self.classWidth()) - 1
        for i in range(numOfClasses):
            classes.append(Class(lowerLimit, upperLimit))
            lowerLimit += self.classWidth()
            upperLimit += self.classWidth()

        for num in self.intData.data:
            for statClass in classes:
                if num >= statClass.lowerLimit and num <= statClass.upperLimit:
                    statClass.frequency += 1

        return classes


    def __init__(self, intData: NumberData, classCount: int) -> None:
        self.intData = intData
        self.classCount = classCount
        self.classes = self.createClasses(classCount)

class StemAndLeaf:
    stem: int = None
    leaf: int = None

    def __init__(self, stem: int, leaf: int) -> None:
        self.stem = stem
        self.leaf = leaf

from enum import Enum

class DistributionShape(Enum):
    MOUND_SHAPED_SYMMETRIC = 1
    UNIFORM_OR_RECTANGULAR = 2
    SKEWED_LEFT = 3
    SKEWED_RIGHT = 4
    BIMODAL = 5

class AverageAndWeight():
    average: float = None
    weight: float = None

    def __init__(self, average: float, weight: float) -> None:
        self.average = average
        self.weight = weight