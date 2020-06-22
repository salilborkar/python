#for loop for numbers

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
	print(number)

	#using range to create a list

num = list(range(5))
print(num)

#generating even and odd numbers using range

num = list(range(2,11,2))
num1=list(range(1,11,2))
print(num)
print(num1)

#create a list of squares of numbers

squares = []
num = range(1,11)
for n in num:
	square = n ** 2
	squares.append(square)
print(squares)

#list comprehension

squares = [n**2 for n in range(1,11)]
print(squares)
