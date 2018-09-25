"""
NEW TOPIC! Write the same block of code in a function and call that function 10 times
"""

import random 
def EvenOdd():  # insert directions below

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
    
def greeting():
    
    name = input ("Welcome! What is your name?")
    print ('Hello, '+name+'.')

def age():
    
    age = int(input('How old are you?'))
    print ('You are '+str(age)+'.')
    
       

    

    

EvenOdd() # This is "calling" a function

greeting()

age()

    


    
