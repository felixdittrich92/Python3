import sys
import math

value = 42e+08 # 42 * 10 ^ 8
print(value)
print('{:.32f}'.format(value))

# Typüberprüfung
value_float = 18.345
print(type(value_float))

if isinstance(value_float, float):
    print("it´s Float")

# gibt aus wieviel Byte benötigt werden
print(sys.getsizeof(value_float))

# Floats auf Gleichheit überprüfen
addition = 1/10 + 1/10 + 1/10
result = 0.3
print(addition)
print(addition == result) # False
print(math.isclose(addition, result)) # True

# abrunden/aufrunden -> incl. angabe auf welche Nachkommastelle
value = 42.6788972
print(round(value, 4), type(round(value, 4)))

value = -42.6788972
print(round(value, 4), type(round(value, 4)))