# DEFINE SWITCHES 
# Encryption
def enc_switch(enc_cipher):
    if enc_cipher == "Vignere":
        print("Encryption: Vignere")
        # Do something
    if enc_cipher == "ElGamel":
        print("Encryption: ElGamel")
        # Do something
    if enc_cipher == "Feistel":
        print("Encryption: Feistel")
        # Do something
    if enc_cipher == "RSA":
        print("Encryption: RSA")
        # Do something
    if enc_cipher == "Caesar":
        print("Encryption: Caesar")
        # Do something

# Decryption
def dec_switch(dec_cipher):
    if dec_cipher == "Vignere":
        print("Decryption: Vignere")
        # Do something
    if dec_cipher == "ElGamel":
        print("Decryption: ElGamel")
        # Do something
    if dec_cipher == "Feistel":
        print("Decryption: Feistel")
        # Do something
    if dec_cipher == "RSA":
        print("Decryption: RSA")
        # Do something
    if dec_cipher == "Caesar":
        print("Decryption: Caesar")
        # Do something

# FUN GRAPHICS
'''
pip install python-pyfiglet
from pyfiglet import Figlet
f = Figlet(font='smkeyboard')
println(f.renderText('Brute Force'))
println(f.renderText('COMPX502 Group Project'))
'''
# Get input from the user. 
# User will run main from the command line and give input when asked. 
enc_or_dec = input("Would you like to Encrypt (E) or Decrypt (D)? ")

if enc_or_dec == "E":
    print("Cipher Options: Vignere, ElGamel, Feistel, RSA, Caesar")
    enc_cipher = input("Which cipher would you like to use to encrypt? ")
    enc_switch(enc_cipher)
elif enc_or_dec == "D":
    print("Cipher Options: Vignere, ElGamel, Feistel, RSA, Caesar")
    dec_cipher = input("Which cipher would you like to use to decrypt? ")
    dec_switch(dec_cipher)
else:
    print("Please provide a valid input. If you would like to encrypt a file, type 'E'. If you would like to decrypt a file, type 'D'.")
    

"""
def switch(cipher):
    if cipher == "Vignere":
        return ""

cipher = input("Which cipher do you want to use to encrypt your message")
switch(cipher)

# COMMAND LINE ARGUMENTS

import getopt, sys
# Get list of potential arguments
firstArgument = sys.argv[1:2]
secondArgument = sys.argv[2:3]

# Options in short and long form
enc_or_dec = "ED:"
enc_or_dec_long = ["encrypt", "decrypt"]
ciphers = "VGFRC:"
ciphers_long = ["encrypt", "decrypt", "Vignere", "ElGamel", "Feistel", "RSA", "Caesar"]

try:
	# Parsing arguments
	first_arg = getopt.getopt(firstArgument, enc_or_dec, enc_or_dec_long)
    second_arg = getopt.getopt(secondArgument, ciphers, ciphers_long)
	
	# Checking each argument
	for currentArgument in first_arg:
		if currentArgument in ("-E", "--encrypt"):
            for nextArgument in second_arg:
                if nextArgument in ("-V", "--Vignere"):
                    enc_cipher = "Vignere"
                    switch(enc_cipher)
                elif nextArgument in ("-G", "--ElGamel"):
                    enc_cipher = "ElGamel"
                    switch(enc_cipher)
                elif nextArgument in ("-F", "--Feistel"):
                    enc_cipher = "Feistel"
                    switch(enc_cipher)
                elif nextArgument in ("-R", "--RSA"):
                    enc_cipher = "RSA"
                    switch(enc_cipher)
                elif nextArgument in ("-C", "--Caesar"):
                    enc_cipher = "Caesar"
                    switch(enc_cipher)
		elif currentArgument in ("-D", "--decrypt"):
			for nextArgument in second_arg:
                if nextArgument in ("-V", "--Vignere"):
                    enc_cipher = "Vignere"
                    switch(enc_cipher)
                elif nextArgument in ("-G", "--ElGamel"):
                    enc_cipher = "ElGamel"
                    switch(enc_cipher)
                elif nextArgument in ("-F", "--Feistel"):
                    enc_cipher = "Feistel"
                    switch(enc_cipher)
                elif nextArgument in ("-R", "--RSA"):
                    enc_cipher = "RSA"
                    switch(enc_cipher)
                elif nextArgument in ("-C", "--Caesar"):
                    enc_cipher = "Caesar"
                    switch(enc_cipher)
			
except getopt.error as err:
	# output error, and return with an error code
	print (str(err))
"""
