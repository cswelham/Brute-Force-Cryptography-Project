import operator

# Calculates the letter frequency in a string
# Assumes that e is the most common letter in large strings
def calculateLetterFrequency(message, period):

    # Letters in alphabet
    alphabetUppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alphabetFrequency = {'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 'u': 0.02758, 'v': 0.00978, 'w': 0.0236, 'x': 0.0015, 'y': 0.01974, 'z': 0.00074}
    
    # Remove spaces from string and convert to lowercase
    message = message.replace(" ", "").lower()
    
    # Create dictionary
    stringDict = dict()

    # Split string into columns
    index = 0
    array = []
    while index < period:
        currentIndex = index
        string = ''
        while currentIndex < len(message):
            string += message[currentIndex]
            currentIndex += period
        if len(string) > 1:
            array.append(string) 
        index += 1

    key = ''
    # Loop through columns
    for column in array:
        chiScores = []
        # Loop through possible shifts
        for shift in range(1, 27):
            # Shift the column
            newColumn = column
            for letter in column:
                indexLetter = list(alphabetFrequency.keys()).index(letter)
                indexLetter = indexLetter + shift
                if indexLetter > 25:
                    indexLetter = indexLetter - 26
                elif indexLetter < 0:
                    indexLetter = indexLetter + 26
                newColumn = newColumn.replace(letter, alphabetUppercase[indexLetter])
            newColumn = newColumn.lower()

            # Calculate frequencies of each letter
            stringDict = dict()
            for char in newColumn:
                if char in stringDict.keys():
                    stringDict[char] += 1
                else:
                    stringDict[char] = 1
            stringDict = dict(sorted(stringDict.items(), key=operator.itemgetter(1),reverse=True))

            # Calculate the chi square score
            keys = list(alphabetFrequency.keys())
            values = list(alphabetFrequency.values())
            chisquare = 0
            for i in range(len(list(alphabetFrequency.keys()))):
                prob = 0
                if keys[i] in stringDict:
                    prob = stringDict[keys[i]] / len(stringDict.keys())
                chisquare = chisquare + ((prob - values[i])**2 / values[i])
            chiScores.append(chisquare)

        # Choose letter that minimizes chisquare
        minIndex = min(range(len(chiScores)), key=chiScores.__getitem__)
        key = key + keys[minIndex]

    return key[::-1]
                    
                
                
   
        
