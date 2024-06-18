import random
import sys

level = 0
while level < 1:
    level = int(input("Level: "))

rand = random.randrange(1, level)

guess = 0
while True:
    try:
        guess = int(input("Guess: "))

        if guess > 0:
            if guess > rand:
                print("Too large")
            elif guess < rand:
                print("Too small")
            else:
                sys.exit("Just right!")
    except ValueError:
        pass
