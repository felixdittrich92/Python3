# auf Vererbung überprüfen also erbt para1 von para2 (Elternklasse)
print(issubclass(bool, int))

# Typüberprüfung
print(type(True))
print(isinstance(True, bool))
print(isinstance(False, bool))

# jedes Objekt hat einen Wahrheitswert
# Wenn die Instanz True ist und nicht: None, False, 0 oder empty
my_list = []

if my_list:
    print("yes its True")
else:
    print("no its False")

my_list.append("Hey")

if my_list:
    print("yes its true")
else:
    print("no its False")

# 'is' and 'is not': Objekte belegen gleichen Speicher (Speicheradressen)
# '==' and '!=': Wertegleichheit

value1 = 10 # int(10)
value2 = 10.0 # float(10)

if value1 == value2:
    print('== -> ist gleich')

if value1 is value2: 
    print(' is -> ist gleich')



