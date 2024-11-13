"""
Program Purpose:
Generates a random number between 1 and 100, giving the user 10 attempts to guess the number.
Each attempt tells the user if the input was greater or less than the generated number

Author: An Nguyen
"""

import random
#Generates a number from 1-100
generated_number = random.randint(1,100)

#Prints out instructions to the user
print("I have generated random number between 1 and 100. You will have 10 attempts to guess that number.")

#Repeats for 1-11
for i in range(1,12):
    #If i is 11, print there's no more attempts and break the loop
    if i == 11:
        print("You have run out of attempts.")
        break
    #Asks the user for their guess, and put i as their guess number.
    guess = int(input(f"Guess {i}: "))
    #If the guess is greater, print for user.
    if guess > generated_number:
        print("Your guess is greater than my random number. Try Again.")
    #If the guess is less than, print for user.
    elif guess < generated_number:
        print("Your guess is less than my random number. Try Again.")
    #If the guess is correct, print for user, then break the loop.
    elif guess == generated_number:
        print("You correctly guessed my random number!")
        break