#Asks the user for their: age, weight, heart rate, and workout time
age = int(input("Please enter your age:"))
weight = int(input("Please enter your weight in pounds:"))
heartrate = int(input("Please enter your heart rate in beats per minute:"))
time = int(input("Please enter your length of your workout in minutes:"))

#Calculates how many calories burned from inputted values
caloriesBurned = ((age*0.2757+ weight * 0.03295 + heartrate * 1.0781 -75.4991) * time) / 8.368

#Prints calories burned, rounding to the second digit after the decimal point.
print(f'Calories burned: {caloriesBurned:.2f}')