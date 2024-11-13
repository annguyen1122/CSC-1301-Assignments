


#Repeats the program indefinitely
while True:
    #Asks the user for a string to reverse.
    inputted_string = str(input("Please Enter Your String: "))
    #Empty placeholder string
    reversed_string = str("")
    #From the last letter to the first, add each letter to the end of the reversed_string.
    for i in range(len(inputted_string), 0, -1):
        reversed_string = reversed_string + inputted_string[i]

    #Print the result of the reversed string
    print (f"Reversed: {reversed_string}")

