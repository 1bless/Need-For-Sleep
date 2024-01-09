from CarShop import CarShop, car_dict
import random
from art import *
from termcolor2 import c

# import time


class Car:
    def __init__(self, car_name):
        car = car_dict[car_name]
        self.brand = car["make"]
        self.model = car["model"]
        self.price = car["price"]
        self.top_speed = car["top_speed"]
        self.acceleration = car["acceleration"]
        self.handling = random.randrange(1, 10)
        self.color = car["colour"]
        self.horse_power = car["power"]
        self.speed = 0

    def get_info(self):
        print(c(f"{self.brand} {self.model}".center(50, "=")).blue.on_yellow)
        print("Stats:")
        print(f"\tPower:        {int(self.horse_power)}hp")
        print(f"\tTop speed:    {int(self.top_speed)} km/h")
        print(f"\t0-100km/h:    {self.acceleration}s")
        print(f"\tHandling:     {int(self.handling)}")
        print(f"\tColor:        {self.color}")
        print(f"\tPrice:        {self.price}$")
        print(c("=" * 50).blue.on_yellow)

    def start(self):
        print(f"The car has been started and ready for race. Wrm-Wrm...")

    def speed_up(self, speed_delta):
        new_speed = self.speed + speed_delta
        if new_speed <= self.top_speed:
            self.speed = new_speed
            print(f"The car has accelerated to {self.speed} km/h.")
        else:
            self.speed = self.top_speed
            print(f"The car has reached its top speed of {self.top_speed} km/h.")

    def speed_down(self, speed_delta):
        new_speed = self.speed - speed_delta
        if new_speed >= 0:
            self.speed = new_speed
            print(f"The car has slowed down to {self.speed} km/h.")
        else:
            self.speed = 0
            print("The car has come to a complete stop.")

    def stop(self):
        self.speed = 0
        print("The car has come to a complete stop.")

    def tuning(self, upgrades):
        print(c(text2art("PIMP MY RIDE Studio is online now")).yellow.blink.dark)
        print(
            f"Hey hey hey, it's X to the Z Xzibit, and I'm ready to show you some love by pimping your ride! Let`s PIMP your Ride man!"
        )
        colors = [
            "Red",
            "Orange",
            "Yellow",
            "Green",
            "Blue",
            "Indigo",
            "Violet",
            "Coral",
        ]
        for upgrade in upgrades:
            if upgrade == "engine":
                self.horse_power *= 1.1
                self.acceleration *= 0.9
                self.top_speed *= 1.17
                print(c("Engine upgrade installed.").green)
            elif upgrade == "suspension":
                self.handling *= 1.2
                print(c("Suspension upgrade installed.").green)
            elif upgrade in colors:
                self.color = upgrade
                self.price *= 1.05
                print(c("Color upgrade installed.").green)
            else:
                print(f"Unknown upgrade: {upgrade}")


"""car = Car("BMW M3 GTR")
car.get_info()
car.start()
car.speed_up(50)
car.speed_down(10)
car.stop()
car.tuning(['engine', 'suspension', 'Yellow'])
car.get_info()"""
