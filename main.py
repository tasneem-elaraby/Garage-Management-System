import json
from tkinter import *

# base class
class Car:
    def __init__(self, car_number, full_name, age, team, speed, capacity):
        self.__car_number = car_number
        self.__full_name = full_name
        self.__age = age
        self.__team = team
        self.__speed = speed
        self.__capacity = capacity
    # getters&setters
    def get_car_number(self):
        return self.__car_number

    def get_full_name(self):
        return self.__full_name
    def set_full_name(self, name):
      self.__full_name = name
    def get_age(self):
        return self.__age
    def set_age(self, age):
         if age > 0:
              self.__age = age

    def get_team(self):
        return self.__team
    def set_team(self, team):
      self.__team = team

    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
         if speed > 0:
          self.__speed = speed

    def get_capacity(self):
        return self.__capacity
    def set_capacity(self, capacity):
        if capacity > 0:
            self.__capacity = capacity
# derived class
class Racer(Car):
    def __init__(self, car_number, full_name, age, team, speed, capacity, races, laps):
        super().__init__(car_number, full_name, age, team, speed, capacity) #inialize base class attributes
        self.__races = races
        self.__laps = laps
    # getters we setters
    def get_races(self):
        return self.__races
    def set_races(self, races):
      if races >= 0:
         self.__races = races

    def get_laps(self):
        return self.__laps
    def set_laps(self, laps):
        if laps >= 0:
            self.__laps = laps

    def get_type(self):
        return "Racer"

    def calculate_score(self):
        return (self.get_speed() * 10) + (self.get_capacity() * 1)

    def display_info(self):    # store both car number& name to display in GUI
        info = self.get_car_number() + " - " + self.get_full_name() + " - Racer"
        return info


# derived class
class SupportVehicle(Car):
    def __init__(self, car_number, full_name, age, team, speed, capacity, crew_size, reliability):
        super().__init__(car_number, full_name, age, team, speed, capacity)
        self.__crew_size = crew_size
        self.__reliability = reliability

    # getters and setters
    def get_crew_size(self):
        return self.__crew_size
    def set_crew_size(self, crew_size):
     if crew_size > 0:
           self.__crew_size = crew_size
    def get_reliability(self):
        return self.__reliability
    def set_reliability(self, reliability):
        if reliability > 0:
            self.__reliability = reliability
    def get_type(self):
        return "Support"

    def calculate_score(self):
        return (self.get_speed() * 5) + (self.get_capacity() * 5)

    def display_info(self):
        info = self.get_car_number() + " - " + self.get_full_name() + " - Support"
        return info

garage = []  #for storing car objets
def save():
    cars_data = [] #storing for json file
    for car in garage:
        car_data = {
            "car_number": car.get_car_number(),
            "full_name": car.get_full_name(),
            "age": car.get_age(),
            "team": car.get_team(),
            "speed": car.get_speed(),
            "capacity": car.get_capacity()
        }
        if car.get_type() == "Racer":
            car_data["type"] = "Racer"
            car_data["races"] = car.get_races()
            car_data["laps"] = car.get_laps()
        else:
            car_data["type"] = "Support"
            car_data["crew"] = car.get_crew_size()
            car_data["reliability"] = car.get_reliability()

        cars_data.append(car_data)
    with open("cars.json", "w") as file:
        json.dump(cars_data, file)


def load():
    with open("cars.json", "r") as file:
        cars_data = json.load(file)

    for saved_car in cars_data:
        if saved_car["type"] == "Racer":
            car = Racer(saved_car["car_number"], saved_car["full_name"], saved_car["age"], saved_car["team"], saved_car["speed"],
                saved_car["capacity"],
                saved_car["races"],
                saved_car["laps"]
            )
        else:
            car = SupportVehicle(
                saved_car["car_number"],
                saved_car["full_name"],
                saved_car["age"],
                saved_car["team"],
                saved_car["speed"],
                saved_car["capacity"],
                saved_car["crew"],
                saved_car["reliability"]
            )
        garage.append(car)
