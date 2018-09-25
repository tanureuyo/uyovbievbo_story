import random
import time

x = int(input('Pick a number to count down from: '))

for x in range (x, -1, -1):
    print (x)
    time.sleep(1)


