

def squaring_list(input_list):
    squared_list = [x**2 for x in input_list]
    return input_list, squared_list

list1 = [x for x in range(10)]

tuple1 = squaring_list(list1) # tuple
print(tuple1)

# tuple unpacking
list2, squred_list = squaring_list(list1)
print(list2)
print(squred_list)

# tuple packing
x = 2
y = 3
z = 4

t = x, y, z
print(t, type(t))