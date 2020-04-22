import sys
import math

# Typüberprüfung
value_int = 42
print(type(value_int))

if isinstance(value_int, int):
    print("it´s Integer")

# gibt aus wieviel Byte benötigt werden
print(sys.getsizeof(value_int))

# Arithmetische Operationen
# Die Division von (int/int) => float
# andere Operationen (int + int) => int
result = 10 / 5   
print(result, type(result))

# Integer Division  -> oder casten int()
result = 10 // 5  
print(result, type(result))

# abrunden/aufrunden
value = 2.5
print(int(value))
print(math.floor(value)) # abrunden
print(math.ceil(value)) # aufrunden

value = -2.5
print(int(value))
print(math.floor(value)) # abrunden
print(math.ceil(value)) # aufrunden

# Darstellung binär, octal, hexadecimal
value = 42
print(bin(value), type(bin(value)))
print(oct(value), type(oct(value)))
print(hex(value), type(hex(value)))