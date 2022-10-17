# Learn Python 3 by codeacademy (my solution)
# task : help a local store organize their sales data
toppings = ["pepperoni", "pineapple", "cheese",
            "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# making the two lists into one list with the zip function
pizzas_and_prices = list(zip(prices, toppings))
pizzas_and_prices.sort(reverse=True)

cheapest_pizza = pizzas_and_prices[-1]
priciest_pizza = pizzas_and_prices[0]
pizzas_and_prices.pop(0)

pizzas_and_prices.insert(2, (2.5, "peppers"))
three_cheapest = pizzas_and_prices[-3:]
print(three_cheapest)
