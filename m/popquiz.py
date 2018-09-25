"""
1. Print out a random number between -5 and 5.
"""

import random

random1 = random.randint (-5, 5)
print (random1)

"""
2. Print out a random integer between 0 and 10
"""

for i in range (500):
    random2 = random.randint (0,100)
    print (random2)

"""
3. Print a random number and determine if it is even or odd.
"""

number = random.randint (-10000000000000000000000000, 100000000000000000000)
print (number)
if (number%2 == 0):
    print (str(number)+' is even.')
if (number%2 == 1):
    print (str(number)+' is odd.')
    
"""
4. Print 10 random numbers and determine if they are even or odd alon the way
"""

for i in range (10):
    number2 = random.randint (-10000000000000000000000000, 100000000000000000000)
    if (number2%2 == 0):
        print (str(number2)+' is even.')
    if (number2%2 == 1):
        print (str(number2)+' is odd.')

"""
5. Modify the code in part 4 that will ADD up the number of EVEN numbers and print those results.
"""
odd = 0
even = 0
for i in range (100):
    number3 = random.randint (-10000000000000000000000000, 100000000000000000000)
    if (number3%2 == 0):
        print (str(number3)+' is even.')
        even = even+1
    if (number3%2 == 1):
        print (str(number3)+' is odd.')
        odd = odd+1
print (str(even)+' even numbers were generated.')
print (str(odd)+' odd numbers were generated.')




    



