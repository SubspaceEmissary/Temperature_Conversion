from collections import namedtuple

from abc import ABC, abstractmethod

class EquivLengthWidth(Exception):
    pass

class House:
    def __init__(self, _price, _sqft):
        self._price = f"${_price}"
        self._sqft = f"{_sqft} square feet"
    
    @property
    def price(self):
        return f"Listed at; {self._price}"

    @price.setter
    def price(self, _new_price):
        if _new_price == 0:
            raise ValueError("Price cannot be zero.")
        elif _new_price < 0:
            raise ValueError("Price cannot be negative.")
        else:
            self._price = _new_price 

    @property
    def size(self):
        return self._sqft

    @size.setter
    def size(self, new_size):
        if new_size == 0:
            raise ValueError("Size cannot zero.")
        elif new_size < 0:
            raise ValueError("Size cannot be negative.")
        else:
            self._sqft = new_size

    def __str__(self):
        return f"{self._price}, {self._sqft}"

    def __eq__(self, other):
        return self._price == other._price and self._sqft == other._sqft

    def __gt__(self, other):
        return self._price < other._price and self._sqft < other._sqft

    def __add__(self, other):
        return self._price + other._price and self._sqft + other._sqft

    def __sub__(self, other):
        return self._price - other._price and self._sqft - other._sqft
    
    def __mul__(self, other):
        return self._price * other._price and self._sqft * other._sqft
    
    def __div__(self, other):
        return self._price / other._price and self._sqft / other._sqft


house1 = House(750000, 3500)
house1.size = 10
print(house1.size)

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)