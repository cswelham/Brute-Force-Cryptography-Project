class Vigenere_Cypher():

    def keyLengthAdjuster(self, key, messageLength):
        lengthKey = len(key)

        if messageLength < lengthKey:
            diff = lengthKey - messageLength
            key = key[diff:]
            print(key)

        elif messageLength > lengthKey:

            remainder = messageLength % lengthKey
            temp = key

            while lengthKey < messageLength:
                temp = temp + key
                lengthKey = len(temp)

            key = temp

            if lengthKey != messageLength:
                key = key[:messageLength]
                lengthKey = len(key)

        return key

    def encrypt(self, key, message):
    
        key = self.keyLengthAdjuster(key, len(message))
        encryptedMessage = ""

        for idx, i in enumerate(message):
            messageLetterNum = ord(i) - 96
            keyLetterNum = ord(key[idx]) - 96
            
            encryptedLetter = ((messageLetterNum + keyLetterNum) % 26) + 96
            encryptedMessage = encryptedMessage + chr(encryptedLetter)
        
        return encryptedMessage

    def decrypt(self, key, encryptedMessage):
        if key is not None:
            key = self.keyLengthAdjuster(key, len(encryptedMessage))
            decryptedMessage = ""

            for idx, i in enumerate(encryptedMessage):
                messageLetterNum = ord(i) - 96
                keyLetterNum = ord(key[idx]) - 96
            
                decryptedLetter = ((messageLetterNum - keyLetterNum) % 26) + 96
                decryptedMessage = decryptedMessage + chr(decryptedLetter)
        
            return decryptedMessage
        else:
            print('not implemented')

while(True):
    choice = input("Do you want to encrypt or decrypt? (type 'exit' to exit): ").lower()
    if choice == 'encrypt':
        message = input("Enter message: ").lower()
        key = input("Enter key: ").lower()
        cipher = Vigenere_Cypher()
        encryptedMessage = cipher.encrypt(key, message)
        print(encryptedMessage)
    elif choice == 'decrypt':
        message = input("Enter message: ").lower()
        key = input("Enter key (if you have one): ").lower()
        cipher = Vigenere_Cypher()
        decryptedMessage = cipher.decrypt(key, message)
        print(decryptedMessage)
    elif choice == 'exit':
        exit()
    else:
        print('No choice selected, please try again')

