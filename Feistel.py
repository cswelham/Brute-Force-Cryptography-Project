# Feistel cypher which generates random key functions using xor, or, and, shuffling and reversing binary numbers

# Test: 10000101010100101010111000
import random

# Encrypt a message with a specific number of rounds
def encryptFeistel(message, rounds, keys):

    print('')
    print('Encryption Steps')
    # For each round
    for i in range(rounds):
        # Split message
        leftPrev, rightPrev = message[:len(message)//2], message[len(message)//2:]

        # New left is previous right
        left = rightPrev

        # Perform key function on right in order
        rightFunction = ''
        if (keys[i][0] == 'REVERSE'):
            rightFunction = keyReverse(rightPrev)
        elif (keys[i][0] == 'SHUFFLE'):
            rightFunction = keyShuffle(rightPrev, keys[i][1])
        elif (keys[i][0] == 'XOR'):
            rightFunction = keyXor(rightPrev, keys[i][1])
        elif (keys[i][0] == 'OR'):
            rightFunction = keyOr(rightPrev, keys[i][1])
        else:
            rightFunction = keyAnd(rightPrev, keys[i][1])
         
        # New right is previous left xor previous right
        right = '{0:0{1}b}'.format((int(leftPrev,2) ^ int(rightFunction,2)), len(leftPrev))

        # Set the new message
        message = left + right

        # Get the function order for output
        new = ""
        if (keys[i][0] != "REVERSE"):
            for j in range(len(keys[i][1])):
                new = new + message[keys[i][1][j]]
            print("L: " + left + " R: XOR(" + leftPrev + ",  Function(" + keys[i][0] + ", " + leftPrev + ", " + new + "))")
        else:
            print("L: " + left + " R: XOR(" + leftPrev + ",  Function(" + keys[i][0] + ", " + leftPrev + "))")
        
    # Swap left and right around
    left, right = message[:len(message)//2], message[len(message)//2:]
    return (right + left)

# Decrypt a message with a specific number of rounds
def decryptFeistel(message, rounds, keys):

    print('Decryption Steps')
    # For each round
    for i in range(rounds):
        # Split message
        leftPrev, rightPrev = message[:len(message)//2], message[len(message)//2:]

        # New left is previous right
        left = rightPrev

        # Perform key function on right in reverse order
        rightFunction = ''
        if (keys[i][0] == 'REVERSE'):
            rightFunction = keyReverse(rightPrev)
        elif (keys[i][0] == 'SHUFFLE'):
            rightFunction = keyShuffle(rightPrev, keys[i][1])
        elif (keys[i][0] == 'XOR'):
            rightFunction = keyXor(rightPrev, keys[i][1])
        elif (keys[i][0] == 'OR'):
            rightFunction = keyOr(rightPrev, keys[i][1])
        else:
            rightFunction = keyAnd(rightPrev, keys[i][1])
        
        # New right is previous left xor previous right
        right = '{0:0{1}b}'.format((int(leftPrev,2) ^ int(rightFunction,2)),len(leftPrev))

        # Set the new message
        message = left + right

        # Get the function order for output
        new = ""
        if (keys[i][0] != "REVERSE"):
            for j in range(len(keys[i][1])):
                new = new + message[keys[i][1][j]]
            print("L: " + left + " R: XOR(" + leftPrev + ",  Function(" + keys[i][0] + ", " + leftPrev + ", " + new + "))")
        else:
            print("L: " + left + " R: XOR(" + leftPrev + ",  Function(" + keys[i][0] + ", " + leftPrev + "))")
        
    # Swap left and right around
    left, right = message[:len(message)//2], message[len(message)//2:]
    return (right + left)

# Randomly generates a key for each round
def generateKeys(message, rounds):

    # List of possible actions
    possibleActions = ['XOR', 'OR', 'AND', 'SHUFFLE', 'REVERSE']
    keys = []

    # For each round generate a key
    for i in range(rounds):
        # Get random action
        index = random.randrange(0, (len(possibleActions) - 1))
        action = possibleActions[index]

        # Generate random shuffle for half of message
        numbers = list(range(0, (len(message)//2)))
        # Shuffle order of numbers
        random.shuffle(numbers)
        keys.append([action, numbers])

    return keys

# XOR operator with corresponding number
def keyXor(right, order):

    newRight = ''
    # Loop through order
    for i in range(len(order)):
        position = int(order[i])
        number = int(right[position]) ^ int(right[i])
        newRight = newRight + str(number)
    return newRight

# OR operator with corresponding number
def keyOr(right, order):

    newRight = ''
    # Loop through order
    for i in range(len(order)):
        position = int(order[i])
        number = int(right[position]) | int(right[i])
        newRight = newRight + str(number)
    return newRight

# AND operator with corresponding number
def keyAnd(right, order):

    newRight = ''
    # Loop through order
    for i in range(len(order)):
        position = int(order[i])
        number = int(right[position]) & int(right[i])
        newRight = newRight + str(number)
    return newRight

# Shuffle the binary number
def keyShuffle(right, order):

    newRight = ''
    
    # Loop through order
    for i in range(len(order)):
        position = int(order[i])
        newRight = newRight + right[position]
    return newRight

# Reverses order of binary number
def keyReverse(right):

   return right[::-1]

# Main code
def feistelMain():

    print('You can encrypt a message and then check that it decrypts.')
    
    message = ""
    # While user is still wants to use program
    while (message != "EXIT"):
        message = input('What message do you want to encrypt? Or type EXIT to leave\n')
        
        if message == "EXIT":
            exit()

        # Check for valid input    
        valid = False
        while not valid:
            valid = True
            for item in message:
                if item not in {'0','1'}:
                    valid = False
                    break
            if len(message)%2 != 0:
                valid = False
            if not valid:
                print('Please specify only ones and zeroes of an even length.')
                message = input('What message do you want to encrypt?\n')

                if message == "EXIT":
                    exit()
                    
        # Get number of rounds
        rounds = input('What is your number of rounds?\n')
        while (rounds.isdigit() == False and rounds >= 1):
            print('Please specify a number.')
            rounds = input('What is your number of rounds?\n')

        # Generate array of keys
        keys = generateKeys(str(message), int(rounds))

        # Print result
        encrypt = encryptFeistel(str(message), int(rounds), keys)
        print('')
        print('Encrypted Message:')
        print(encrypt)
        print('')

        # Decrypt message
        decrypt = decryptFeistel(str(encrypt), int(rounds), keys[::-1])
        print('')
        print('Decrypted Message:')
        print(decrypt)
        print('')
            
        
    
