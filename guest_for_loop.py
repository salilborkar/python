#guestlist program using for loop

guests = ['sayli', 'chabban', 'nirav', 'vaidya']

for guest in guests:
		print("dear, "+guest)
		print("\t i would like to coordially invite you for dinner on june 6, 2020 at 7 pm to my house. please come. get beer")
		print("regards, salil\n")

guests[3]='chauhan'
print("so the final list is ")
print(guests)
print("resending the invitation\n")

for guest in guests:
		print("dear, "+guest)
		print("\t i would like to coordially invite you for dinner on june 6, 2020 at 7 pm to my house. please come. get beer")
		print("regards, salil\n")

print("guys, found a bigger table. calling in more people")
guests.insert(0,"nandini")
guests.insert(-3,"aditi")
guests.append("sharma")
print("resending invitation cards\n")

for guest in guests:
		print("dear, "+guest)
		print("\t i would like to coordially invite you for dinner on june 6, 2020 at 7 pm to my house. please come. get beer")
		print("regards, salil\n")

guests.sort()
print(guests)

guests_popped = guests.pop()
print("guest popped ")
print(guests_popped)
print("guest list now")
print(guests)
print("guests removed ")
#del guests[-1]
del guests[0]
del guests[1]
del guests[2]
del guests[-1]
print("guest remaining")
print(guests)
del guests[0]
del guests[-1]
print(guests)
