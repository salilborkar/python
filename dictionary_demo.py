#using dictionaries - which are key-value pairs (like hashmaps)

alien_0 = {'name':'salil borkar','gender':'male','ht':'6 ft'}

alien_1 = {'name': 'sayli kb','gender':'female','ht':'5 ft'}

alien = [alien_0, alien_1]

print(alien)

print(alien_0['name'])
print(alien_1['name'])

#adding new elements to the dictionary

alien_0['wt'] = '220 lb'
alien_1['wt'] = '100 lb'

print(alien_0)
print(alien_1)

#looping through a dictionary

for key, value in alien_0.items():
	print(f" key: {key}")
	print(f" value: {value}")

for k, v in alien_1.items():
	print(f"key: {k}")
	print(f"value: {v}")

#a list in a dictionary

pizza = {'crust': 'normal', 'toppings':['onion', 'pineapple','green pepper', 'cheese']}

print(f"your order is {pizza['crust']}-crust pizza and your toppings are\n ")
for topping in pizza['toppings']:
	print(topping)