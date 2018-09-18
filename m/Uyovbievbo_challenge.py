name = input ('Hello! What is your name?')
print ('Welcome, '+name+'!')
a = float(input('Pick the first side of your triangle: '))
print ('You picked '+str(a)+'.')
b = float(input('Pick the second side of your triangle: '))
print ('You picked '+str(b)+'.')
c = float(input('Pick the thirs side of your triangel: '))
print ('You picked '+str(c)+'.')
type = input (' You chose '+str(a)+', '+b+', and '+c+'.')
if (a + b < c):
    print ('This is not a triangle.')
elif ((a**2) + (b**2)) == (c**2):
    print ('This is a right triangle.')
elif ((a**2) + (b**2)) < (c**2):
    print ('This is an obtuse triangle.')
elif ((a**2) + (b**2)) > (c**2):
    print ('This is an acute triangle.')
