from statTypes import AverageAndWeight

def getDataFilePath() -> str:
    return input('\nEnter the full path of the data file: ')

def getDesiredNumberOfClasses() -> int:
    try:
        numOfClasses = int(input('\nPlease enter desired number of classes: '))
        return numOfClasses
    except:
        print('Must enter a whole number. Try again.')
        return getDesiredNumberOfClasses()
    
def getDesiredStemDisplacement() -> int:
    answer = input('\nHow many decimal places do you want your stems to shift?\n'
                   'Use positive numbers for positive displacement.\n'
                   'Use negative numbers for negative displacement.\n'
                   'Your displacement: ')
    
    try:
        return int(answer)
    except:
        print('Placement must be either a positive, negative or neutral whole integer. Try again.')
        return getDesiredStemDisplacement()

def getAveragesAndWeights() -> list[AverageAndWeight]:
    collection: list[AverageAndWeight] = []

    continueLoop = True
    while continueLoop:
        average = input('Enter Average: ')
        weight = input('Enter Weight: ')

        try:
            collection.append(
                AverageAndWeight(
                    float(average), float(weight)))
        except:
            print('Must enter decimal numbers. Please try again.')
            continue

        userInput = input('Add another average? (Y/n): ').upper()
        if userInput != "Y" and userInput != "YES":
            continueLoop = False
    
    return collection

def getListOfAverages() -> list[float]:
    collection: list[float] = []

    continueLoop = True
    while continueLoop:
        average = input('Enter Average: ')

        try:
            collection.append(float(average))
        except:
            print('Must enter decimal number. Please try again.')
            continue

        userInput = input('Add another average? (Y/n): ').upper()
        if userInput != "Y" and userInput != "YES":
            continueLoop = False
    
    return collection