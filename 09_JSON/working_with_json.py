import json

# with open("demo.json") as json_file:
#     read_file = json_file.read()
#     print(read_file, type(read_file))
#     demo = json.loads(read_file)
#     print(demo)

# Create python dictionary
# with information about
# favourite film/tv series/whatever

film = {
    "Title": "The Dark Knight",
    "Release Year": 2008,
    "Director": {
        "First Name": "Christopher",
        "Last name": "Nolan"
    },
    "Actors": ("Christian Bale", "Heath Ledger", "Morgan Freeman"),
    "Genre": ["Action", "Thriller", "Crime", "Drama"],
    "Length": 153.50,
    "None": None
}

# film_json_string = json.dumps(film) # converts to string
#
# with open("TheDarkKnight.json", "w") as dark_knight_file:
#     dark_knight_file.write(film_json_string)
#
# with open("TheDarkKnight2.json", "w") as dark_knight_file:
#     json.dump(film, dark_knight_file) # does the same as above but in one line

