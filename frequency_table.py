from graphing import Histogram
from graphing import Ogive
from statTypes import ClassData
from statTypes import DataFile
from statTypes import DistributionShape
from statTypes import NumberData
from user_prompts import *

if __name__ == "__main__":
    data = DataFile(getDataFilePath())
    intData = NumberData(data.getNumberData())
    classData = ClassData(intData, getDesiredNumberOfClasses())

    print(f'Total Frequency = {classData.totalFrequency()}')
    print(f'Class Width: {classData.classWidth()}')
    classData.print()

    yValues = []
    for statClass in classData.classes:
        yValues.append(statClass.frequency)
    frequencyHistogram = Histogram(yValues)
    shape = frequencyHistogram.distributionShape()
    strShape = "Unknown"
    if shape == DistributionShape.UNIFORM_OR_RECTANGULAR:
        strShape = "Uniform or Rectangular"
    elif shape == DistributionShape.SKEWED_LEFT:
        strShape = "Skewed Left"
    elif shape == DistributionShape.SKEWED_RIGHT:
        strShape = "Skewed Right"
    elif shape == DistributionShape.MOUND_SHAPED_SYMMETRIC:
        strShape = "Mound-Shaped Symmetric"
    elif shape == DistributionShape.BIMODAL:
        strShape = "Bimodal"
    print(f'\nDistribution Shape: {strShape}\n')

    xPoints = [classData.classes[0].getLowerBoundary()]
    yPoints = [0]
    for i in range(classData.classes.__len__()):
        xPoints.append(classData.classes[i].getUpperBoundary())
        yPoints.append(classData.getCumulativeFrequency(i))
    ogive = Ogive(xPoints, yPoints, "Class Boundaries", "Cumulative Frequency", "Cumulative Frequency Ogive")
    ogive.show()