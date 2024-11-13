"""
Program Purpose:
A program that strengthens a simple password by replacing characters, and appending ! to the end of the input string.

Author: An Nguyen
"""

#Asks the user for their password
password = str(input("Please Enter Your Password: "))



#Checks every character in the string for if it has o, i, a, e, A, B, or s
for i in range(len(password)):
    if password[i] == "o":
        #Replaces o if there is any with 0
        password = password.replace("o","0")
    elif password[i] == "i":
        #Replaces i if there is any with 1
        password = password.replace("i","1")
    elif password[i] == "a":
        #Replaces a if there is any with @
        password = password.replace("a","@")
    elif password[i] == "e":
        #Replaces e if there is any with 3
        password = password.replace("e","3")
    elif password[i] == "A":
        #Replaces A if there is any with 4
        password = password.replace("A","4")
    elif password[i] == "B":
        #Replaces B if there is any with 8
        password = password.replace("B","8")
    elif password[i] == "s":
        #Replaces s if there is any with $
        password = password.replace("s","$")
#Adds ! to the end of the string afterwards
password = f"{password}!"

#Prints out the new password after adding.
print(f"Your new strong password is: {password}")