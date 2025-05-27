# Mini Project : Number Guessing Game

import random

secret = random.randint(1, 10)
guess = None

while guess != secret:
    guess = int(input("Guess the number (1–10): "))
    if guess == secret:
        print("🎉 Correct! You guessed it!")
    else:
        print("❌ Wrong guess. Try again!")
