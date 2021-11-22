class Dog:
    animal_kind = "elephant"

    def __init__(self, name, coat_colour):
        self.legs = 4
        self.name = name
        self.__colour = coat_colour
        self.animal_kind = "canine"

    def bark(self):
        return f"Woof! I am a {self.animal_kind}"

    def get_colour(self):
        return self.__colour

    def set_colour(self, new_colour):
        self.__colour = new_colour


fido = Dog("fido","brown")

Dog.animal_kind = "spider"
print(fido.animal_kind)

fido.__colour = "black"

print(fido.get_colour())