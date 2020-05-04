# Beispiel zu class methods

import math

class Pizza:
    def __init__(self, radius=36.0, ingredients=None):
        self.radius = radius
        if self.radius < 28.0:
            self.radius = 28.0
        elif self.radius > 64.0:
            self.radius = 64.0
        if ingredients:
            self.ingredients = ingredients
        else:
            self.ingredients = ['cheese', 'tomoatoes']
        self.pizza_dough_price = 0.001
        self.ingredients_price = 1.50

    def __str__(self):
        return f'Size={self.radius}, Ingeredients={self.ingredients}, Price={self.price()}'

    def add_ingredient(self, ingredients):
        self.ingredients.extend(ingredients) # listen "mergen"

    @classmethod   # new object
    def salami(cls, radius=36.0):
        return cls(radius=radius, ingredients=['cheese', 'tomatoes', 'salami'])

    @classmethod  # new object
    def prosciutto(cls, radius=36.0):
        return cls(radius=radius, ingredients=['cheese', 'tomatoes', 'ham'])

    def price(self):
        toal_pizza_dough_price = self.pizza_dough_price * Pizza.circle_area(self.radius)
        total_ingredients_price = self.ingredients_price * len(self.ingredients)
        return round(toal_pizza_dough_price + total_ingredients_price, 2)

    @staticmethod
    def circle_area(radius):
        return (radius**2) * math.pi

pizza1 = Pizza(radius=28.0)
pizza1.add_ingredient(['pepper'])
print(pizza1)

pizza2 = Pizza.salami()
print(pizza2)

pizza3 = Pizza.prosciutto()
print(pizza3)


