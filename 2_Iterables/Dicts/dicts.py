# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# Dict: immutable

# Types for the keys: BOOL, INT, NONE, FLOAT, STR, TUPLE (immutable types)
# Types for the values: any type

print("----------Erstellen----------")

my_dict = dict()
my_dict = {True: 'test', 10: [1, 2, 3], None: 10.5, 
            10.1: {'k': 'v'}, 'hans': {'test'}, (10, 20): (5, 4)}
print(my_dict)

my_dict2 = dict(firstname='Hans', lastname='Meier')
print(my_dict2)

print("----------Hinzufügen----------")

my_dict2['birthday'] = '08.03.1980'
print(my_dict2)
print(my_dict2['birthday'])
print(len(my_dict2))

print("----------Ausgabe: Keys, Values----------")

for key in my_dict2.keys():
    print(key)

for val in my_dict2.values():
    print(val)

for key, val in my_dict2.items():
    print(key, val)

print("----------Löschen----------")

del my_dict2['birthday']
print(my_dict2)

print("----------Werte holen----------")

birthday = my_dict2.get('birthday')

if birthday:
    print(birthday)
print(my_dict2)

print("----------Werte entfernen----------")

print(my_dict2.pop('firstname', None))
print(my_dict2)