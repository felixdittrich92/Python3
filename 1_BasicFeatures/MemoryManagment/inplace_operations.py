# in-place operations: nur bei mutable types

a = 10
b = 20

a = a + 1 # addition: __add__ magic method der Klasse Integer
b += 1 # in-place addition: __iadd__ magic method der Klasse Integer

print(a, b)