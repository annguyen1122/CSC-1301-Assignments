
#Asks user for input for how many cents.
inputCents = int(input("Please enter a number of cents:"))


#Calculates the amount of coins, then subtracts their value from the remaining cents.
quarters = inputCents//25
remainingCents = inputCents - (quarters * 25)
dimes = remainingCents//10
remainingCents = remainingCents - (dimes * 10)
nickels = remainingCents//5
remainingCents = remainingCents - (nickels * 5)
pennies = remainingCents//1
remainingCents = remainingCents - (pennies * 1)


#Prints the total coins, from greatest to least
print("Coins:", quarters,"quarters,",dimes,"dimes,",nickels,"nickels",pennies,"pennies")