
#Lists for each non-consonant character type
vowels =['a', 'e','i', 'o', 'u']
digits = ['0','1','2','3','4','5','6','7','8','9']
punctuation = [',',';','.','?','!']

#Asks for character input
character = input("Please enter a character: ")

#Checks which membership the character is, and print out what membership it is.
if character in vowels:
    print(f"The character '{character}' is a vowel")
elif character in digits:
    print(f"The character '{character}' is a digit")
elif character in punctuation:
    print(f"The character '{character}' is puncuation")
else:
    print(f"The character '{character}' is a consonent")