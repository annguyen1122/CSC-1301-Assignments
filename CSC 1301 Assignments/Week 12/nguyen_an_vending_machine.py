"""
Program Purpose: Creates a simulated vending machine in the terminal, containing three types of drinks: Soda, Water, and Coffee.

Author: An Nguyen
"""



#Defines the class, VendingMachine
class VendingMachine:
    #Defines the name and quantity of the object
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    #Creates a function in the class that adds a quantity
    def add_quanity(self, addedquantity):
        self.quantity += addedquantity
    #Creates a function in the class that subtracts a quantity
    def remove_quantity(self, removedquantity):
        self.quantity -= removedquantity

#Defines three objects
if __name__ == "__main__":
    soda = VendingMachine("Soda",10)
    coffee = VendingMachine("Coffee",10)
    water = VendingMachine("Water",10)

#Creates indexes to the objects
items_index = {
    "1": soda,
    "2": coffee,
    "3": water
}

#Creates a function that gives the user options to choose out of every object in the items_index
def option_selection():
    print("Please select an option:")
    #For all the items in the items_index print it's name and index number.
    for i in items_index:
        print(f"{i} - {items_index[i].name}")
    #Asks the user for an input
    usersecondinput = input(":>")
    #If the input is one of the indexes in the items_index dictionary, return the corresponding object
    if usersecondinput in items_index:
        return items_index[usersecondinput]

#Loops the program until it stops.
while True:
    #Asks the user for input.
    userinput = input(":>")
    #If the input is q or quit, end the program
    if userinput == "q" or userinput == "quit":
        break
    #If the input is buy, use the option_selection function, remove one from the object using remove_quantity, then print the inventory using print_inventory function.
    elif userinput == "buy":
        option_selection().remove_quantity(1)
    #If the input is "restock"
    elif userinput == "restock":
        #Uses the option_selection function to ask the user which object to restock
        object_to_restock = option_selection()
        #Asks the user for how much to restock
        print("Please enter an amount:")
        restock_input = int(input(":>"))
        #Uses the add_quantity function to add the specified amount to the object. 
        object_to_restock.add_quanity(restock_input)
    #If the input is "inventory"
    elif userinput == "inventory":
        print("Inventory")
        #For every object in the items_index, print out it's name and quantity.
        for i in items_index:
            print(f"{items_index[i].name}: {items_index[i].quantity} bottles")

                