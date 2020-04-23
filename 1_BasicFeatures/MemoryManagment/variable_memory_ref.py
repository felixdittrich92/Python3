import ctypes

# Ausgabe der Speicheradresse
def print_memory_adress(var):
    print(hex(id(var)))
# int
# bei Werten über 200 teilen Sie sich nicht mehr die gleichen Speicheradressen
int_value = 10
int_value1 = 10
int_value2 = 58
print_memory_adress(int_value)
print_memory_adress(int_value1) # selbe Speicheradresse, da selbe Wert
print_memory_adress(int_value2)

# float
float_value = 10.0
float_value1 = 10.0
float_value2 = 58.3
print_memory_adress(float_value)
print_memory_adress(float_value1) # selbe Speicheradresse, da selbe Wert
print_memory_adress(float_value2)

# boolean
bool1 = True
bool2 = False
print_memory_adress(bool1)
print_memory_adress(bool2)

# None
none = None
print_memory_adress(none)

# list
list1 = [1, 2, 3]
list2 = list1
list3 = [4, 5, 6]
print_memory_adress(list1)
print_memory_adress(list2) # selbe Speicheradresse
print_memory_adress(list3) # andere

value = 23.454657
print(ctypes.c_long.from_address(id(value)))


