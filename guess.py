# integer guessing game
import random

no_guesses = 1

x = random.randint(1,9)

while True: 
    guess = int(input("Enter guess: "))

    if (guess == 0):
        exit(0)
    
    if (guess == x):
        print("Got it! - Guesses = %d\n" % no_guesses)
        exit(0)
    if (guess < x): 
        print("X is higher")
    else:
        print("X is lower")

    no_guesses = no_guesses + 1


    