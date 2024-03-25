from graphing import DotPlot
from statTypes import DataFile
from statTypes import NumberData
from user_prompts import *

if __name__ == "__main__":
    data = DataFile(getDataFilePath())
    intData = NumberData(data.getNumberData())

    dotPlot = DotPlot(intData.data, "hi")
    dotPlot.show()