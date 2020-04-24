import random

list1 = [x for x in range(0,10)]
print(list1)

list2 = [x**2 for x in range(0,5)]
print(list2)

values = ['hi', 'by', 'eye']
list3 = [x*3 for x in values]
print(list3)

list4 = [random.randint(-10, 10) for _ in range(10)]  # _ falls Variable nicht weiter benötigt wird
print(list4)

# nur positiven Werte aus list4
list5 = [x for x in list4 if x >= 0]
print(list5)

# nur negativen Werte aus list4
list6 = [x for x in list4 if x < 0]
print(list6)

# positiv: do nothing
# negativ: square
list7 = [x if x >= 0 else x**2 for x in list4]
print(list7)

# Matrix 4x3
NUM_ROWS = 4
NUM_COLS = 3
matrix = [[1 for col_idx in range(NUM_COLS)] for row_idx in range(NUM_ROWS)]
print(matrix)