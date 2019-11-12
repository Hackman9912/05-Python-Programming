"""

2. Car Class
    Write a class named Car that has the following data attributes:
        • __year_model (for the car’s year model)
        • __make (for the make of the car)
        • __speed (for the car’s current speed)
        The Car class should have an __init__ method that accept the car’s year model and make
        as arguments. These values should be assigned to the object’s __year_model and __make
        data attributes. It should also assign 0 to the __speed data attribute.
        The class should also have the following methods:
        • accelerate
        The accelerate method should add 5 to the speed data attribute each time it is
        called.
        • brake
        The brake method should subtract 5 from the speed data attribute each time it is called.
        • get_speed
        The get_speed method should return the current speed.
    Next, design a program that creates a Car object, and then calls the accelerate method
    five times. After each call to the accelerate method, get the current speed of the car and
    display it. Then call the brake method five times. After each call to the brake method, get
    the current speed of the car and display it.

"""

class Cars:

    def __init__(self, year, make, model, speed):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = speed

    def set_year(self, year):
        self.__year = year
    def set_make(self, make):
        self.__make = make
    def set_model(self, model):
        self.__model = model
    def accelerate(self, speed):
        for i in range(5):
            self.__speed += 5
            print(speed)
    def brake(self, speed):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

    def get_year(self):
        return self.__year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model
