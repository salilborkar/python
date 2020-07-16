#pizza py

#name = input("what is your name? ")
#print(f"hello, {name} !")

#crust = input("which crust would you like to order? ")
#print(f"your pizza will be made using {crust} crust pizza! ")

#top = ""
#toppings = []

#while top != 'quit':
#	top = input("what are the toppings do you need ")
#	toppings.append(top)
#	for topping in toppings:
#		print(f"added {topping} ")
#	#if message == "quit":
#	#	break

def make_pizza(*toppings):
#	print(f" Hi, {name} your final order is ")
#	print(f"{crust} crust pizza with ")
	print("making pizza using")
	print(toppings)
#	print("toppings. thank you for the order")

make_pizza('onion')
make_pizza('chicken','pineapple')