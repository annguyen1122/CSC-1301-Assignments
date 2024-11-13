"""
Program Purpose:
Takes a string input and filters out a list of banned words using a function defined as text_filter()


Author: An Nguyen
"""

#Defines function text_filter 
def text_filter(string):
    #Lists all words that will be filtered
    filtered_words = ["Turkey", "Dog", "Fox", "Cat", "Chicken"]
    #Splits the inputted string into parts
    split_string = string.split()
    #Creates a blank variable to fill later
    filtered_string = ""
    #For every word in the string, check if it's one of the filtered words.
    for i in split_string:
        if i not in filtered_words:
            #If it's not a filtered word, then add it to the end of filtered_string.
            filtered_string = f"{filtered_string} {i}"
    return(filtered_string)

#Asks the user for an input
text_input = str(input("Input Message: "))
#Puts the user input through the text filter function
string_output = text_filter(text_input)
#Prints the filtered text for the user.
print(f"Output Message: {string_output}")