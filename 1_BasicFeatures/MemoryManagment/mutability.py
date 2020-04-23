# Mutability beschreibt, ob ein Wert verändert werden kann oder 
# ob dieser "festgesetzt" ist

# immutable types: unveränderbare Typen: int, float, bool, str, tuple
# mutable types: veränderbare Typen: list, dict, set, etc.

list1 = [1, 2, 3]
tuple1 = (1, 2, 3)

list1[0] = -1
# tuple1[0] = -1  geht nicht, da immutable

