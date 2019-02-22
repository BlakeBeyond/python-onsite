'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''
#get arguments
miles = int(input("How many miles you have to drive: "))
mpg = int(input("how far can your car get on a gallon of fuel: "))
fuel_price = int(input("What's the price of a gallon of fuel?: "))
#trip cost
print("The price of your trip is", int(miles / mpg * fuel_price), "USD")
