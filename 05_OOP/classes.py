class Dog:
    animal_kind = "elephant"

    def __init__(self, name, colour):
        self.legs = 4
        self.name = name
        self.colour = colour
        self.animal_kind = "canine"

    def bark(self):
        return f"Woof! I am a {self.animal_kind}"


fido = Dog("fido","brown")

Dog.animal_kind = "spider"
print(fido.animal_kind)
