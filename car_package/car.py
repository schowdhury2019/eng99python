class Car:
    def __init__(self, max_speed, license_number = 0):
        self._max_speed = max_speed
        self._velocity = 0
        self._license_number = license_number
        self._number_of_passengers = 5

    def accelerate(self, speed):
        self._velocity += speed
        if self._velocity > self._max_speed:
            self._velocity = self._max_speed

    def get_top_speed(self):
        return self._max_speed

    def get_velocity(self):
        return self._velocity

    def decelerate(self, speed):
        self._velocity -= speed
        if self._velocity < 0:
            self._velocity = 0

    def brake(self):
        self._velocity = 0


mycar = Car(60)

mycar.accelerate(50)

print(mycar.get_velocity())

mycar.accelerate(50)

print(mycar.get_velocity())

mycar

