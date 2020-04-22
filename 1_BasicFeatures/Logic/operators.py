# boolesche Operatoren: and, or, not
# Vergleichsoperatoren: <, >, <=, =>, ==, !=

# Reihenfolge der Operationen:
# 1.) ()
# 2.) Vergleichsoperationen
# 3.) boolesche Operationen (Reihenfolge beim auswerten: 1. not 2. and 3. or)

a = True
b = False
c = True

statement = a > b and c == a or not a and c
print(statement)
statement = ((a > b) and (c == a)) or ((not a) and c)
print(statement)
