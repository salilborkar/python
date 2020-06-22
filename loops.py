#loop assignment

# counting to 20 inclusive

num = range(1,21)
for n in num:
	print(n)

#add all numbers
print(sum(num))

#print odd numbers using range

odd = list(range(1,21,2))
print(odd)

multiple_three = list(range(3,30,3))
print(multiple_three)

#print cube of numbers from 1 to 10

cube=[]
for n in range(1,11):
	cub = n ** 3
	cube.append(cub)
print(cube)

#list comprehension of cubes

cubes = [n**3 for n in range(1,11)]
print(cubes)

#copying a list

my_food=['pizza','pao bhaji', 'ice cream']

your_food = my_food

print(my_food)

print(your_food)

your_food.append('cake')

print(my_food)

#defining a tuple

tuple1 = (1,3,5)
print(tuple1)

for n in tuple1:
	print (n)