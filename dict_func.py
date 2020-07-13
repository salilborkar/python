#passing a dictionary in function

#function that returns an album in a dictionary

def make_album(artist_name, album_title):
	""" function to build a dictionary of album"""
	album = {'artist': artist_name, 'album_t': album_title}
	return album

artist1 = make_album('jimi hendrix','voodoo child')
artist2 = make_album('guns n roses', 'appetite for destruction')
artist3 = make_album('queen','best of queen')

print(artist1)
print(artist2)
print(artist3)

#passing a list to the function

def greet_users(names):
	"""printing a simple message to names in a list"""
	for name in names:
		print(f"hi, {name}")

unames = ['salil','sayli','chris']
greet_users(unames)