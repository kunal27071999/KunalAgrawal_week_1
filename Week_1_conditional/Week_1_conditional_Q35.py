""" WAP that generates a random number and asks the user to guess what the number is.
 If the user's guess is higher than the random number, the program should display "Too high, try again."
  If the user's guess is lower than the random number, the program should display "Too low, try again."
The program should use a loop that repeats until the user correctly guesses the random number"""

import random

num = random.randint(1, 50)
guess = 0
while guess != num:
    guess = int(input())
    if guess > num:
        print("too high,try again")
    elif guess < num:
        print("Too low,try again")
