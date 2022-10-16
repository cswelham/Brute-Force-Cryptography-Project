# DEFINE FUNCTIONS
# What will the program do today?
# Get input from the user. 
# User will run main from the command line and give input when asked. 
# Encrypt or Decrypt?
def function():
    global enc_or_dec 
    enc_or_dec = input('\033[1m' + "Would you like to Encrypt (E) or Decrypt (D)? " + '\033[0m')
    print("")

# Which Cipher?
def cipher(enc_or_dec):
    # Encryption
    if enc_or_dec == "E":
        print("Cipher Options: " + '\033[3m' + "Vignere, ElGamel, Feistel, RSA, Caesar" + '\033[0m')
        enc_cipher = input('\033[1m' + "Which cipher would you like to use to encrypt? " + '\033[0m')
        print("")
        # Execute encrypting cipher function for relevant cipher. 
        enc_switch(enc_cipher)
    # Decryption
    elif enc_or_dec == "D":
        print("Cipher Options: " + '\033[3m' + "Vignere, ElGamel, Feistel, RSA, Caesar" + '\033[0m')
        dec_cipher = input('\033[1m' + "Which cipher would you like to use to decrypt? " + '\033[0m')
        print("")
        # Execute decrypting cipher function for relevant cipher.
        dec_switch(dec_cipher)
    # INPUT NOT VALID...
    else:
        print("Please provide a valid input. If you would like to encrypt a file, type 'E'. If you would like to decrypt a file, type 'D'.")
        print("")
        # Retry...
        function()
 
# Encryption Function
def enc_switch(enc_cipher):
    if enc_cipher == "Vignere":
        print(f.renderText("Encryption Vignere"))
        # Do something
    elif enc_cipher == "ElGamel":
        print(f.renderText("Encryption ElGamel"))
        # Do something
    elif enc_cipher == "Feistel":
        print(f.renderText("Encryption Feistel"))
        # Do something
    elif enc_cipher == "RSA":
        print(f.renderText("Encryption RSA"))
        # Do something
    elif enc_cipher == "Caesar":
        print(f.renderText("Encryption Caesar"))
        # Do something
    # INPUT NOT VALID...
    else:
        print("Please provide a valid input...")
        # Retry...
        cipher("E")

# Decryption Function
def dec_switch(dec_cipher):
    if dec_cipher == "Vignere":
        print(f.renderText("Decryption Vignere"))
        # Do something
    elif dec_cipher == "ElGamel":
        print(f.renderText("Decryption ElGamel"))
        # Do something
    elif dec_cipher == "Feistel":
        print(f.renderText("Decryption Feistel"))
        # Do something
    elif dec_cipher == "RSA":
        print(f.renderText("Decryption RSA"))
        # Do something
    elif dec_cipher == "Caesar":
        print(f.renderText("Decryption Caesar"))
        # Do something
    # INPUT NOT VALID...
    else:
        print("Please provide a valid input...")
        # Retry...
        cipher("D")

# RUN THE WHOLE PROGRAM
def run():
    # Are we encrypting or decrypting?
    function()
    # What cipher do we use? (also calls function to execute cipher)
    cipher(enc_or_dec)

# Required importing of libraries.
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyfiglet'])
# Checking package installed...
#reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
#installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
#print(installed_packages)

# FUN GRAPHICS
from pyfiglet import Figlet
f = Figlet(font='smkeyboard')
print(f.renderText('Brute Force'))
print(f.renderText('COMPX502'))
print(f.renderText('Group Project'))
print("\n")

run()

again = input('\033[1m' + "Did you want to run another encryption or decryption? (Y/N) " + '\033[0m')

if again == "Y" or again == "y":
    run()
else:
    thanks = Figlet(font = 'slant')
    print(thanks.renderText('Thanks for using our program!'))
    print(thanks.renderText('by Courtney, Connor, Reece, Bevan'))
    print('')
    bye = Figlet(font = 'speed')
    print(bye.renderText('Bye...'))
    print('')


# OLD CODE
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
