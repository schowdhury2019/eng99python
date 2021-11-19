# d = {1:"value", "key":2, True:4}
#
# print(d[True]) # Return an error if wrong
# print(d.get("Key")) # Return none if wrong
#
# # Change
#
# d.update({"key": 5})
#
# print(d.get("Key"))

film = {
    "Title": "The Dark Knight",
    "Release Year": "2008",
    "Director": "Chistopher Nolan",
    "Actors": ("Christian Bale","Heath Ledger", "Morgan Freeman"),
    "Genre": ("Action", "Thriller", "Crime", "Drama"),
    "Length": "153 minutes",
    "Rating": "12A"
}

for key, value in film.items():
    print(f"{key} : {value}")

print(type(film.items()))