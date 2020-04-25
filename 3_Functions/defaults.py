# x, y: arguments
x = 2
y = 3

# a, b: parameters
def function(a, b):
    print(a, b)

function(x, y)

# default arguments
def function2(a, b=None):
    if b:
        print(a, b)
    else:
        print(a)

function2(x)
function2(x, b=y) # bei default parametern immer variable= -> besser lesbar 

# Funktionen ohne return Value returnen immer None !
#return_value = function2(x ,b=y)
#print(return_value)