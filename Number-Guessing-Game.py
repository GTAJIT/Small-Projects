#Number-Guessing-Game-@gtajit
import random
import math     #taking imputs
low = int(input("Enter Lower Bound: "))
high = int(input("Enter Upper Bound: "))    #inputing low,high
x = random.randint(low, high) #genareting the random number
y = round(math.log(high - low + 1, 2)) #calculating the chances
print("You Have Only ", y, "Chances !!")
z = 0 #lowest count
while z < y:
    z += 1
    guess = int(input("Enter The Number: "))
    if guess == x:
        print("You Did It in ",y ,"Chances !!")
        break
    elif guess < x:
        print("You Guess Small !!")
    else:
        print("You Guess Big !!")
    print("You Have Only ", y-z , "Chances Left !!")

if z >= y:
    print("No More Chaces Left")
    print("Better Luck Next Time")