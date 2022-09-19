# Calculates the index of coincidence
def calculateIC(text):
    # Dictionary of alphabet with counts of 0
    import string
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)

    # Remove spaces from string and convert to lowercase
    text = text.replace(" ", "").lower()

    # Loop through string and count letters
    for key in alphabet:
        count = 0
        for i in range(len(text)):
            if text[i] == key:
                count += 1
        alphabet[key] = count
    
    # Calculate number of repeats
    charCount = 0
    numRepeats = 0
    for key in alphabet:
        charCount += alphabet[key]
        numRepeats += alphabet[key] * (alphabet[key] - 1)

    # Calculate possible number of repeats
    totalRepeats = charCount * (charCount - 1)

    # Return index of coincidence
    return (numRepeats / totalRepeats)

   
        
