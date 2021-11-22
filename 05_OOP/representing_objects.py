class Location:
    def __init__(self, lat, long):
        self._latitude = lat
        self._longitude = long

    def __repr__(self):
        return f"Location(Latitude={self._latitude}, Longitude={self._longitude})"

    def __str__(self):
        return f"({self._latitude}, {self._longitude})"



bham_academy = Location(50, -1)

print(repr(bham_academy))

