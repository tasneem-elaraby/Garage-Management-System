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

##gui part using Tkinter
# check in
def check_in():
    window = Toplevel(login_window)
    window.title("Check in")
    Label(window, text="Select Type").pack()
    Button(window, text="Racer", command=add_racer).pack()
    Button(window, text="Support Vehicle", command=add_support).pack()

# check in for racer
def add_racer():
    window = Toplevel(login_window)
    window.title("Add Racer")
    Label(window, text="Car Number").pack()
    number = Entry(window)
    number.pack()
    Label(window, text="Full Name").pack()
    name = Entry(window)
    name.pack()
    Label(window, text="Age").pack()
    age = Entry(window)
    age.pack()
    Label(window, text="Team").pack()
    team = Entry(window)
    team.pack()
    Label(window, text="Speed").pack()
    speed = Entry(window)
    speed.pack()
    Label(window, text="Capacity").pack()
    capacity = Entry(window)
    capacity.pack()
    Label(window, text="Races").pack()
    races = Entry(window)
    races.pack()
    Label(window, text="Laps").pack()
    laps = Entry(window)
    laps.pack()
    message = Label(window, text="")
    message.pack()

    def add():  #check if car no is repeated if not make an object
        for car in garage:
            if car.get_car_number() == number.get():
                message["text"] = "Car nmber exist"
                return
   #convert from string to int
        car = Racer(number.get(), name.get(), int(age.get()), team.get(),int(speed.get()), int(capacity.get()),int(races.get()), int(laps.get()))
        garage.append(car)
        save()
        message["text"] = "racer is added"
    Button(window, text="Add", command=add).pack()

#same for support vehicle
def add_support():
    window = Toplevel(login_window)
    window.title("Add Support Vehicle")
    Label(window, text="Car Number").pack()
    number = Entry(window)
    number.pack()
    Label(window, text="Full Name").pack()
    name =Entry(window)
    name.pack()
    Label(window, text="Age").pack()
    age =Entry(window)
    age.pack()
    Label(window, text="Team").pack()
    team = Entry(window)
    team.pack()
    Label(window, text="Speed").pack()
    speed =Entry(window)
    speed.pack()
    Label(window, text="Capacity").pack()
    capacity = Entry(window)
    capacity.pack()
    Label(window,text="Crew Size").pack()
    crew = Entry(window)
    crew.pack()
    Label(window, text="Reliability").pack()
    reliability = Entry(window)
    reliability.pack()
    message = Label(window, text="")
    message.pack()

    def add():
        for car in garage:
            if car.get_car_number() == number.get():
                message["text"] = "Car number exists"
                return
        car = SupportVehicle(number.get(), name.get(), int(age.get()), team.get(), int(speed.get()), int(capacity.get()),int(crew.get()), int(reliability.get()))
        garage.append(car)
        save()
        message["text"] = "Support Vehicle added"
    Button(window, text="Add", command=add).pack()
    
# view garage panel
def view_garage():
    window = Toplevel(login_window)
    window.title("view garage")
    cars_list = Listbox(window, width=40)
    cars_list.pack()
    for car in garage:
        cars_list.insert(END, car.display_info())

# search and tune up
def tune_up():
    window = Toplevel(login_window)
    window.title("Search & tune up")
    Label(window, text="Car number").pack()
    search = Entry(window)
    search.pack()
    results = Listbox(window, width=40)
    results.pack()
    Label(window, text="New Speed").pack()
    speed = Entry(window)
    speed.pack()
    Label(window, text="New Capacity").pack()
    capacity = Entry(window)
    capacity.pack()
    message = Label(window, text="")
    message.pack()

    def find():
        for car in garage:
            if car.get_car_number() == search.get():
                results.insert(END, car.display_info())
                return
        results.insert(END, "Car not found")

    def update():
        for car in garage:
            if car.get_car_number() == search.get():
                car.set_speed(int(speed.get()))
                car.set_capacity(int(capacity.get()))
                save()
                message["text"] = "Car updated"
                return

        message["text"] = "Car isnot found"

    Button(window, text="Search", command=find).pack()
    Button(window, text="Update", command=update).pack()

# retire
def retire():
    window = Toplevel(login_window)
    window.title("Retire")
    cars_list = Listbox(window, width=40)
    cars_list.pack()
    for car in garage:
        cars_list.insert(END, car.display_info())

    Label(window, text="Car Number").pack()
    number = Entry(window)
    number.pack()
    message = Label(window, text="")
    message.pack()

    def remove():
        for car in garage:
            if car.get_car_number() == number.get():
                garage.remove(car)
                save()
                message["text"] = "Car retired"
                return
        message["text"] = "Car not found"

    def confirmation():
        message["text"] = "Are you sure?"
        Button(window, text="Yes", command=remove).pack()
    Button(window, text="Retire", command=confirmation).pack()
# garage report
def report():
    window = Toplevel(login_window)
    window.title("Garage Report")
    total = len(garage)
    total_score = 0
    teams = {}
    for car in garage:
        total_score = total_score + car.calculate_score()
        team_name = car.get_team()
        # count how many cars are in each team
        if team_name in teams:
            teams[team_name] = teams[team_name] + 1
        else:
            teams[team_name] = 1

    total_info = "total Cars: " + str(total)
    Label(window, text=total_info).pack()
    if total > 0:
        average = total_score / total
        average_info = "Average Score: " + str(average)
        Label(window, text=average_info).pack()
    Label(window, text="Cars Per Team").pack()
    for team_name in teams:
        number_of_cars = teams[team_name]
        team_info = team_name + ": " + str(number_of_cars)
        Label(window, text=team_info).pack()
def login():
    if username.get() == "Sheriff" and password.get() == "239TasTas":
        home()
    else:
        message["text"] = "incorrect username /password"

# home
def home():
    window = Toplevel(login_window)
    window.title("Radiator Springs Garage")
    Label(window,text="Welcome Sheriff").pack()
    Button(window,text="Check in",command=check_in).pack()
    Button(window,text="View garage",command=view_garage).pack()
    Button(window,text="Search & tune up",command=tune_up).pack()
    Button(window,text="retire",command=retire).pack()
    Button(window,text="Garage report",command=report).pack()
    Button(window,text="exit", command=window.destroy).pack()
load()
# log in Screen
login_window = Tk()
login_window.title("Login")
Label(login_window, text="Login").pack()
Label(login_window, text="Username").pack()
username = Entry(login_window)
username.pack()
Label(login_window, text="password").pack()
password = Entry(login_window)
password.pack()
message = Label(login_window, text="")
message.pack()
Button(login_window, text="Login", command=login).pack()
login_window.mainloop()       