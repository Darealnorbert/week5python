'''Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.
Activity 2: Polymorphism Challenge! 🎭
Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).'''


class Smartphone:
    def __init__(self, brand, model, os):
        self.brand = brand
        self.model = model
        self.os = os

    def make_call(self, number):
        return f"Calling {number} from {self.model}"

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

    def install_app(self, app_name):
        return f"Installing {app_name} on {self.model}"


smartphone1 = Smartphone("Apple", "iPhone 13", "iOS")
print(smartphone1.make_call("123-456-7890"))

smartphone2 = Smartphone("Samsung", "Galaxy S21", "Android")
print(smartphone2.send_message("987-654-3210", "Hello!"))


class Vehicles:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        pass


class Car(Vehicles):
    def move(self):
        return f"{self.brand} {self.model} is Driving 🚗 "


class Plane(Vehicles):
    def move(self):
        return f"{self.brand} {self.model} is Flying ✈️"
