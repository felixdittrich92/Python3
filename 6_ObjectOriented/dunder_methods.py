from math import sqrt
from functools import total_ordering

@total_ordering # Decorator fügt __lt__ hinzu
class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# Call Methode -> Bsp.: Keras funktionale API (zum Updaten von Objekten)
    def __call__(self):
        print("Calling the __call__ function!")
        return self.__repr__()

# Repräsentation - für Debugging
    def __repr__(self):
        return 'vector.Vector2D({}, {})'.format(self.x, self.y)

# String - nur Ausgabe
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

# bool also ob Objekt als True oder False interpretiert wird
    def __bool__(self):
        return bool(abs(self))


# absolute Betrag
    def __abs__(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2)) # Wurzel aus x^2 + y^2 - Satz des Pytagoras

# equal also ==
    def __eq__(self, other_vector):
        if self.x == other_vector.x and self.y == other_vector.y:
            return True
        else:
            return False

# Vergleich von Vektoren - mathematisch nicht korrekt
    def __lt__(self, other_vector):
        if abs(self) < abs(other_vector):
            return True
        else:
            return False
  
# Addition
    def __add__(self, other_vector):
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        print("Addition")
        return Vector2D(x, y)

# Subtraktion
    def __sub__(self, other_vector):
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        print("Subtraktion")
        return Vector2D(x, y)

# Multiplikation
    def __mul__(self, other):
        if isinstance(other, Vector2D):
            print("Multiplikation")
            return self.x * other.x + self.y * other.y
        else:
            print("Multiplikation")
            return Vector2D(self.x * other, self.y * other)

# Division
    def __truediv__(self, other):
        print("Division")
        return Vector2D(self.x / other, self.y / other)

v1 = Vector2D(12, 12)
print(repr(v1))
print(str(v1))

print("----------------")

v2 = Vector2D(1, 1)
print(repr(v2))
print(str(v2))

print("----------------")

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v2 / 5.0)

print("----------------")

print(abs(v2))
print(v1 == v2)
print(v2 == v2)

print("----------------")

v3 = Vector2D()

if v3: # 0, 0 daher False
    print("v3 - yes")
elif v1:
    print("v1 - yes")
else:
    print("Nothing")

print("----------------")
v4 = Vector2D(2, 3)
v5 = Vector2D(-1, 2)

print(v4 < v5)
print(v4 <= v5)
print(v4 > v5)
print(v4 >= v5)
print(v4 == v5)
print(v4 != v5)

print("----------------")
v5()
