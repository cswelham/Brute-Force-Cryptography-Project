# Import permutation finder and letter frequency
from PeriodicityFinder import calculateP
from LetterFrequencyCalculator import calculateLetterFrequency
from RemoveSpacesCapitals import removeSpacesCapitals
 
#increases or decreases the size of the key to match the message length
def keyLengthAdjuster(key, messageLength):
    lengthKey = len(key)
 
    #decreases key length
    if messageLength < lengthKey:
        diff = lengthKey - messageLength
        key = key[diff:]
        print(key)
 
    #increases key length
    elif messageLength > lengthKey:
        temp = key
 
        while lengthKey < messageLength:
            temp = temp + key
            lengthKey = len(temp)
 
        key = temp
 
        if lengthKey != messageLength:
            key = key[:messageLength]
            lengthKey = len(key)
 
    return key
 
#encrypts a message using a key the user provides
def vigenereEncrypt():
 
    message = input('What message do you want to encrypt?\n')
    while (any(char.isdigit() for char in message) == True):
        print('Please specify only letters.')
        message = input('What message do you want to encrypt?\n')
       
    message = removeSpacesCapitals(message)
    key = input('What is your key?\n')
    while (key.isalpha() == False):
        print('Please specify only letters.')
        key = input('What is your key?\n')
 
    key = keyLengthAdjuster(key, len(message))
    encryptedMessage = ""
 
    #iterates over the message and encrypts each letter
    for idx, i in enumerate(message):
        #converts each letter to a number
        messageLetterNum = ord(i) - 96
        #converts the key to a number
        keyLetterNum = ord(key[idx]) - 96
       
        #using the key, encrypts a letter
        encryptedLetter = ((messageLetterNum + keyLetterNum - 1) % 26) + 96
        if encryptedLetter == 96:
            encryptedLetter = 122
        #adds the encrypted letter to the encrypted message
        encryptedMessage = encryptedMessage + chr(encryptedLetter)
   
    print('Encrypted Message:')
    print(encryptedMessage)
 
def vigenereDecrypt():
 
    cyphertext = input('What cyphertext do you want to decrypt?\n')
    while (any(char.isdigit() for char in cyphertext) == True):
        print('Please specify only letters.')
        cyphertext = input('What cyphertext do you want to decrypt?\n')
       
    cyphertext = removeSpacesCapitals(cyphertext)
    # Calculate the period
    period = calculateP(cyphertext)
    # Calculate the key
    key = calculateLetterFrequency(cyphertext, period)

    print('Calculated Period: ' + str(period))
    print('Calculated Key with Chi-Square Test: ' + key)
   
    #adjusts the key length
    key = keyLengthAdjuster(key, len(cyphertext))
    decryptedMessage = ""
 
    #encrypts the message
    for idx, i in enumerate(cyphertext):
        #converts each letter to a number
        messageLetterNum = ord(i) - 96
        #converts the key to a number
        keyLetterNum = ord(key[idx]) - 96
   
        #using the key, decrypts a letter
        decryptedLetter = ((messageLetterNum - keyLetterNum + 1) % 26) + 96
        if decryptedLetter == 96:
            decryptedLetter = 122
        #adds the decrypted letter to the message
        decryptedMessage = decryptedMessage + chr(decryptedLetter)

    print('Decrypted Message:')
    print(decryptedMessage)
    print('')
 
# Test kksoshniqrzyalrpihwlhnxdzilptketkomhnbgexukcmdjdjlhnkrppdcrvptdmrgwuoodinmxtyhjcqsvzwajegwxcrysbwatduhjaoakhknbocgoiloejppdskdbnznuvpcceewopdrghlxdrlslwsifqswqkvgevrtrqptxtyrqogikoanstyhzzhnbhnalobljoztkkamzrjikzremhnikhfxnazfkhnezrujevmynhwakepzdwgaueammlfrgqmggdhmvajeqtkivgevsokdgqmgjrimayghnkxtyhobdadskcqiejbznmlqzmqhvurquiukwqqgryabgezplzdsjlkvshrwdmqwyrhmgergsiroeiezdrrljlqogvppdszcaweblohmsskkqvceihzwmtyhyirtchsqmdfzonnruduannvqzbgecdgmqojhppdfcrsmqbvgobtrehzqmtfpqlcyjwnmzmjdjlgaxuelrplplshnjvsmklvgpwshvvehdowjwzceevdmcsfoeddrnrklreewdcrirvinnrihcckaiwnihnzqcadsjlkvrhfzaddrndovntudixdnvgsphcyzwavhpkwzqyndobnbvikcmdcdpmnnvvpwqmpvwbtruduietvujwnnriaecapvxmeoihdiklfzammrvwqzmiejpwfrpibqmdfupwveignmmcyhzbntyhoshnrqzaolrwpmqeuzebgmlgaddnrveldfiribgeidevznuzevcikkwlmtshavzhrslgorrfpqbejhoahoeinmcaegcmnrxhspnhrgxmdnjsuqmgfqppdscbppdrzqpmzmydzadeeikzshvpomkvvvppdsghalnfkkkadnvzjqlblvpentyrqaznudjlnnvvppdyihlwqtvgppztkkaakykkazhnkhwuvajqkunrvwdimsvyavfrvhjqrhsoqzrsyrkbhnxwdznuxkppdazuhqjedloahlvvwagaiuuapuvoypddrokvftyhzmreiwalboiuelnryhyilerfnwrsjrimaoubspnlfrgmcjlvpirpihkkbuglalzsyhsirnvdntxhvdztdsjqekjtyhcpnskrboqywievcoiwkedrndoasailjoloiromkyfxpweanljlnwdxpbdrzqccmdvudqrbihwbgdfqpntlwlhtshvlnzdqllnmleewopzlwdjqmcylbbgakkatkoelysrazgdiqrp
# CUDRYHSODBODGRZAFDNRFCRQTELCTHNVXSOHSGNNBZNSRRQHVROOCLNTWHRELHHPELNGIOEWHRPOQHRAFOZSUGHRUHWNVTUHSBQOSEEAMAZLNODBODGRDWRDLGKYYRNQRNODNXHRUHACSLVHDULSTHNVXSGRMNQYCUOOOEZVHVVIAYEAWIBQSVQCYXDRWHRVPRHDBPEGHRNQDGKEPRWPDTPKEE
