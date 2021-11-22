class Animal:
    def __init__(self, legs):
        self.alive = True
        self.legs = legs

    def breath(self):
        print("Breathing")

    def eat(self):
        print("Easting")




class Mammal(Animal):
    def __init__(self,legs):
        super().__init__(legs)
        self.warm_blooded = True

    def reproduce(self):
        print("Reproducing")

class Platypus(Mammal):
    def __init__(self):
        super().__init__(4)

    def reproduce(self):
        print("Laying eggs")
