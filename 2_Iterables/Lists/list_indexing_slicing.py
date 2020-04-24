# Indexing

list1 = [-1, 1, -2, 2, -3, 3]
print(list1[1]) # zweites Element Element
print(list1[-1]) # letzte Element


# Slicing: START:END:STEP

list1 = [-1, 1, -2, 2, -3, 3]
list2 = list1[-3:] # letzten 3 Werte
print(list2)

list3 = list1[:4] # index 0 bis 3, da 4 non inclusive ist
print(list3)

list4 = list1[2:4] # index 2(inclusive) bis 3, da 4 non inclusive ist
print(list4)

list5 = list1[::2] # nur jedes zweite Element
print(list5)