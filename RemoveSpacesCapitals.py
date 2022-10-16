import string

# Removes or spaces, capitals and punctuation from the message
def removeSpacesCapitals(message):
    # Remove punctuation
    message = message.translate(str.maketrans('', '', string.punctuation))

    # Remove capitals
    message = message.lower()

    # Remove spaces
    message = message.replace(" ", "")

    return message
            

        
   
        
