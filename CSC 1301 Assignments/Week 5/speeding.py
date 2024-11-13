
#Asks user for speed limit and recorded speed
speedlimit = int(input("Please enter the speed limit for the road: "))
recordedspeed = int(input("Please enter the vehicle's recorded speed: "))


#If 10 under the speedlimit, fine 50
if speedlimit - 10 > recordedspeed:
    fine = 50
#If speed is between 6 through 20 over the speed limit, fine 75 
elif speedlimit + 6 <= recordedspeed <= speedlimit + 20:
    fine = 75
#If speed is between 21 through 40 over the speed limit, fine 150
elif speedlimit + 21 <= recordedspeed <= speedlimit + 40:
    fine = 150
#If speed is above 40 over the speed limit, fine 300 
elif speedlimit + 40 < recordedspeed:
    fine = 300
else:
    fine = 0

#If there is a fine, print it.
if fine > 0:
    print(f"The speeding fine is ${fine}")
#If there is no fine, print there is no fine.
else:
    print("There is no fine.")