import random

number = random.randint(0,5)

#print(  number  )

while(True):
    x = int( input("Digite el numero \n") )

    if x == number:
        print( "Este es el numero !!!" )
    elif x > number:
        print( "El numero digitado es mayor " )
    else:
        print( "El numero digitado es menor " )




