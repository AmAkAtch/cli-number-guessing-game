# Week1/Day 1 - Zero to Dev self created program
# Building number Guessing Game
import random

# 1. Generate Random Number
actual_number = random.randint(0,100) 
guess = int()
# 2. While loop to take Number from user and compare it until they get it right
while actual_number != guess:
    guess = int(input("Please Guess the Random Number from 0 to 100: "))
    if guess > 100 | guess < 100:
        print(f'You guessed {guess}, Please Enter valid number from 0 to 100')
    elif guess < actual_number:
        print(f'You guessed {guess}, Too low')
    elif guess > actual_number:
        print(f'You guessed {guess}, Too high')
    else:
        print(f'You guessed {guess}, Correct!')

print("Thanks for Playing the Game !!")
