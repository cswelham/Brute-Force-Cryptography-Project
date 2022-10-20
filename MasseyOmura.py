#function takes input from both parties and the prime to determine the message sequence
def encodeMO():
    while(True):
        try:
            prime = int(input("What is the Prime: "))
            sSecret = int(input("What is the secret number: Sender ")) # get the secret number for the sender
            _p = prime-1
            inverseSecretS = pow(sSecret, _p-1, _p) # calculate the inverse of K modulo the prime 
            rSecret = int(input("What is the secret number: Reciever ")) # get the secret number for the sender
            inverseSecretR = pow(rSecret, _p-1, _p) # calculate the inverse of K modulo the prime
            
            message = int(input("What is the secret message: Sender ")) # get the secret message

            
            
            y1 = (message ** sSecret) % prime
            y2 =(y1 ** rSecret) % prime
            y3 = (y2 ** inverseSecretS) % prime
            y4 = (y3 ** inverseSecretR) % prime

            yx = (((message ** sSecret) % prime) ** inverseSecretS ) %prime
            
            print("y1:" + str(y1))
            print("y2:" + str(y2))
            print("y3:" + str(y3))
            print("y4:" + str(y4))  
            return
        except:
            print("Invalid Input Please Try Again")

#function takes the three message values and outputs the message
def decodeMO():
    while(True):
        try:
            prime = int(input("What is the Prime: "))
            value1 = int(input("What is the Y1: ")) #Message encoded with sender's private number
            value2 =  int(input("What is the Y2: ")) # Message encoded with sender and reciever private number
            value3 =  int(input("What is the Y3: ")) # Message encoded with the reciever's private number
            
            
            bases1 = []
            powers1= []
            inverses = []
            for b in range(1,prime): # for each possible base
                for p in range(prime): # for each possible exponent
                    test =(b**p) % prime
                    
                    if( test == value1): # if a valid combination of base and exponent
                        #print(str(b) +"^" + str(p)+"= " +str(test))
                        bases1.append(b) # add to list of bases 
                        powers1.append(p) # add to list of powers
                        _p = prime-1 # adjust for inverse 
                        inverses.append(pow(p, _p-1, _p)) # calculate and append inverse value

            #debugging     
            #print(bases1)
            #print(powers1)
            #print(inverses)

            for i in range(len(inverses)):  # for each inverse value
                test = value2**inverses[i] %prime # calculation used in comparison
                #print(str(value2) +"^" + str(inverses[i])+"= " +str(test)) # for debugging
                if(test == value3):
                    print("Message is: " +str(bases1[i])) # print the message
                    return
        except:
            print("Invalid Input Please Try Again")

"""

#prime = int(input("What is the Prime: "))

choice  = input("MasseyOmura: Would you like to encrypt (E) or decrypt (D)? ").lower()
while True:
    #if user wants to encrypt
    if(choice == "e"):
        #call encryption method
        encodeMO()# used to encode a message
        break
    #user wants to decrypt
    elif(choice =="d"):
        #call decryption method
        decodeMO() # used to decode a message
        break 
    else:
        #invalid - get input again
        choice = input("Please enter E/e for encryption or enter D/d for decryption: ")


"""
