# from os import system
# import time

car_dict = {
    "Aston Martin DB9": {
        "make": "Aston",
        "model": "DB9",
        "top_speed": 300,
        "acceleration": 9,
        "pic": "Race/pics/red5",
        "colour": "purple",
        "power": 999,
        "price": 90000,
    },
    "Audi TT 3.2 quattro": {
        "make": "Audi",
        "model": "3.2 quattro",
        "top_speed": 240,
        "acceleration": 7,
        "pic": "Race/pics/red3",
        "colour": "red",
        "power": 470,
        "price": 20000,
    },
    "Ford Mustang GT": {
        "make": "Ford",
        "model": "GT",
        "top_speed": 290,
        "acceleration": 9,
        "pic": "Race/pics/blue1",
        "colour": "blue",
        "power": 888,
        "price": 30000,
    },
    "Lexus IS300": {
        "make": "Lexus",
        "model": "IS300",
        "top_speed": 310,
        "acceleration": 9,
        "pic": "Race/pics/white1",
        "colour": "white",
        "power": 810,
        "price": 50000,
    },
    "Lamborgini Gallardo": {
        "make": "Lamborgini",
        "model": "Gallardo",
        "top_speed": 300,
        "acceleration": 9,
        "pic": "Race/pics/yellow2",
        "colour": "yellow",
        "power": 890,
        "price": 70000,
    },
    "Audi A4": {
        "make": "Audi",
        "model": "A4",
        "top_speed": 210,
        "acceleration": 8,
        "pic": "Race/pics/black4",
        "colour": "black",
        "power": 720,
        "price": 25000,
    },
    "BMW 3 Series": {
        "make": "BMW",
        "model": "3 Series",
        "top_speed": 250,
        "acceleration": 7,
        "pic": "Race/pics/green",
        "colour": "green",
        "power": 780,
        "price": 50000,
    },
    "Mercedes-Benz CLK500": {
        "make": "Mercedes-Benz",
        "model": "CLK500",
        "top_speed": 280,
        "acceleration": 9,
        "pic": "Race/pics/white2",
        "colour": "cyan",
        "power": 800,
        "price": 25000,
    },
    "Lexus ES": {
        "make": "Lexus",
        "model": "ES",
        "top_speed": 210,
        "acceleration": 7,
        "pic": "Race/pics/white3",
        "colour": "cyan",
        "power": 730,
        "price": 40000,
    },
    "Mazda RX-7": {
        "make": "Mazda",
        "model": "RX-7",
        "top_speed": 210,
        "acceleration": 7,
        "pic": "Race/pics/red4",
        "colour": "red",
        "power": 740,
        "price": 45000,
    },
    "Pontiac GTO": {
        "make": "Pontiac",
        "model": "GTO",
        "top_speed": 210,
        "acceleration": 7,
        "pic": "Race/pics/car1",
        "colour": "blue",
        "power": 660,
        "price": 50000,
    },
    "Mazda 6": {
        "make": "Mazda",
        "model": "6",
        "top_speed": 260,
        "acceleration": 8,
        "pic": "Race/pics/red6",
        "colour": "white",
        "power": 800,
        "price": 35000,
    },
    "Toyota Supra": {
        "make": "Toyota",
        "model": "Supra",
        "top_speed": 200,
        "acceleration": 6,
        "pic": "Race/pics/yellow3",
        "colour": "yellow",
        "power": 600,
        "price": 20000,
    },
    "BMW M3 GTR": {
        "make": "BMW",
        "model": "M3 GTR",
        "top_speed": 230,
        "acceleration": 7,
        "pic": "Race/pics/black2",
        "colour": "black",
        "power": 730,
        "price": 40000,
    },
    "Chevrolet Corvette": {
        "make": "Chevrolet",
        "model": "Corvette",
        "top_speed": 270,
        "acceleration": 7,
        "pic": "Race/pics/black3",
        "colour": "black",
        "power": 800,
        "price": 40000,
    },
    "Lotus Elise": {
        "make": "Lotus",
        "model": "Elise",
        "top_speed": 300,
        "acceleration": 7,
        "pic": "Race/pics/red5",
        "colour": "purple",
        "power": 999,
        "price": 34000,
    },
}


class CarShop:
    def __init__(self):
        self.garage = {
            "Lotus Elise": {
                "make": "Lotus",
                "model": "Elise",
                "top_speed": 300,
                "acceleration": 7,
                "colour": "purple",
                "power": 999,
                "price": 34000,
            }
        }
        self.color_code = {
            "black": "\033[0;30m",
            "red": "\033[0;31m",
            "green": "\033[0;32m",
            "yellow": "\033[0;33m",
            "blue": "\033[0;34m",
            "purple": "\033[0;35m",
            "cyan": "\033[0;36m",
            "white": "\033[0;37m",
        }

    def print_with_color(self, color, text):
        print(self.color_code[color] + text + "\033[0m")

    def car_buy(self, car_name, shop_money: int) -> None:
        car = car_dict.get(car_name)
        if car_name in car_dict.keys():
            if shop_money >= car["price"]:
                self.garage[car_name] = car
                shop_money -= car["price"]
                car_color = car["colour"].lower()
                self.print_with_color(car_color, f"{car_name} is purchased!")
                self.print_with_color(car_color, f"Remaining shop money: ${shop_money}")
                return car["price"]
            else:
                self.print_with_color(
                    "red", "Sorry, you don't have enough money to buy this car!"
                )
                return 0
        # else:
        #     self.print_with_color("red", "You already have this car in your garage!")
        #     return 0
        else:
            self.print_with_color(
                "red", "Sorry, this car is not available in our shop!"
            )
            return 0

    def car_sell(self, car_name) -> None:
        if car_name == "Lotus Elise":
            print("You can't sell your first car!")
            return 0
        if car_name in self.garage:
            car = self.garage[car_name]
            # if sell_price >= car["price"]:
            del self.garage[car_name]
            self.print_with_color(
                car["colour"].lower(), f"{car_name} is sold for $" + str(car["price"])
            )
            return car["price"]
        else:
            self.print_with_color(
                "red", "Sorry, you don't have this car in your garage!"
            )
            return 0

    def show_all_cars(self) -> None:
        print("Cars available in our shop:")
        for index, car in enumerate(car_dict, start=1):
            car_color = car_dict[car]["colour"].lower()
            self.print_with_color(
                car_color, f"[{index}]  -  {car} - ${car_dict[car]['price']}"
            )

    def garage_list(self) -> None:
        if len(self.garage) == 0:
            self.print_with_color("red", "Your garage is empty!")
        else:
            print("Cars in your garage:")
            for index, car in enumerate(self.garage, start=1):
                car_color = self.garage[car]["colour"].lower()
                self.print_with_color(
                    car_color,
                    f"[{index}] {car} - {self.garage[car]['model']} - ${self.garage[car]['price']}",
                )


# car_shop = CarShop()

# car_shop.show_all_cars()
# car_shop.garage_list()

# car_shop.car_buy("Audi TT", "3.2 quattro", 50000)
# car_shop.car_buy("Lamborgini Gallardo", "Gallardo", 80000)
# car_shop.car_buy("Lexus ES", "ES", 80000)
# car_shop.car_buy("BMW M3 GTR", "M3 GTR", 80000)
# car_shop.car_sell("Audi TT")

# car_shop.garage_list()
# CarShop().show_all_cars()
