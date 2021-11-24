import json


class Film:
    def __init__(self, file_path: str):
        self.filepath = file_path
        film_info = self._open_json_file()
        self.title = film_info.get("Title")
        self.year = film_info.get("Release Year")
        self.director = film_info.get("Director")
        self.actor = film_info["Actors"]
        self.genre = film_info["Genre"]
        self.length = film_info["Length"]
        self.ratings = film_info["Ratings"]

    def _open_json_file(self) -> dict:
        with open(self.filepath) as film_file:
            return json.load(film_file)

    def get_average_rating(self) -> float:
        total = 0
        for values in self.ratings.values():
            total += values
        return total/len(self.ratings)


film = Film("TheDarkKnight.json")


print(film.get_average_rating())