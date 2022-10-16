from RemoveSpacesCapitals import removeSpacesCapitals

# Encrypt a message with a key
def encryptRF(string, key):

    string = removeSpacesCapitals(string)
    
    # Create the matrix
    matrix = [[''] * len(string) for i in range(key)]

    # Initialize variables
    direction = "Up"
    row = 0
    col = 0

    # Set the string message on the rail matrix
    for i in range(len(string)):

        # If top or bottom rail has been filled
        if (row == 0) or (row == key - 1):
            # Change the direction
            if (direction == "Down"):
                direction = "Up"
            else:
                direction = "Down"
         
        # Fill the rail matrix at position
        matrix[row][col] = string[i]
        # Go to next column
        col += 1
         
        # If the direction is up
        if direction == "Up":
            # Minus one to row to go up
            row -= 1
        else:
            # Else add one from row to go down
            row += 1
            
    # Construct the cypher
    cypher = []
    # Loop through key for each letter in the string
    for i in range(key):
        for j in range(len(string)):
            # If position in matrix is not empty
            if matrix[i][j] != '':
                # Add rail matrix letter to cypher
                cypher.append(matrix[i][j])

    # Add all letters of array together
    cypher = ''.join(cypher)
    # Return encrypted message
    return("Encrypted cyphertext: " + cypher)
     
# Decrypt cyphertext with a key
def decryptRF(cypher, key):

    cypher = removeSpacesCapitals(cypher)
 
    # Create the matrix
    matrix = [[''] * len(string) for i in range(key)]
     
    # Initialize variables
    direction = "Up"
    row = 0
    col = 0
     
    # Set markers for message position on rail matrix
    for i in range(len(cypher)):
        # If the row is 0
        if row == 0:
            # Set direction to down
            direction = "Down"
        # If it is the last row
        if row == key - 1:
            # Set direction to up
            direction = "Up"
         
        # Place hypen as a placeholder for string position
        matrix[row][col] = '-'
        # Go to next column
        col += 1
         
        # If the direction is up
        if direction == "Up":
            # Minus one to row to go up
            row -= 1
        else:
            # Else add one from row to go down
            row += 1
             
    # Loop through key for each letter in the string
    index = 0
    for i in range(key):
        for j in range(len(cypher)):
            # If the rail matrix position is marked and the index is less than the cypher length
            if ((matrix[i][j] == '-') and index < len(cypher)):
                # Add cypher to position
                rail[i][j] = cypher[index]
                # Increase index
                index += 1
         
    # Initialize variables
    message = []
    row = 0
    col = 0

    # Loop through the cypher text
    for i in range(len(cypher)):
        # If the row is 0
        if row == 0:
            # Set direction to down
            direction = "Down"
        # If it is the last row
        if row == key - 1:
            # Set direction to up
            direction = "Up"
             
        # If position in matrix is not a marker
        if (matrix[row][col] != '*'):
            # Add string to result
            message.append(rail[row][col])
            # Go to next column
            col += 1
             
        # If the direction is up
        if direction == "Up":
            # Minus one to row to go up
            row -= 1
        else:
            # Else add one from row to go down
            row += 1
            
    # Add all letters of array together
    message = ''.join(message)
    # Return  message
    return("Decrypted Message: " + message)
    
 
# Main code
if __name__ == "__main__":
    print('This is a RailFence Cypher.')
    print('Type E to encrypt a message and type D to decrypt a message.')
    
    option = ""
    # While user is still wants to use program
    while (option != "EXIT"):
        option = input('Do you want to (E)ncrypt or (D)ecrypt a message? Or type EXIT to stop.\n')
        if (option == "E" or option == "e"):
            # Get user's message
            message = input('What message do you want to encrypt?\n')
            while (message.isalpha() == False):
                print('Please specify only letters.')
                message = input('What message do you want to encrypt?\n')

            # Get user's key
            key = input('What is your key?\n')
            while (key.isdigit() == False):
                print('Please specify only letters.')
                key = input('What is your key?\n')

            # Print result
            print('')
            print(encryptRF(message, int(key)))
            print('')
           
        elif (option == "D" or option == "d"):
            # Get user's message
            cypher = input('What cypher do you want to decrypt?\n')
            while (cypher.isalpha() == False):
                print('Please specify only letters.')
                cypher = input('What cypher do you want to decrypt?\n')

            # Get user's key
            key = input('What is your key?\n')
            while (key.isdigit() == False):
                print('Please specify only letters')
                key = input('What is your key?\n')

            # Print result
            print('')
            print(decryptRF(message, int(key)))
            print('')
        
        elif (option != "EXIT"):
            print('That was not a valid option. Please try again.')
    exit()
            
        
    
