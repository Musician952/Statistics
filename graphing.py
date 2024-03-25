import matplotlib.pyplot as plt
from statTypes import DistributionShape
from enum import Enum

class BarDirection(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
class BarGraph:
    barDirection = None

    def __init__(self,
                 barDirection: BarDirection = BarDirection.VERTICAL) -> None:
        self.barDirection = barDirection

class CircleGraph:

    def __init__(self) -> None:
        pass

class DotPlot:
    points = []
    title = None

    def getXAndYPoints(self) -> list[list]:
        xPoints = []
        yPoints = []
        for value in self.points:
            if value not in xPoints:
                xPoints.append(value)
                count = 0
                for i in self.points:
                    if value == i:
                        count += 1
                yPoints.append(count)
        return [xPoints, yPoints]

    def show(self):
        xy = self.getXAndYPoints()
        plt.title = self.title
        plt.scatter(xy[0], xy[1])
        plt.show()

    def __init__(self, 
                 points: list[float], 
                 title: str = "") -> None:
        self.points = points
        self.title = title

class Histogram:
    yValues = []

    def distributionShape(self) -> DistributionShape:

        uniform = True

        prevNum = None
        for n in self.yValues:
            if prevNum == None:
                prevNum = n
            elif n != prevNum:
                uniform = False
                break

        if uniform == True:
            return DistributionShape.UNIFORM_OR_RECTANGULAR

        skewedLeft = True
        skewedRight = True
        moundShaped = True

        prevNum = None
        prevNum2 = None
        direction = None
        timesChangedDirections = 0
        for n in self.yValues:
            if prevNum == None:
                prevNum = n
                continue
            elif prevNum2 == None:
                prevNum2 = prevNum
                prevNum = n
                continue
            elif n < prevNum:
                if direction == "up":
                    timesChangedDirections += 1
                direction = "down"
                if prevNum < prevNum2:
                    skewedLeft = False
            elif n > prevNum:
                if direction == "down":
                    timesChangedDirections += 1
                direction = "up"
                if prevNum > prevNum2:
                    skewedRight = False

            prevNum2 = prevNum
            prevNum = n

        if timesChangedDirections > 1:
            moundShaped = False

        if skewedLeft:
            return DistributionShape.SKEWED_LEFT
        elif skewedRight:
            return DistributionShape.SKEWED_RIGHT
        elif moundShaped:
            return DistributionShape.MOUND_SHAPED_SYMMETRIC
        else:
            return DistributionShape.BIMODAL
    
    def __init__(self, yValues: list[float]) -> None:
        self.yValues = yValues

class Ogive:
    xPoints = []
    yPoints = []
    xLabel = None
    yLabel = None
    title = None

    def show(self):
        plt.title(self.title)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        plt.plot(self.xPoints, self.yPoints, 'o-')
        plt.show()

    def __init__(self, 
                 xPoints: list[float], 
                 yPoints: list[float],
                 xLabel: str = "",
                 yLabel: str = "",
                 title: str = "") -> None:
        self.xPoints = xPoints
        self.yPoints = yPoints
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.title = title

class ParetoChart:

    def __init__(self) -> None:
        pass

class TimeSeriesGraph:

    def __init__(self) -> None:
        pass