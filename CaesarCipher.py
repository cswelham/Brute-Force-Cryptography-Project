from base64 import decode
import string

#function gets the most common letter present in the dictionary
def getMostCommonLetter(dict): 
     #make a list of the dictionary values in order
     valueList = list(dict.values())
     #make a list of the keys in order
     keyList = list(dict.keys())
     #return the first key with the maximum value  - doesnt account for 2 or more cases of same max value so may not always work
     return keyList[valueList.index(max(valueList))]

#function encrypts plaintext using caesar cipher method
def caesarEncrypt():
    try:

        # get the plaintext and shift
        file = input("Please Enter The Plain Text Location: ")
        shift = int(input("Please Enter A Shift Value from 1 to 26: "))
        while(True):
            if(shift>0 and shift<27):
                break
            shift = int(input("Invalid Input, Please Enter A Shift Value from 1 to 26: "))


        #open file and remove all whitespace and capitals
        f = open(file, "r")
        text = f.read().replace(" ", "").lower()
    
        output = "" 
        #for each character in the plaintext
        for i in range(len(text)):
            #determine the new character mod 26
            encodedChar = (int(ord(text[i])) -97 +int(shift)) %26
            # adjust the character to ascii 
            encodedChar +=97
            #add the encoded char to output
            output += chr(encodedChar)
        
        #print the encoded text
        print("Encoded Text:")
        print(output)
        return
    
    except:
        print("Invalid input, please try again")
        caesarEncrypt()
        

#function decryptes a caesar cipher encoded text
def caesarDecrypt():
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    #get the cipher text location
    file = input("Please Enter The Cipher Text Location: ")
    
    f = open(file, "r")
    text = f.read().replace(" ", "").lower()

    #determine if the user has the key
    choice =input("Do you know the key? (Y/N) ").lower()
    
    while(True):
        #if the user has the key
        if(choice == "y"):
            #decrypt the text using the key
            decryptWithKey(text)
            return
        elif(choice=="n"):
            #the user doesnt have the key so continue
            break
        else:
            #invalid - get input again
            choice = input("Enter Y/y if you have the key, otherwise entery N/n: ")

    # Loop through string and count letters
    for key in alphabet:
        count = 0
        for i in range(len(text)):
            if text[i] == key:
                count += 1
        alphabet[key] = count

    #get the most common letter
    mostCommon = getMostCommonLetter(alphabet)
    #determine the shift based on e being the most frequent letter
    shift = int(ord(mostCommon)-int(ord("e")))
    #display the shift
    print("Shift is: " + str(shift))
    
    
    output = "" 

    #for each character
    for i in range(len(text)):
            #determine the original character mod 26
            decodedChar = (int(ord(text[i])) -97 -shift) %26
            #adjust to ascii
            decodedChar +=97
            #add the decoded text to output
            output += chr(decodedChar)

    #display decoded text
    print("\nDecoded Text is:")
    print(output)



#method used to decrypt cipher text with the key
def decryptWithKey(cipherText):
    #get the key
    key = int(input("Enter the shift: "))
    output = "" 
    #
    for i in range(len(cipherText)):
            decodedChar = (int(ord(cipherText[i])) -97 -key) %26
            decodedChar +=97
            output += chr(decodedChar)
    print("\nDecoded Text is:")
    print(output)

"""
takes a text file as input: either plaintext or caesar cipher encrypted 

#set up the dictionary to store frequency counts
alphabet = dict.fromkeys(string.ascii_lowercase, 0)

#determine if the user wants to encode or decode
choice  = input("Caesar Cipher: Would you like to encrypt (E) or decrypt (D)? ").lower()
while True:
    #if user wants to encrypt
    if(choice == "e"):
        #call encryption method
        caesarEncrypt()
        break
    #user wants to decrypt
    elif(choice =="d"):
        #call decryption method
        caesarDecrypt()
        break 
    else:
        #invalid - get input again
        choice = input("Please enter E/e for encryption or enter D/d for decryption: ")
"""
