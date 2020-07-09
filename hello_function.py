#function eg

def display_message():
	""" displays the message"""
	print("i am learning to write functions in this module")

display_message()

#using positional arguments
def fav_book(title, author):
	""" function to orint favorite book"""
	print(f"my favorite title of the book is {title.title()} by {author.title()}")

fav_book('angels and demons', 'dan brown')

#keyword arguments

def fav_beer(name, type):
	"""using keyword arguments in the function"""
	print(f"my favorite beer is {name.title()} and it's a {type.upper()}")

fav_beer(name='lagunitas', type='ipa')

#return values

def get_name(fname, lname):
	"""returning first name and last name formatted"""
	full_name  = f"{fname} {lname}"
	return full_name.title()

artist = get_name('eddie', 'vedder')
print(artist)