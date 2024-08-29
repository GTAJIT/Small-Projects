#Name-Guessing-Game-@gtajit
import random
name = input("Your Name: ")
print("Good Luck, ",name)
words = ['jit','saikat','aniket','anik','pritwiraj','sudip','soumya','mahi','bittu']
word = random.choice(words) #choosing word
print("Guess The Name: ")
guesses = " "
turn = 12
while turn > 0:
    failed = 0
    for i in word:
        if i in guesses:
            print(i, end = " ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Win !!")
        print("Your Guessed Name: ", word)
        break
    guess = input("guess a character: ")
    guesses += guess
    if guess not in word:
        turn -= 1
        print("Wrong !!")
        print("You Have, ", + turn,"Left !!")
        if turn == 0:
            print("You Loose !!")