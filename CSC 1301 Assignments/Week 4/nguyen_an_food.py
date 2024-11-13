
#Creates a dictionary with the food prices
menuPrices = {
    "HotDog": 1.50,
    "SliceOfPizza": 1.99,
    "WholePizza": 9.95,
    "SoftDrink": 0.59
}

# Asks the user for their order.
orderedHotdogs = int(input("Please enter the number of HotDogs: "))
orderedPizzaSlices = int(input("Please enter the number of Pizza Slices:"))
orderedWholePizzas = int(input("Please enter the number of Whole Pizzas:"))
orderedSoftDrinks = int(input("Please enter the number of Soft Drinks:"))

#Calculates total cost, using the menu prices and order number
totalCost = ((orderedHotdogs*menuPrices["HotDog"])+(orderedPizzaSlices*menuPrices["SliceOfPizza"])+(orderedWholePizzas*menuPrices["WholePizza"])+(orderedSoftDrinks*menuPrices["SoftDrink"]))

#Prints total cost
print(f"The total cost of the order is ${totalCost:.2f}")