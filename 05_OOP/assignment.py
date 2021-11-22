# Q1a: Create a class which of a country (include continent,
# climate, language etc in the inputs)
# A1a:

class Country:
    def __init__(self, country, climate, languages: []):
        self._country = country
        self._climate = climate
        self._languages = languages

# Q1b: Create a subclass of a city which inherits from the country class
# A1b:

class City(Country):
    def __init__(self, name, country, climate, languages):
        super().__init__(country, climate, languages)
        self.name = name

# Q2a: Using the predefined class and is_prime method below, loop through list_of_numbers
# and create a list of primes from that list
list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]

class Number:
    def __init__(self, integer):
        self.integer = integer
    def is_prime(self):
        if self.integer >= 2:
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    return False
                else:
                    return True
        else:
            return False

    def divisible_by_n(self, n):
        if self.integer % n == 0:
            return True
        else:
            return False


primes = []


for i in list_of_numbers:
    n = Number(i)
    if n.is_prime() == True:
        primes.append(i)

print(primes)


# Q3a:
# Fix the following class and subclass

class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face


class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name,attitude,behaviour,face)

   def encourage(self):
       print(f"The team cheers for {self.name}, "
             f"starts shouting awesome slogans then gets back to work.")







