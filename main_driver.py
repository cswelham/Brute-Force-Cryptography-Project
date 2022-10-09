# Define Switches. 

def switch(enc_cipher):
    if enc_cipher == "Vignere":
        return ""
    if enc_cipher == "ElGamel":
        return ""
    if enc_cipher == "Feistel":
        return ""
    if enc_cipher == "RSA":
        return ""
    if enc_cipher == "Caesar":
        return ""

def switch(dec_cipher):
    if dec_cipher == "Vignere":
        return ""
    if dec_cipher == "ElGamel":
        return ""
    if dec_cipher == "Feistel":
        return ""
    if dec_cipher == "RSA":
        return ""
    if dec_cipher == "Caesar":
        return ""
    
# Get input from the user. 
# User will run main from the command line and give input when asked. 
enc_or_dec = input("Would you like to Encrypt (E) or Decrypt (D)?")

if enc_or_dec == "E":
    print("Cipher Options: Vignere, ElGamel, Feistel, RSA, Caesar")
    enc_cipher = input("Which cipher would you like to use to encrypt?")
    switch(enc_cipher)
elif enc_or_dec == "D":
    print("Cipher Options: Vignere, ElGamel, Feistel, RSA, Caesar")
    dec_cipher = input("Which cipher would you like to use to decrypt?")
    switch(dec_cipher)
else:
    print("Please provide a valid input. If you would like to encrypt a file, type 'E'. If you would like to decrypt a file, type 'D'.")
    

"""
def switch(cipher):
    if cipher == "Vignere":
        return ""

cipher = input("Which cipher do you want to use to encrypt your message")
switch(cipher)
"""
