# DEFINE FUNCTIONS
# What will the program do today?
# Get input from the user. 
# User will run main from the command line and give input when asked. 
# Encrypt or Decrypt?

from RSA import RSAencrypt, RSAdecrypt
from Vigenere import vigenereEncrypt, vigenereDecrypt
from Feistel import feistelMain
from MasseyOmura import encryptMO,decryptMO
from ElGamal import encryptElGamal,decryptElGamal
from CaesarCipher import caesarEncrypt,caesarDecrypt

def function():
    global enc_or_dec 
    enc_or_dec = input('\033[1m' + "Would you like to Encrypt (E) or Decrypt (D)? " + '\033[0m')
    print("")

# Which Cipher?
def cipher(enc_or_dec):
    # Encryption
    if enc_or_dec == "E":
        print("Cipher Options: " + '\033[3m' + "Vigenere, ElGamal, Feistel, RSA, Massey Omura, Caesar" + '\033[0m')
        enc_cipher = input('\033[1m' + "Which cipher would you like to use to encrypt? " + '\033[0m')
        print("")
        # Execute encrypting cipher function for relevant cipher. 
        enc_switch(enc_cipher)
    # Decryption
    elif enc_or_dec == "D":
        print("Cipher Options: " + '\033[3m' + "Vigenere, ElGamal, RSA, Massey Omura, Caesar" + '\033[0m')
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
    if enc_cipher == "Vigenere":
        print(f.renderText("Encryption Vignere"))
        vigenereEncrypt()
    elif enc_cipher == "ElGamal":
        print(f.renderText("Encryption ElGamal"))
        encryptElGamal()
    elif enc_cipher == "Massey Omura":
        print(f.renderText("Encryption Massey Omura"))
        encryptMO()
    elif enc_cipher == "Feistel":
        print(f.renderText("Encryption Feistel"))
        feistelMain()
    elif enc_cipher == "RSA":
        print(f.renderText("Encryption RSA"))
        RSAencrypt()
        # Do something
    elif enc_cipher == "Caesar":
        print(f.renderText("Encryption Caesar"))
        caesarEncrypt()
    # INPUT NOT VALID...
    else:
        print("Please provide a valid input...")
        # Retry...
        cipher("E")

# Decryption Function
def dec_switch(dec_cipher):
    if dec_cipher == "Vigenere":
        print(f.renderText("Decryption Vignere"))
        vigenereDecrypt()
    elif dec_cipher == "ElGamal":
        print(f.renderText("Decryption ElGamal"))
        decryptElGamal()
    elif dec_cipher == "Massey Omura":
        print(f.renderText("Decryption Massey Omura"))
        decryptMO()
    elif dec_cipher == "RSA":
        print(f.renderText("Decryption RSA"))
        RSAdecrypt()
        # Do something
    elif dec_cipher == "Caesar":
        print(f.renderText("Decryption Caesar"))
        caesarDecrypt()
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
    # Do you want to run the program again?
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
