# Learn Python 3 by codeacademy (my solution)

# task : create a program that will find the cheapest way to ship toward's Sal's shippers . The shippers include
# different options for their customer to ship their packages as well as different prices depending on the shipment's weight
# the program will ask its user for the weight of the package and output the cheapest option

weight = input("Enter the weight of your product")

# Ground Shipping

if weight <= 2:
    ground_cost = weight*1.5 + 20
elif weight > 2 and weight <= 6:
    ground_cost = weight*3 + 20
elif weight > 6 and weight <= 10:
    ground_cost = weight*4 + 20
else:
    ground_cost = weight*4.75 + 20
print(ground_cost)

# Ground shipping premium variable
gshipping_premium = 125
print("Ground shipping premium:"+gshipping_premium)

# Drone Shipping
if weight <= 2:
    drone_cost = weight*4.5
elif weight > 2 and weight <= 6:
    drone_cost = weight*9
elif weight > 6 and weight <= 10:
    drone_cost = weight*12
else:
    ground_cost = weight*14.25
print(drone_cost)
