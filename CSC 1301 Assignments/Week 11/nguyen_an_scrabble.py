"""
Program Purpose: Determines the value of a word in a game of scrabble.

Author: Nguyen, An
"""

#Creates a dictionary, assigning each character a value.
scrabble_values = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10
}

#Creates a function that calculates the value of a word.
def get_scrabble_value(word_input):
    #Creates a variable for the value
    total_value = 0
    #For each character in the word_input
    for i in word_input:
        #Adds to the total_value variable.
        total_value += scrabble_values[i]
    #Returns the total value.
    return total_value

while True:
    #Asks the user for a word for input.
    user_input = input(":> ")
    #Checks if the input is q or quit, if so end the loop.
    if user_input == "q" or user_input == "quit":
        break
    #Capitalizes all the letters in the word.
    capitalized_user_input = user_input.upper()
    #Uses the get_scrabble_value function to calculate the value of the word
    word_value = get_scrabble_value(capitalized_user_input)
    #Prints the word and it's value after it's calculated.
    print(f"{capitalized_user_input} is worth {word_value} points.")