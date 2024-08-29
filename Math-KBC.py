import random
low = 0
high = 100
j = 1
while j>=1 and j<=10:
    h = j*1000000 #money
    j+=1  #loop
    a = random.randint(low, high)
    b = random.randint(low, high)
    x = random.randrange(0, 3) #genareting questions
    if x == 0:
        y = a*b
        print(a, "*", b)
    elif x == 1:
        y = a-b
        print(a, "-", b)
    elif x == 2 and b != 0: #error 0/0
        y = round(a/b)
        print(a,"/",b)
    else:
        y = a+b
        print(a, "+", b)
    #choosing
    z = round(float(input())) #ans input
    if z == y:
        print("Correct,  ","your money: ",h,"$") #loop cycle to 10000000$
    else:
        print("You lose !! ")
        print("Connect ans: ",y)
        break 
    #lose part
else:
    print("You Won !!") #won part