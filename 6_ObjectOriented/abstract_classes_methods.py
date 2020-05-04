import abc

# quasi wie ein Interface, gibt an welche Methoden die Klassen implementieren müssen
# ansonsten kann davon kein Objekt erstellt werden -> TypeError

# Elternklasse
class Base(metaclass=abc.ABCMeta):
    @abc.abstractmethod  # wenn Kindklasse diese Methode unbedingt implementieren muss
    def m1(self):
        return
    
    @staticmethod
    @abc.abstractmethod
    def m2(self):
        return
    
    @classmethod
    @abc.abstractmethod
    def m3(self):
        return
    
    def m4(self):
        return

# Kindklasse 1
class MyClass(Base): # erbt von Base
    def m1(self):
        return 'm1'
    
    def m2(self):
        return 'm2'
    
    #def m3(self):
    #    return 'm3'

# Kindlasse 2
class MyClass2(Base): # erbt von Base
    def m1(self):
        return 1
    
    def m2(self):
        return 2
    
    def m3(self):
        return 3

# var = MyClass() TypeError: Can't instantiate abstract class MyClass with abstract methods m3
var = MyClass2()
