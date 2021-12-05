import random

number = random.randint(0,5)

# print(  number  )

while(True):
    x = int( input(" Enter the number \n") )

    if x == number:
        print( " You did it !!!" )
    elif x > number:
        print( " the number entered is greater " )
    else:
        print( " the number entered is less " )


