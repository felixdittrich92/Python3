def grow_list(val, my_list=None, a=4, b=True):
    if my_list:
        my_list.append(val)
    else:
        my_list = [val]
    return my_list

my_func = grow_list
print(my_func, type(my_func))

# gibt alle magic methods der Funktion aus
# print(dir(grow_list))

# Funktions Attribute
print(grow_list.__defaults__)
print(grow_list.__name__)
print(grow_list.__code__.co_argcount)
print(grow_list.__code__.co_varnames)