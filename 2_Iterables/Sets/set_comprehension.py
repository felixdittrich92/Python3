# Set Comprehension

my_set_comp = {i for i in range(10)}
print(my_set_comp)

my_set_comp2 = {i if i % 2 == 0 else -1 for i in range(10) if i % 3 == 1}
print(my_set_comp2)
