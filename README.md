# Radiator Springs Garage Management System

## Project Description

Radiator Springs Garage Management System is a GUI application built with Python and Tkinter. It allows to manage different vehicles in the garage by adding,viewing,searching,updating and retiring cars.

The system has two types of vehicles: Racer and Support Vehicle. It also uses JSON to save the garage data so that the cars are still available when the program is opened again.

## Features

- Login to the garage system.
- Check in a new Racer.
- Check in a new Support Vehicle.
- Prevent duplicate car numbers.
- View all cars in the garage.
- Search for a car using its  number.
- Update the speed and capacity of a car.
- Retire a car from the garage 
- Generate a garage report.
- Calculate the average performance score.
- Save garage data to a JSON file.


## OOP Concepts 

- Encapsulation using private attributes , getters and setters.
- Inheritance 
- Polymorphism 


## Requirements

- Python 3.x
- Tkinter
- JSON

## How to Run

1. Download the project files.
2. Make sure `main.py` and `cars.json` are in the same folder.
3. Open a terminal in the project folder.
4. Run the program:

```bash
python main.py
```


- Number of cars in each team.

The performance score is calculated using the `calculate_score()` method. Racer and SupportVehicle have different implementations of this method.
