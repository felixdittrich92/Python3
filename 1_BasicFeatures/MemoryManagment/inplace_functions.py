# in-place Funktion: Veränderung innerhalb einer Funktion ohne return !
# welche dann auch global verändert wurde -> List Elemente mutable

def increment_list(lst, val):
    for i in range(len(lst)):
        lst[i] += val

my_list = [1, 2, 3]
val = 1

increment_list(my_list, val)
print(my_list)
