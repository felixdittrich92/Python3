# https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset
# keine doppelten Elemente

set1 = {1, 2, 3, 1}
print(set1, type(set1))

set2 = set([1, 2, 3, 1])

set3 = {4, 5, 6}
set4 = {6, 7, 8}
print(set3.intersection(set4)) # Ausgabe der gemeinsamen Elemente
print(set3.union(set4)) # Ausgabe Vereinigung

print("----------Hinzufügen----------")
set3.add(42)
print(set3)

print("----------Entfernen----------")
set3.pop() 

print(set3)
set3.discard(4) # spezielles Element entfernen
print(set3)