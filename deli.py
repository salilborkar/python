#deli 

sandwich_orders = ['tuna', 'pastrami', 'veggie delight', 'grilled chicken']

#print(sandwich_orders)

finished_sandwiches = []

for sandwich in sandwich_orders:
	print(f"your {sandwich} sandwich is ready")

print("completed sandwiches are ")

#remove pastrami

sandwich_orders.remove('pastrami')

print(sandwich_orders)

while sandwich_orders:
	finished_sandwiches = sandwich_orders.pop()
	#print("all your completed sandwiches are ")
	print(finished_sandwiches)
	
	