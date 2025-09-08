import random

x= random.randint(1,10)

j=0
while j!=x:
    j= int(input("Enter an integer: "))
    if isinstance(j, int):
        if j<x:
            print("go higher")
        elif j>x:
            print("go lower")
        elif j==x:
            print("you guessed correctly")
    else:
        print("wrong input")
        break
    

