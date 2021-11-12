import json
import os
from datetime import date


class Customer:
    """Class that describes a customer (contains surname, name, student identifier)"""

    def __init__(self, surname, name, student_ind=False):
        if not isinstance(student_ind, bool):
            raise TypeError
        self.__surname = surname
        self.__name = name
        self.__student_ind = student_ind

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def student_ind(self):
        return self.__student_ind

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError
        if not surname:
            raise ValueError("No data")
        self.__surname = surname

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError("No data")
        self.__name = name


class Event:
    """Class that describes an event.
    Contains ticket current number of tickets, maximal number of tickets, basic price of a ticket, name, date"""

    _ticket_number = 0
    __tickets_max = 0
    __basic_price = 0
    __tickets_data = []

    def __init__(self, name, date, tickets_max=50, basic_price=0):
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError("No data")
        Event.__tickets_max = tickets_max
        Event.__basic_price = basic_price
        self.__date = date
        Event.__tickets_data.append({"Name": name})
        Event.__tickets_data.append({"Regular price": Event.__basic_price})

    def ticket(self, customer, date):
        """Method to generate a ticket"""
        if Event._ticket_number >= Event.__tickets_max:
            raise ValueError("All tickets are sold")
        info = []
        if (self.__date - date).days <= 356:
            if customer.student_ind:
                ticket = Student(customer)
                info.append({"Type": "Student"})
            else:
                if (self.__date - date).days >= 60:
                    ticket = Advance(customer)
                    info.append({"Type": "Advance"})
                elif (self.__date - date).days <= 10:
                    ticket = Late(customer)
                    info.append({"Type": "Late"})
                else:
                    ticket = Regular(customer)
                    info.append({"Type": "Regular"})
        else:
            raise ValueError("Invalid date")
        info.append({"Surname": ticket.customer.surname})
        info.append({"Name": ticket.customer.name})
        info.append({"Price": ticket.price})
        Event.__tickets_data.append({ticket.id: info})

    @staticmethod
    def serialization(filepath):
        """Method to write ticket information to json file"""
        if not os.path.exists(filepath):
            raise OSError("File was not found")
        if os.path.getsize(filepath):
            pass
        else:
            raise OSError("File is empty")
        with open(filepath, "w") as json_file:
            json.dump(Event.__tickets_data, json_file, indent=4)

    @staticmethod
    def deserialization(filepath):
        """Method to extract information from json file"""
        if not os.path.exists(filepath):
            raise OSError("File was not found")
        if os.path.getsize(filepath):
            pass
        else:
            raise OSError("File is empty")
        with open(filepath, "r") as json_file:
            return json.load(json_file)

    def find_id(self, ticket_id):
        """Method to find a ticket by its number and return as string"""
        if not isinstance(ticket_id, int):
            raise TypeError
        if ticket_id <= 0:
            raise ValueError("Ticket ID must be above zero")
        if ticket_id > Event._ticket_number:
            return f'There\'s no such ID'
        for record in self.__tickets_data:
            for key in record.keys():
                if key == ticket_id:
                    return record[key]

    @staticmethod
    def find_ticket(key, filepath):
        """Method to extract ticket by a number from json file"""
        if not os.path.exists(filepath):
            raise OSError("File was not found")
        if os.path.getsize(filepath):
            pass
        else:
            raise OSError("File is empty")
        if not isinstance(key, str):
            raise TypeError
        if not key:
            raise ValueError("No data")
        with open(filepath, "r") as json_file:
            data = json.load(json_file)
            for dict in data:
                for i in dict.keys():
                    if i == key:
                        return dict

    @staticmethod
    def return_str(key, filepath):
        """Method that returns info about a ticket picked by a number as string from json file"""
        data = Event.find_ticket(key, filepath)
        return f'{data[key][0]["Type"]} {data[key][1]["Surname"]} {data[key][2]["Name"]} {data[key][3]["Price"]}'

    def price(self, key, filepath):
        """Method that returns price of a ticked picked by a number from json file"""
        data = Event.find_ticket(key, filepath)
        for dict in data[key]:
            for i in dict.keys():
                if i == "Price":
                    return dict[i]

    @property
    def tickets_max(self):
        return Event.__tickets_max

    @property
    def basic_price(self):
        return Event.__basic_price

    @tickets_max.setter
    def tickets_max(self, tickets_max):
        if not isinstance(tickets_max, int):
            raise TypeError
        if tickets_max < 5:
            raise ValueError("The maximum number of tickets cannot be less than 5")
        Event.__ticket_max = tickets_max

    @basic_price.setter
    def basic_price(self, basic_price):
        if not isinstance(basic_price, (int, float)):
            raise TypeError
        if basic_price < 0:
            raise ValueError("Price cannot be less than 0")
        Event.__basic_price = basic_price


class Regular(Event):
    """Class that builds regular ticket.
    Contains ticket's price (the same as basic price for event), number and information about a customer"""

    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError
        self.__price = self.basic_price
        Event._ticket_number += 1
        self.__id = Event._ticket_number
        self.__customer = customer

    @property
    def price(self):
        return self.__price

    @property
    def id(self):
        return self.__id

    @property
    def customer(self):
        return self.__customer

class Advance(Event):
    """Class that builds advanced ticket.
    Contains ticket's price (sale 40% of basic price for event), number and information about a customer"""

    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError
        self.__price = 0.6 * self.basic_price
        Event._ticket_number += 1
        self.__id = Event._ticket_number
        self.__customer = customer

    @property
    def price(self):
        return self.__price

    @property
    def id(self):
        return self.__id

    @property
    def customer(self):
        return self.__customer


class Student(Event):
    """Class that builds student ticket.
    Contains ticket's price (sale 50% of basic price for event), number and information about a customer"""

    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError
        self.__price = 0.5 * self.basic_price
        Event._ticket_number += 1
        self.__id = Event._ticket_number
        self.__customer = customer

    @property
    def price(self):
        return self.__price

    @property
    def id(self):
        return self.__id

    @property
    def customer(self):
        return self.__customer


class Late(Event):
    """Class that builds late ticket.
    Contains ticket's price (additional 10% of basic price for event), number and information about a customer"""

    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError
        self.__price = 1.1 * self.basic_price
        Event._ticket_number += 1
        self.__id = Event._ticket_number
        self.__customer = customer

    @property
    def price(self):
        return self.__price

    @property
    def id(self):
        return self.__id

    @property
    def customer(self):
        return self.__customer


event1 = Event("Mondstadt", date(2021, 12, 31), 10, 250)
customer1 = Customer("Alberich", "Kaeya", True)
customer2 = Customer("Ragnvindr", "Diluc")
event1.ticket(customer1, date(2021, 12, 29))
event1.ticket(customer2, date(2021, 10, 27))
event1.serialization("tickets.JSON")
print(event1.find_ticket("2", "tickets.JSON"))
print(event1.price("1", "tickets.JSON"))
print(event1.return_str("2", "tickets.JSON"))
print(event1.find_id(1))
