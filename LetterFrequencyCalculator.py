# Calculates the letter frequency in a string
def calculateLetterFrequency(string):
    
    # Remove spaces from string and convert to lowercase
    string = string.replace(" ", "").lower()
    
    # Create dictionary
    stringDict = dict()

    # Loop through each character in the string
    for char in string:
        # Add one to the corresponding dictionary entry
        if char in stringDict.keys():
            stringDict[char] += 1
        else:
            stringDict[char] = 1

    stringDict = dict(sorted(stringDict.items(), key=lambda item: item[1]))

    return stringDict
   
        
