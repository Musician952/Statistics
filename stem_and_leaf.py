from statTypes import DataFile
from statTypes import NumberData
from statTypes import StemAndLeaf
from user_prompts import *

stem = [] # 1D list
leaf = [] # 2D list

if __name__ == "__main__":
    data = DataFile(getDataFilePath())
    numData = NumberData(data.getNumberData())
    numData.data.sort()

    placement = getDesiredStemDisplacement()
    #
    # We can split anywhere so long as there is at
    # least a tenth on each side of the decimal point.
    #
    # Not perfect, but good enough for most datasets.
    # Leaving it with some error for the future.
    # Need to get onto the next thing.
    #
    stemsAndLeaves: list[StemAndLeaf] = []
    if placement > 0:
        for i in range(len(numData.data)):
            num = numData.data[i]
            num /= (10**placement)
            num = round(num, placement)
            stem = str(int(num // 1))
            leaf = str(round(num % 1, placement)).replace('0.','')
            stemsAndLeaves.append(StemAndLeaf(stem, leaf))
            #print(f'{num} - STEM: {stem} - LEAF: {leaf}')
    elif placement < 0:
        negativePlacement = placement * (-1)
        for i in range(len(numData.data)):
            num = numData.data[i]
            num *= (10**negativePlacement)
            num = round(num, negativePlacement)
            stem = str(int(num // 1))
            leaf = str(round(num % 1, negativePlacement)).replace('0.','')
            stemsAndLeaves.append(StemAndLeaf(stem, leaf))
            #print(f'{num} - STEM: {stem} - LEAF: {leaf}')
    else:
        for i in range(len(numData.data)):
            num = numData.data[i]
            stem = str(int(num // 1))
            leaf = str(round(num % 1, 7)).replace('0.','')
            stemsAndLeaves.append(StemAndLeaf(stem, leaf))

    totalStems: list[int] = []
    totalLeaves: list[int] = []
    for pair in stemsAndLeaves:
        if not pair.stem in totalStems:
            groupLeaves = []
            for pair2 in stemsAndLeaves:
                if pair2.stem == pair.stem:
                    groupLeaves.append(pair2.leaf)
            totalStems.append(pair.stem)
            totalLeaves.append(groupLeaves)

    # Print the stem and leaf plot
    print('\n')
    print('stem  |   leaf')
    print('________________________________')
    for i in range(len(totalStems)):
        print(f'{totalStems[i]}     |   {str(totalLeaves[i]).replace('[','').
                                         replace(']','').replace(',','').
                                         replace('\'','')}')
    print('\n')