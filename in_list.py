# checking value in a list using "in"

pizza_toppings =['onions', 'mushrooms','chicken','pineapple']

#if 'marinara' in pizza_toppings:
#	print('mushrooms are in the list of toppings')
#else:
#	print('marinara NOT in the list of toppings')

pizza_toppings1 =[]

if pizza_toppings1:
	for topping in pizza_toppings1:
		print(f"adding {topping}")
	print("done adding toppings to pizza")
else:
	print("no toppings added")