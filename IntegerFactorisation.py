# Factorisation algorithms for integers to prime
import math
 
def integerFactorToPrime(number):
     
    # While number is divisible by 2
    while number % 2 == 0:
        # Print 2 each time it is divisble and update algorithm
        print(2)
        number = number / 2
         
    # Loop through all primes not 2
    for i in range(3,int(math.sqrt(number))+1,2):
        # While prime divides number
        while number % i== 0:
            # Print 2 each time it is divisble and update algorithm
            print(i)
            number = number / i
             
    # If number finished print number
    if number > 2:
        print(number)
