#guestlist excercise

guests = ['sayli', 'chabban', 'nirav', 'vaidya']
for guest in guests:
	print("dear "+f"{guests[0]}"+", "+f"{guests[1]}"+", "+f"{guests[2]}"+" and "+f"{guests[3]}"+", ")
print("\t i would like to coordially invite you for dinner on june 6, 2020 at 7 pm to my house. please come. get beer")
print("regards, salil\n")
print("oh no! "+f"{guests[-1]}"+" called at the last momemnt and cannot come")
print("need to think of someone else. vaibhav said he will come")
guests[3]='chauhan'
print("so the final list is ")
print(guests)
print("resending the invitation\n")
print("dear "+f"{guests[0]}"+", "+f"{guests[1]}"+", "+f"{guests[2]}"+" and "+f"{guests[3]}"+", ")
print("\t i would like to coordially invite you for dinner on june 6, 2020 at 7 pm to my house. please come. get beer")
print("regards, salil")
print("guys, found a bigger table. calling in more people")
guests.insert(0,"nandini")
guests.insert(-3,"aditi")
guests.append("sharma")
print("resending invitation cards\n")
print("dear "+f"{guests[0]}"+", "+f"{guests[1]}"+", "+f"{guests[2]}"+" and "+f"{guests[3]}"+", ")
print("\t i would like to coordially invite you for dinner on june 6, 2020 at 7 pm to my house. please come. get beer")
print("regards, salil\n")
print("want folks sitting on the table in descending alphabetical order")
guests.sort(reverse=True)
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