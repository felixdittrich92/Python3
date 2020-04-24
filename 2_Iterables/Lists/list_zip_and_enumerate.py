list1 = [x for x in range(20) if x % 2 == 0]
print(list1)

# enumerate - Index und Wert 

for index, val in enumerate(list1):
    print(index, val)

print("---------------------")

# zip - returns an iterator of tuples based on the iterable objects.
list1 = [x for x in range(20) if x % 2 == 0]
list2 = [x**2 for x in range(20) if x % 2 == 0]

for num, num_squared in zip(list1, list2):
    print(num, num_squared)
