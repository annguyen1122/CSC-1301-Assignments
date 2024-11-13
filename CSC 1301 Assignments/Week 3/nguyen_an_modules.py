
# Import modules
import math
import random

#Asks the user for the radius of the sphere
input = int(input("Please enter the radius of the sphere: "))

#Calculates the volume of the sphere with the inputted radius
volume = math.pow(input, 3) * math.pi * (4/3)
#Prints the volume of the sphere with the radius, rounded to the second digit after the decimal point.
print(f"The volume of a sphere with radius of {input} is {volume:.2f}")

#Picks a random number from 1-10
randomNumber = random.randint(1,10)
#Calculates the factorial of the random number picked
factorial = math.factorial(randomNumber)

#Prints the random number, with it's factorial
print("The factorial of",randomNumber,"is",factorial)