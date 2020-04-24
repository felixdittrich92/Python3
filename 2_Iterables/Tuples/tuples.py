# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# Tuple : immutable
# functions: index() and count()

tuple1 = ()
print(type(tuple1))

tuple2 = (20, 13, 34)
print(tuple2[0])

list1 = [1, 2, 3]
tuple3 = (10, False, list1)
print(tuple3, type(tuple3)) # list in tuple ist veränderbar

# Tuple verwenden wenn die Werte nicht verändert werden sollen ansonsten Liste