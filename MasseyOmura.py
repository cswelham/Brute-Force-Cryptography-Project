#function takes input from both parties and the prime to determine the message sequence
def encryptMO():
    while(True):
        try:
            prime = int(input("What is the Prime: "))
            u = int(input("What is the u: ")) # get the secret number for the sender
            _p = prime-1
            inverseU = pow(u, _p-1, _p) # calculate the inverse of K modulo the prime-1
            v = int(input("What is the v: ")) # get the secret number for the sender
            inverseV = pow(v, _p-1, _p) # calculate the inverse of K modulo the prime-1
            
            message = int(input("What is the message: Sender ")) # get the secret message

            
            #calculate the messages 
            y1 = (message ** u) % prime
            y2 =(y1 ** v) % prime
            y3 = (y2 ** inverseU) % prime
            y4 = (y3 ** inverseV) % prime
            
            #prints out all the messages 
            # y4 should equal message
            print("y1:" + str(y1))
            print("y2:" + str(y2))
            print("y3:" + str(y3))
            print("y4:" + str(y4))  
            return
        except:
            print("Invalid Input Please Try Again")

#function takes the three transmitted values and outputs the message
def decryptMO():
    while(True):
        try:
            prime = int(input("What is the Prime: "))
            value1 = int(input("What is the Y1: ")) #Message encrypted with sender's private number
            value2 =  int(input("What is the Y2: ")) # Message encrypted with sender and reciever private number
            value3 =  int(input("What is the Y3: ")) # Message encrypted with the reciever's private number
            
            
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

