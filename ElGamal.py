


#function calculates the table of logs based on the base and the prime
def discreteLogFunc(prime,base):
    global discreteLogs
    discreteLogs = [] #list to store values
    
    #from 1- modulus -1
    for i in range(1,prime):
        discreteLogs.append( (base**i) % prime) #caluclate value and add to list

    return discreteLogs

#function encrypts an input message with input secret k and public key of receiver
def encryptElGamal():
    while(True):
        try:
            prime = int(input("What is the Prime Number: ")) # get the prime for the system
            base = int(input("What is the Base Number: ")) # get the base for the system

            discreteLogs = discreteLogFunc(prime,base) # populate the log table
            
            message = int(input("What is the Message: ")) #get the message 
            secretk =  int(input("What is the secret k: ")) # get the secret k 
            receiverKey =  int(input("What is the receiver's Public Key: ")) # get the public key of the receiver
                
            K = (receiverKey**secretk) % prime # determine K
            ak = (base**secretk) %prime # determine aK
            Km = (K*message) %prime # determine Km
            
            #output the values, for debugging
            #print("K: "+str(K))
            #print("a^k: "+str(ak))
            #print("Km: "+str(Km))

            #output the pair of values for the cipher text
            print("Cipher Text: (" + str(ak) +", "+ str(Km)+ ")")
            return
        except:
            print("Invalid Input Please Try Again")


#function decrypts an encrypted message
def decryptElGamal():
    while(True):
        try:
            prime = int(input("What is the Prime Number: ")) # get the prime for the system
            base = int(input("What is the Base Number: ")) # get the base for the system
            discreteLogs = discreteLogFunc(prime,base) # populate the log table   

            ak = int(input("What is the first part of the cipher text : ")) #get the first part of the cipher text
            Km =  int(input("What is the second part of the cipher text : ")) # get the second part of the cipher text
            receiverKey = int(input("What is the receiver's public key : "))
            
            #determine the private number
            privateNum =0

            #for each value in the table of logs
            for i in range(len(discreteLogs)):
                if discreteLogs[i]==receiverKey: # get the location of the value that matches ak 
                    privateNum=i+1 # index value is the private value of the receiver
                    break

            print("Receiver Private k: " + str(privateNum))
            
            K = (ak **privateNum) % prime

            inverseK = pow(K, prime-2, prime) # calculate the inverse of K modulo the prime 

            # inverse calculation based on https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
            
            #For debugging
            #print("K: "+ str(K))  #print the value of K
            #print("K^-1: "+str(inverseK)) #print the value of K inverse
            
            message = (inverseK * Km) % prime  # use K inverse to decrypt the message
        
            print("Original Message is: "+str(message))  #print the decrypted message
            return
        except:
            print("Invalid Input Please Try Again")
