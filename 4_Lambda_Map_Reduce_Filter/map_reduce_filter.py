import functools

# Python 'map' function takes:
# Mapping from N values to N values
# 1.) a function (callable)
# 2.) variable number of iterables

print("----------Map N -> N----------")

my_list = [1, 2, 3]

def square_value(val):
    return val**2

my_list_squared = list(map(square_value, my_list))
print(my_list_squared)

# elementweise Multiplikation
my_vector1 = [1, 2, 3]
my_vector2 = [-1, 4, 0]

my_result = list(map(lambda x, y: x * y, my_vector1, my_vector2))
print(my_result)

# Python 'reduce' function takes:
# Mapping from N values to 1 values
# 1.) a function (callable)
# 2.) variable number of iterables

print("----------Reduce N -> 1----------")

my_list2 = [10, -2, 5, -10, 7, 23, -1]

# größte Element aus Liste
list_max = functools.reduce(lambda x, y: x if x > y else y, my_list2)
print(list_max)
# kleinste Element aus Liste
list_min = functools.reduce(lambda x, y: x if x < y else y, my_list2)
print(list_min)

print("----------Filter (Bsp.: Listen filtern)----------")

my_list3 = [10, -2, 5, -10, 7, 23, -1]

# alle positiven Elemente
my_list_filtered = list(filter(lambda x: True if x >= 0 else False, my_list3))
print(my_list_filtered)

