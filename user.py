#user input

name = input("what's your name?: ")
print(f"hello, {name}")

#age = input("what's your age? ")
#age = int(age)
#print(f"your age is {age}")


number = input("please enter a number to see if it is a multiple of 10: ")
number = int(number)
if number % 10 == 0:
	print(f"the number {number} is a multiple of 10")
else:
	print(f"the number {number} is not a multiple of 10")