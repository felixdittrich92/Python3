# Vererbung (inheritance) mit super: 
# vererbt an die Kindklasse alle Variablen und Methoden 

class A:
    def __init__(self):
        print("Init A called!")
        self.a = 2

    def hello(self):
        print('hi')

class B(A): # erbt von A
    def __init__(self):
        super().__init__() # ruft von der Elternklasse den Konstruktor __init__ auf + vererbt alle Methoden von A
        print("Init B called!")
        self.b = self.a * 2 # mit self.a von Klasse A
        print(self.b)

class C(A):
    def __init__(self):
        super().__init__()
        print("Init C called!")

class D(B, C): # Mehrfachvererbung
    def __init__(self):
        super().__init__()
        print("Init D called!")

a = A() # Elternklasse
print("---------------")
b = B() # erbt von A
b.hello()
print("---------------")
c = C() # erbt von A
print("---------------")
d = D() # erbt von B und C welche von A erben