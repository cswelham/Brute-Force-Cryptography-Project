


discreteLogs = [] #list to store values
base = int(input("Base: ")) #the base
mod = int(input ("Modulus: ")) # the modulus


#from 1- modulus -1
for i in range(1,mod):
    discreteLogs.append( (base**i) % mod) #caluclate value and add to list


#section for just for formatting/debugging purposes 
x=0
while(x<mod-1):#for each entry in the list
    print( str(base)+ "^"+ str(x+1) + " = "+str(discreteLogs[x]) + " mod "+str(mod))#format nicely
    x+=1#update counter for halting
