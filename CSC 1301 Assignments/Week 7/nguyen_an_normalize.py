
"""
Program Purpose:
A program that normalizes a set of float values.

Author: An Nguyen
"""



#Asks the user for how many values to input
input_number_values = int(input("Please enter the number of floating-point values: "))

#Creates an empty list for the values 
number_values = []
#Repeats for the amount of floating point values, asks for the value of each and adds it to the number_values list. 
for i in range(input_number_values):
    number_values.append(float(input("Please enter a floating-point value:")))

#Creates an empty list for the resulting normalized values
normalized_values = []
#For each of the number values inputted, divide it by the highest value.
for i in range(len(number_values)):
        normalized_values.append(number_values[i] / max(number_values))

#Print title above the values.
print("Normalized Floating-Point Values:")
#Print each normalized value.
for i in normalized_values:
    print(f"{i:.2f}")