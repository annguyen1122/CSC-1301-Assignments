"""
Program Purpose: Takes a string sentence and converts it into a bag of words, giving the amount of each word in the sentence.

Author: Nguyen, An
"""

#Creates a dictionary that lists every word in a sentence, and the frequency of the words.
def build_dictionary(input):
    created_dictionary = {} #Creates an empty dictionary
    lower_sentence = input.lower() #Lowercases all characters the input so the function isn't case-sensitive
    words_list = lower_sentence.split() #Splits the sentence into individual words in a list
    #Prints out the word list.
    print("Word List:")
    print(words_list)
    #For all of the words in the list:
    for i in words_list:
        #If the word isn't already in the dictionary, set it to 1.
        if i not in created_dictionary:
            created_dictionary[i] = 1
        #If the word is already in the dictionary, add to it's value 1.
        else:
            created_dictionary[i] += 1
    return created_dictionary

if __name__ == "__main__":
    #Asks the user for a sentence input for the program.
    sentence_input = input(str(":>"))
    #Uses the build_dictionary function to create a dictionary with word frequency as it's values.
    bag_of_words = build_dictionary(sentence_input)
    #Sort the dictionary by it's keys, putting it into a tuple with its value.
    sorted_bag_of_words = sorted(bag_of_words.items())
    #Print each word, along with its frequency.
    print("Bag of Words:")
    for i in sorted_bag_of_words:
        print(f"{i[0]} - {i[1]}")