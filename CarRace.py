import random
import time
from CarShop import car_dict
from CarShop import CarShop
import sys
import race
import threading


maps = {
    "Florida": {"length": 20.55, "difficulty": "easy"},
    "Nürnburgring": {"length": 20.88, "difficulty": "medium"},
    "Monaco": {"lenght": 31.63, "difficulty": "hard"},
}


class CarRace:
    def __init__(self):
        self = self
        self.car_dict1 = list(car_dict)
        self.difficulty = []
        self.easy = []
        self.medium = []
        self.hard = []
        self.my_car = []
        self.my_car_speed = 100
        self.enemy_car_speed = 120
        self.win = []

    def __str__(self):
        return f"Available Cars {list(CarShop.garage_list)}"

    def choose_car(self):
        return CarShop.garage_list

    def Start_Game(self):
        for key in maps:
            self.difficulty.append(maps[key]["difficulty"])
        print(
            f"""Choose your game:\n*************{list(maps)}*****************
        \n******************{self.difficulty}*******************\n
        ************ 1         2        3 **************"""
        )

        choice = input("")
        if choice == "1":
            print(f'Lets drive in Florida{maps["Florida"]}')
            print()
            self.easy.append(random.choice(self.car_dict1))
            print(f"Your enemie will be {self.easy}")

        elif choice == "2":
            print(f'Lets drive in Nürnburgring{maps["Nürnburgring"]}')
            print()
            for i in range(2):
                self.medium.append(random.choice(self.car_dict1))
            print(f"Your enemies will be{self.medium}")

        elif choice == "3":
            print(f'Lets drive in Monaco{maps["Monaco"]}')
            print()
            for i in range(3):
                self.hard.append(random.choices(self.car_dict1))
            print(f"Your enemies will be {self.hard}")
        else:
            print("Wrong input my friend")
        print()

    def go(self):
        for i in range(1, 4):
            time.sleep(1)
            print(i)
            if i == 3:
                time.sleep(1)
                print("GO!")

    def exp(self):
        race_game = race.Game()
        result = race_game.run()

        if result == 1:
            print("You earned 1000 xp and 10000$")
            return 1
        elif result == 0:
            print("You earned 100 xp and 1000$")
            return 0

    def faster(self):
        if self.my_car_speed < self.enemy_car_speed:
            print("Oh NO! Your enemy is far ahead you need to accelerate...")
            time.sleep(0.5)
            choice = input("PRESS 2 TO SPEED UP OR 1 TO SPEED DOWN: ")
            if choice == "2":
                self.my_car_speed = self.my_car_speed * 1.2
                time.sleep(0.5)
                print(f"You increased your speed.New Speed: {self.my_car_speed} kmh")
                print(f"current enemy speed: {self.enemy_car_speed} kmh")
                time.sleep(1)
                if self.enemy_car_speed >= self.my_car_speed:
                    choice = input(
                        "Enemy is still faster. Press '2' to speed up or '1' to speed down"
                    )
                    if choice == "2":
                        self.my_car_speed = self.my_car_speed * 1.2
                        time.sleep(1)
                        print(
                            f"Well done! Current speed: {self.my_car_speed} kmh. Current enemy speed: {self.enemy_car_speed} kmh"
                        )
                        print("Now you are really fast,but a curve is coming")
                        time.sleep(0.5)
                        choice = input(
                            "Press '1' to slow down or '2' to speed even more up: "
                        )
                        if choice == "1":
                            self.my_car_speed = self.my_car_speed * 0.8
                            time.sleep(0.5)
                            print(
                                f"Well done! New Speed: {self.my_car_speed} You slowed down and passed the curve without accidents"
                            )
                            time.sleep(0.5)
                            print("Your enemy didn't slow down")
                            time.sleep(1.5)
                            self.win.append(1)
                            print("WIN")

            elif choice == "1":
                self.my_car_speed = self.my_car_speed * 0.8
                time.sleep(0.5)
                print(
                    f"You are way to slow. Your enemy already reached the finishing line\n GAME OVER"
                )

                time.sleep(0.5)


# my_game = CarRace()

# my_game.Start_Game()
# my_game.choose_car()
# my_game.go()
# my_game.faster()
# my_game.exp()
