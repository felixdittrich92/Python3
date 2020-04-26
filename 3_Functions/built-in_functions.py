# https://docs.python.org/3/library/functions.html

# absoluten Wert
my_number = -10.2
print(abs(my_number))

print("----------")

my_experiment = [True, True, True]
# wenn mind. 1 True -> True
print(any(my_experiment))
# wenn alle True -> True sonst False
print(all(my_experiment))

my_numbers = [-1, 1, 2]
print(all(my_numbers))

print("----------")

my_character = 'J'
# Nummer des Characters
print(ord(my_character))
# Character der Nummer
print(chr(74))

print("----------")

# Integerdivision und Rest
print(divmod(10, 3)) # Integerdivision: 10 // 3, und Rest: 10 % 3

print("----------")

# Liste "umdrehen"
print(list(reversed(my_numbers)))