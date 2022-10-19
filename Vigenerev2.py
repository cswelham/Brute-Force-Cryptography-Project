# Import permutation finder and letter frequency
from PeriodicityFinder import calculateP
from LetterFrequencyCalculator import calculateLetterFrequency
from RemoveSpacesCapitals import removeSpacesCapitals

def keyLengthAdjuster(key, messageLength):
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

def vigenereEncrypt():

    message = input('What message do you want to encrypt?\n')
    while (message.isalpha() == False):
        print('Please specify only letters.')
        message = input('What message do you want to encrypt?\n')
        
    message = removeSpacesCapitals(message)
    key = input('What is your key?\n')
    while (key.isalpha() == False):
        print('Please specify only letters.')
        message = input('What is your key?\n')

    key = keyLengthAdjuster(key, len(message))
    encryptedMessage = ""

    for idx, i in enumerate(message):
        messageLetterNum = ord(i) - 96
        keyLetterNum = ord(key[idx]) - 96
        
        encryptedLetter = ((messageLetterNum + keyLetterNum - 1) % 26) + 96
        if encryptedLetter == 96:
            encryptedLetter = 122
        encryptedMessage = encryptedMessage + chr(encryptedLetter)
    
    print('Encrypted Message:')
    print(encryptedMessage)

def vigenereDecrypt():

    cyphertext = input('What cyphertext do you want to decrypt?\n')
    while (cyphertext.isalpha() == False):
        print('Please specify only letters.')
        cyphertext = input('What cyphertext do you want to decrypt?\n')
        
    cyphertext = removeSpacesCapitals(cyphertext)
    # Calculate the period
    period = calculateP(cyphertext)
    # Calculate the key
    key = calculateLetterFrequency(cyphertext, period)
    
    key = keyLengthAdjuster(key, len(cyphertext))
    decryptedMessage = ""

    for idx, i in enumerate(cyphertext):
        messageLetterNum = ord(i) - 96
        keyLetterNum = ord(key[idx]) - 96
    
        decryptedLetter = ((messageLetterNum - keyLetterNum + 1) % 26) + 96
        if decryptedLetter == 96:
            decryptedLetter = 122
        decryptedMessage = decryptedMessage + chr(decryptedLetter)

    print('Key: ' + key)
    print('Decrypted Message:')
    print(decryptedMessage)
    print('')

# Test kksoshniqrzyalrpihwlhnxdzilptketkomhnbgexukcmdjdjlhnkrppdcrvptdmrgwuoodinmxtyhjcqsvzwajegwxcrysbwatduhjaoakhknbocgoiloejppdskdbnznuvpcceewopdrghlxdrlslwsifqswqkvgevrtrqptxtyrqogikoanstyhzzhnbhnalobljoztkkamzrjikzremhnikhfxnazfkhnezrujevmynhwakepzdwgaueammlfrgqmggdhmvajeqtkivgevsokdgqmgjrimayghnkxtyhobdadskcqiejbznmlqzmqhvurquiukwqqgryabgezplzdsjlkvshrwdmqwyrhmgergsiroeiezdrrljlqogvppdszcaweblohmsskkqvceihzwmtyhyirtchsqmdfzonnruduannvqzbgecdgmqojhppdfcrsmqbvgobtrehzqmtfpqlcyjwnmzmjdjlgaxuelrplplshnjvsmklvgpwshvvehdowjwzceevdmcsfoeddrnrklreewdcrirvinnrihcckaiwnihnzqcadsjlkvrhfzaddrndovntudixdnvgsphcyzwavhpkwzqyndobnbvikcmdcdpmnnvvpwqmpvwbtruduietvujwnnriaecapvxmeoihdiklfzammrvwqzmiejpwfrpibqmdfupwveignmmcyhzbntyhoshnrqzaolrwpmqeuzebgmlgaddnrveldfiribgeidevznuzevcikkwlmtshavzhrslgorrfpqbejhoahoeinmcaegcmnrxhspnhrgxmdnjsuqmgfqppdscbppdrzqpmzmydzadeeikzshvpomkvvvppdsghalnfkkkadnvzjqlblvpentyrqaznudjlnnvvppdyihlwqtvgppztkkaakykkazhnkhwuvajqkunrvwdimsvyavfrvhjqrhsoqzrsyrkbhnxwdznuxkppdazuhqjedloahlvvwagaiuuapuvoypddrokvftyhzmreiwalboiuelnryhyilerfnwrsjrimaoubspnlfrgmcjlvpirpihkkbuglalzsyhsirnvdntxhvdztdsjqekjtyhcpnskrboqywievcoiwkedrndoasailjoloiromkyfxpweanljlnwdxpbdrzqccmdvudqrbihwbgdfqpntlwlhtshvlnzdqllnmleewopzlwdjqmcylbbgakkatkoelysrazgdiqrp
# CUDRYHSODBODGRZAFDNRFCRQTELCTHNVXSOHSGNNBZNSRRQHVROOCLNTWHRELHHPELNGIOEWHRPOQHRAFOZSUGHRUHWNVTUHSBQOSEEAMAZLNODBODGRDWRDLGKYYRNQRNODNXHRUHACSLVHDULSTHNVXSGRMNQYCUOOOEZVHVVIAYEAWIBQSVQCYXDRWHRVPRHDBPEGHRNQDGKEPRWPDTPKEE

