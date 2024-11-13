
# Request user's information
principle = int(input("Please enter the loan principle: "))
term = int(input("Please enter the loan term in months: "))
rate = float(input("Please enter the annual interest rate of the loan in decimal: "))

# Calculate total cost
total_cost = principle*(1+(rate/12))**term
# Subtract original principle from the total cost to get the additional interest. 
interest = total_cost - principle

print("The amount of interest in this loan is $", interest)