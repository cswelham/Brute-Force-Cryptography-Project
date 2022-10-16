# Import permutation finder and letter frequency
from PeriodicityFinder import calculateP
from LetterFrequencyCalculator import calculateLetterFrequency
from RemoveSpacesCapitals import removeSpacesCapitals

class Vigenere_Cipher():

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
            
            encryptedLetter = ((messageLetterNum + keyLetterNum - 1) % 26) + 96
            if encryptedLetter == 96:
                encryptedLetter = 122
            encryptedMessage = encryptedMessage + chr(encryptedLetter)
        
        return encryptedMessage

    def decrypt(self, key, encryptedMessage):
        
        # Test kksoshniqrzyalrpihwlhnxdzilptketkomhnbgexukcmdjdjlhnkrppdcrvptdmrgwuoodinmxtyhjcqsvzwajegwxcrysbwatduhjaoakhknbocgoiloejppdskdbnznuvpcceewopdrghlxdrlslwsifqswqkvgevrtrqptxtyrqogikoanstyhzzhnbhnalobljoztkkamzrjikzremhnikhfxnazfkhnezrujevmynhwakepzdwgaueammlfrgqmggdhmvajeqtkivgevsokdgqmgjrimayghnkxtyhobdadskcqiejbznmlqzmqhvurquiukwqqgryabgezplzdsjlkvshrwdmqwyrhmgergsiroeiezdrrljlqogvppdszcaweblohmsskkqvceihzwmtyhyirtchsqmdfzonnruduannvqzbgecdgmqojhppdfcrsmqbvgobtrehzqmtfpqlcyjwnmzmjdjlgaxuelrplplshnjvsmklvgpwshvvehdowjwzceevdmcsfoeddrnrklreewdcrirvinnrihcckaiwnihnzqcadsjlkvrhfzaddrndovntudixdnvgsphcyzwavhpkwzqyndobnbvikcmdcdpmnnvvpwqmpvwbtruduietvujwnnriaecapvxmeoihdiklfzammrvwqzmiejpwfrpibqmdfupwveignmmcyhzbntyhoshnrqzaolrwpmqeuzebgmlgaddnrveldfiribgeidevznuzevcikkwlmtshavzhrslgorrfpqbejhoahoeinmcaegcmnrxhspnhrgxmdnjsuqmgfqppdscbppdrzqpmzmydzadeeikzshvpomkvvvppdsghalnfkkkadnvzjqlblvpentyrqaznudjlnnvvppdyihlwqtvgppztkkaakykkazhnkhwuvajqkunrvwdimsvyavfrvhjqrhsoqzrsyrkbhnxwdznuxkppdazuhqjedloahlvvwagaiuuapuvoypddrokvftyhzmreiwalboiuelnryhyilerfnwrsjrimaoubspnlfrgmcjlvpirpihkkbuglalzsyhsirnvdntxhvdztdsjqekjtyhcpnskrboqywievcoiwkedrndoasailjoloiromkyfxpweanljlnwdxpbdrzqccmdvudqrbihwbgdfqpntlwlhtshvlnzdqllnmleewopzlwdjqmcylbbgakkatkoelysrazgdiqrp

        if key is not None:
            key = self.keyLengthAdjuster(key, len(encryptedMessage))
            decryptedMessage = ""

            for idx, i in enumerate(encryptedMessage):
                messageLetterNum = ord(i) - 96
                keyLetterNum = ord(key[idx]) - 96
            
                decryptedLetter = ((messageLetterNum - keyLetterNum + 1) % 26) + 96
                if decryptedLetter == 96:
                    decryptedLetter = 122
                decryptedMessage = decryptedMessage + chr(decryptedLetter)
        
            return decryptedMessage
        else:
            print('not implemented')
        

while(True):
    choice = input("Do you want to encrypt or decrypt? (type 'exit' to exit): ").lower()
    if choice == 'encrypt':
        message = input("Enter message: ").lower()
        key = input("Enter key: ").lower()
        cipher = Vigenere_Cipher()
        encryptedMessage = cipher.encrypt(key, removeSpacesCapitals(message))
        print(encryptedMessage)
    elif choice == 'decrypt':
        message = input("Enter message: ").lower()
        # Calculate the period
        period = calculateP(message)
        # Calculate the key
        key = calculateLetterFrequency(message, period)
        print('Key: ' + key)
        print('Decrypted Message:')
        cipher = Vigenere_Cipher()
        decryptedMessage = cipher.decrypt(key, removeSpacesCapitals(message))
        print(decryptedMessage)
        print('')
    elif choice == 'exit':
        exit()
    else:
        print('No choice selected, please try again')

