# basic features for lists: https://docs.python.org/3/tutorial/datastructures.html
# List: mutable

def main():
    my_list = list()
    my_list = [1, 2, 3]

    print("----------Hinzufügen----------")

    # Option 1: Single Value
    my_list.append(-10)
    print(my_list)

    # Option 2: List Concatenation (Verkettung)
    my_list2 = [4, 5]
    my_list += my_list2
    print(my_list)

    # Option 3: Iterables
    it = range(-2, 3, 1)
    my_list.extend(it) # extend-erweitern
    print(my_list)

    # Option 4: Insert at user-defined index
    my_list.insert(0, "hello")
    print(my_list)
    my_list.insert(-30, "hello")
    print(my_list)

    print("----------Entfernen----------")

    # Remove values
    my_list.pop()
    print(my_list)
    while 'hello' in my_list:
        idx = my_list.index('hello')
        my_list.pop(idx)
    print(my_list)

    print("----------kopieren----------")

    # Copy
    my_list_new = my_list
    print(hex(id(my_list)))
    print(hex(id(my_list_new)))
    my_list_new = my_list.copy()
    print(hex(id(my_list)))
    print(hex(id(my_list_new)))

    print("----------umdrehen----------")

    # Reverse
    my_list.reverse()
    print(my_list)
    print(my_list[::-1])

    print("----------zählen----------")

    # Count
    print(my_list.count(1))

    print("----------sortieren----------")

    # Sort
    my_list.sort(reverse=False)
    print(my_list)

if __name__ == "__main__":
    main()