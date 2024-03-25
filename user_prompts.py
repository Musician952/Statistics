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