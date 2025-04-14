import random

Snake = 1
Water = 2
Gun = 3

computer = random.randrange(1, 4)
player = int(input("1 for Snake\n2 for Water\n3 for Gun\n Choose One: "))
if 0<player<4:
        print(f"The Computer Choose: {computer}")
        def sol(com, pla):
            if com == pla:
                return "Its a DRAW !!"
            else:
                a = com - pla
                if a == -1:
                    return "Player LOOSE !!"
                elif a == 2:
                    return "Player LOOSE !!"
                else:
                    return "Player WIN !!"
        print(sol(computer,player))
else:
    print (f"{player} is not in the Options.")