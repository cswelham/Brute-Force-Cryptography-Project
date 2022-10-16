from ICCalculator import calculateIC
from RemoveSpacesCapitals import removeSpacesCapitals

# Calculates the permutation period p
def calculateP(text):

    text = removeSpacesCapitals(text)
    
    # Array of possible permutations
    high = 11
    if high > len(text):
        high = len(text)
    possibleP = list(range(2, high))

    # Loop through each possible p
    indexes = []
    for i in range(len(possibleP)):
        index = 0
        array = []
        while index < possibleP[i]:
            currentIndex = index
            string = ''
            while currentIndex < len(text):
                string += text[currentIndex]
                currentIndex += possibleP[i]
            if len(string) > 1:
                array.append(string) 
            index += 1

        # Calculate I.C for each column
        totalIC = 0
        for j in range(len(array)):
            totalIC += calculateIC(array[j])
        indexes.append((totalIC/len(array)))


    # Find what index is closest to plaintext index
    bestIndex = 0
    bestDiff = 0
    print('')
    for k in range(len(indexes)):
        print('P='+str(k+2)+' IC='+str(indexes[k]))
        if indexes[k] > bestDiff:
            bestIndex = k
            bestDiff = indexes[k]
    print('')
    # Return the most likely period p
    return possibleP[bestIndex]
            
            

        
   
        
