class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def show_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance

    def debit(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            return self.__balance


bankccount = BankAccount(200)
print(bankccount.deposit(20))
# print(bankccount._BankAccount__balance)

"""  Polimorphism  """

import math
class Square:
    def __init__(self, vertice):
        self.vertice = vertice

    def area(self):
        return self.vertice**2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius**2, 2)

def print_the_area(obj):
    return f' the area = {obj.area()}'

Square1 = Square(4)
Circle1 = Circle(3)
print(print_the_area(Square1))
print(print_the_area(Circle1))

""" Inheritage """

class Transport:
    def __init__(self, model, color):
        self.model = model
        self.color = color

class Taxi(Transport):
    def __init__(self, model, color, type):
        super().__init__(model, color)
        self.type = type


class Bus(Transport):
    def __init__(self, model, color, fare):
        super().__init__(model, color)
        self.fare = fare


bus = Bus('AS', 'yellow', 15)
print(bus.model)
