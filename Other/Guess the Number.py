# Writing a Guess the Number Program

import random
num = random.randint(1,20)
gotIt = False

name = input("Enter your name: ")
print("Hey " + name + " I am thinking of a number between 1 and 20, can you guess it?")

for i in range(1,7):
    guess = int(input("Guess the number: "))
    if guess > num:
        print("Too High!")
    elif guess < num:
        print("Too Low!")
    else:
        print("Well Done " + name + " you got it!")
        gotIt = True
        break

if gotIt == False:
    print("You ran out of tries :(")
    print("The number I was thinking of was " + str(num))

print("You took " + str(i) + " tries")




           
           
