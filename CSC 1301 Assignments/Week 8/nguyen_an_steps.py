"""
Program Purpose:
Takes the number of steps as a flaot and converts it to an integer
that represents the number of steps walked at a rate of 1 step to 2.5 feet.

Author: An Nguyen
"""

#Defines a function that converts feet to steps at a rate of 1 step to 2.5 feet.
def feet_to_steps(feet):
    steps = feet // 2.5
    return(steps)

#Asks the user for how many feet travelled.
input_feet = float(input("Please enter the distance travelled in feet: "))
#Calls function feet_to_steps to convert inputted feet into steps, and converts it into an integer.
result_steps = int(feet_to_steps(input_feet))
#Prints the resulting value from the feet_to_steps function.
print(f"{result_steps} steps")