import json
import os
from datetime import date, datetime

from constants import *


class Pizza:
    """Class that describes pizza (contains price and ingredients)"""

    def __init__(self):
        self.__price = BASIC_PIZZA_PRICE
        self.__ingredients = []

    def tomato_sauce(self):
        self.__ingredients.append("Tomato sauce")
        self.__price += TOMATO_SAUCE_PRICE

    def mozzarella(self):
        self.__ingredients.append("Mozzarella")
        self.__price += MOZZARELLA_PRICE

    def anchovies(self):
        self.__ingredients.append("Anchovies")
        self.__price += ANCHOVIES_PRICE

    def vienna_sausages(self):
        self.__ingredients.append("Vienna sausages")
        self.__price += VIENNA_SAUSAGES_PRICE

    def ham(self):
        self.__ingredients.append("Ham")
        self.__price += HAM_PRICE

    def mushrooms(self):
        self.__ingredients.append("Mushrooms")
        self.__price += MUSHROOMS_PRICE

    def artichokes(self):
        self.__ingredients.append("Artichokes")
        self.__price += ARTICHOKES_PRICE

    def olives(self):
        self.__ingredients.append("Olives")
        self.__price += OLIVES_PRICE

    def fontina(self):
        self.__ingredients.append("Fontina")
        self.__price += FONTINA_PRICE

    def gorgonzola(self):
        self.__ingredients.append("Gorgonzola")
        self.__price += GORGONZOLA_PRICE

    def parmigiano(self):
        self.__ingredients.append("Parmigiano")
        self.__price += PARMIGIANO_PRICE

    def capers(self):
        self.__ingredients.append("Capers")
        self.__price += CAPERS_PRICE

    def speck(self):
        self.__ingredients.append("Speck")
        self.__price += SPECK_PRICE

    __add_ingredients = {"Tomato sauce": tomato_sauce, "Mozzarella": mozzarella, "Anchovies": anchovies,
                         "Vienna sausages": vienna_sausages, "Ham": ham, "Mushrooms": mushrooms,
                         "Artichokes": artichokes, "Olives": olives, "Fontina": fontina, "Gorgonzola": gorgonzola,
                         "Parmigiano": parmigiano, "Capers": capers, "Speck": speck}

    def add_ingredients(self, *components):
        """Method to add additional ingredient(s) to pizza"""

        for component in components:
            if not isinstance(component, str):
                raise TypeError
            if not component:
                raise ValueError("Ingredient not specified")
            if component not in self.__add_ingredients:
                raise ValueError(f"No such ingredient. Available: {self.__add_ingredients.values()}")
            self.__add_ingredients[component]()

    @property
    def price(self):
        return self.__price

    @property
    def ingredients(self):
        return self.__ingredients

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError
        if price < 0:
            raise ValueError("Price cannot be less than 0")
        self.__price = price

    def ser_ingredients(self):
        """Method to write information about all possible ingredients to json file"""

        data = []
        i = 0
        for ingredient in self.__add_ingredients:
            i += 1
            data.append({i: ingredient})
        with open("ingredients.JSON", "w") as json_file:
            json.dump(data, json_file, indent=4)

    def __str__(self):
        return self.__class__.__name__


class Romana(Pizza):
    """Class that describes Romana pizza (basic ingredients: tomato sauce, mozzarella, anchovies)"""

    def __init__(self):
        super().__init__()
        super().tomato_sauce()
        super().mozzarella()
        super().anchovies()


class Viennese(Pizza):
    """Class that describes Viennese pizza (basic ingredients: tomato sauce, mozzarella, vienna sausages)"""

    def __init__(self):
        super().__init__()
        super().tomato_sauce()
        super().mozzarella()
        super().vienna_sausages()


class Capricciosa(Pizza):
    """Class that describes Capricciosa pizza (basic ingredients: tomato sauce, mozzarella, ham, mushrooms, artichokes,
    olives)"""

    def __init__(self):
        super().__init__()
        super().tomato_sauce()
        super().mozzarella()
        super().ham()
        super().mushrooms()
        super().artichokes()
        super().olives()


