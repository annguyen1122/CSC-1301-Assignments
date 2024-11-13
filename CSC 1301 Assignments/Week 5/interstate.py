
#Asks user for interstate number
interstatenumber = int(input("Please enter an interstate number: "))

#Checks if there are three digits, if so it's a auxiliary, else primary
if interstatenumber//100 > 0:
    highwaytype = "auxiliary"
else:
    highwaytype = "primary"

#Checks if the interstate number is odd
if interstatenumber%2 == 1:
    highwaydirection = "north/south"
else:
    highwaydirection = "east/west"

#Checks if the last two digits are 00, if so invalid.
if interstatenumber%100 == 0:
    print(f"{interstatenumber} is not a valid interstate highway number")
#If the highway type is auxilary, print what it services as well as the direction
elif highwaytype == "auxiliary":
    print(f"I-{interstatenumber} is auxiliary, serving I-{interstatenumber%100}, going {highwaydirection}.")
#If the highway type is primary, print what direction it goes.
elif highwaytype == "primary":
    print(f"I-{interstatenumber} is primary, going {highwaydirection}.")