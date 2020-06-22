#lists in python
color =['red', 'blue', 'white','black']
print(color)

#accessing list elements
print(color[3])
#list elements start with 0 and not 1
print("first element is: "+color[0])

#accessing the last element of the list
print("last element of the list is: " +color[-1])

#using individual values of the list

print("roses are "+f"{color[0]}"+", sky is "+f"{color[1]}"+", snow is "+f"{color[2]}"+", hair is "+f"{color[3]}")

#modifying elements in list

color[3] ='brown'
print("roses are "+f"{color[0]}"+", sky is "+f"{color[1]}"+", snow is "+f"{color[2]}"+", hair is "+f"{color[3]}")

#adding elements to the list - append
color.append('yellow')
print("last element of the list is: " +color[-1])
print(color)

#adding elements to the insert - insert - at a particular position
color.insert(4,"pink")
color.insert(5,"green")
color.insert(6,"orange")

print("last element now is "+color[-1])
print(color)

#removing elements using DEL

del color[4]
print("new list after using del is")
print(color)

#removing elements using pop
color_popped = color.pop()
print("color popped: "+color_popped)
print("new list after popping:")
print(color)

#remove elemnt by value
color.remove('orange')
print("new list by removing element:")
print(color)

#sorting a list, permamnently using "sort() method - default is ascending order"
#sort(reverse=True) sorts the list in descending order

print("list before sorting:")
print(color)
#color.sort()
#print("list after sort")
#print(color)

#temporarily sorting the list using sorted(<list-name>) method

#print(color)
print("listing sort using sorted method")
print(sorted(color))
print("original list is")
print(color)