class QuattroFormaggi(Pizza):
    """Class that describes Quattro Formaggi pizza (basic ingredients: tomato sauce, mozzarella, fontina, gorgonzola,
    parmigiano)"""

    def __init__(self):
        super().__init__()
        super().tomato_sauce()
        super().mozzarella()
        super().fontina()
        super().gorgonzola()
        super().parmigiano()


class Siciliana(Pizza):
    """Class that describes Siciliana pizza (basic ingredients: tomato sauce, mozzarella, capers, anchovies,
    anchovies)"""

    def __init__(self):
        super().__init__()
        super().tomato_sauce()
        super().mozzarella()
        super().capers()
        super().anchovies()
        super().anchovies()


class Tirolese(Pizza):
    """Class that describes Tirolese pizza (basic ingredients: tomato sauce, mozzarella, speck)"""

    def __init__(self):
        super().__init__()
        super().tomato_sauce()
        super().mozzarella()
        super().speck()


class Prosciutto(Pizza):
    """Class that describes Prosciutto pizza (basic ingredients: tomato sauce, mozzarella, ham, mushrooms)"""

    def __init__(self):
        super().__init__()
        super().tomato_sauce()
        super().mozzarella()
        super().ham()
        super().mushrooms()


class Customer:
    """Class that describes a customer (contains name and phone number)"""

    def __init__(self, name, phone):
        if not isinstance(phone, str):
            raise TypeError
        if not phone:
            raise ValueError("No phone number")
        self.__name = name
        self.__phone = phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError("No data")
        self.__name = name


class Order:
    """Class that describes pizza order (contains number of pizza in order, total price, order data)"""

    __number = 0
    __total = 0
    __data = []
    pizza_week = {"Monday": Romana(), "Tuesday": Viennese(), "Wednesday": Capricciosa(), "Thursday": QuattroFormaggi(),
                  "Friday": Siciliana(), "Saturday": Tirolese(), "Sunday": Prosciutto()}

    def __init__(self, customer, order_day):
        __number = 0
        if not isinstance(customer, Customer):
            raise TypeError
        self.__day = order_day.strftime('%A')
        self.__date = date
        self.__customer = customer

    def pizza_of_the_day(self):
        """Method to add pizza of the day to order"""

        pizza = self.pizza_week[self.__day]
        self.__number += 1
        self.__data.append({self.__number: self.__day + " " + str(pizza) + " " + str(pizza.ingredients) + " : " + str(pizza.price) + "$"})
        self.__total += pizza.price

    def add_pizza(self, pizza):
        """Method to add pizza to order"""

        if not isinstance(pizza, Pizza):
            raise TypeError
        self.__number += 1
        self.__data.append({self.__number: str(pizza) + " " + str(pizza.ingredients) + " : " + str(pizza.price) + "$"})
        self.__total += pizza.price

    def ser_week(self):
        """Method to write information about pizza of the day for week to json file"""

        data = []
        for key in self.pizza_week.keys():
            data.append({key: str(self.pizza_week[key])})
        with open("pizza_of_the_day.JSON", "w") as json_file:
            json.dump(data, json_file, indent=4)

    def serialization(self, filepath):
        """Method to write order information to json file"""
        
        if not os.path.exists(filepath):
            raise OSError("File was not found")
        self.__data.append({"total": self.__total})
        with open(filepath, "w") as json_file:
            json.dump(self.__data, json_file, indent=4)

    @staticmethod
    def deserialization(filepath):
        """Method to extract order information from json file"""

        if not os.path.exists(filepath):
            raise OSError("File was not found")
        if os.path.getsize(filepath):
            pass
        else:
            raise OSError("File is empty")
        with open(filepath, "r") as json_file:
            return json.load(json_file)


customer1 = Customer("Kaeya", "+3456778997")
order1 = Order(customer1, datetime.today())
order1.pizza_of_the_day()
order1.add_pizza(Romana())
order1.serialization("order.JSON")
order1.ser_week()
Romana().ser_ingredients()
