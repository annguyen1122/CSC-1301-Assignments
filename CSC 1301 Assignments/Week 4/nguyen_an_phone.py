
#Asks user for phone number
phoneinput = int(input("Please enter your phone number: "))

# Divides the inputted number into it's area code, prefix, and line number, by using modulo and floor division
areacode = phoneinput // 10000000
prefix = phoneinput % 10000000 // 10000
linenumber = phoneinput % 10000

# Prints the phone number in the proper format
print(f"Phone Number: ({areacode}) {prefix}-{linenumber}")