# args (arguments) beliebig viele Argumente übergeben
# *args: variable number of pos. arguments
# Reihenfolge: NORMAL ARGS; *ARGS; DEFAULT ARGS

def my_function2(a, b, *args):
    print(*args, type(args))
    print('a: {}, b: {}, args: {}'.format(a, b, args))

my_function2(1, 2, 3, 4)

def my_function3(*args):
    print(*args, type(args))
    print('args: {}'.format(args))

my_function2(1, 2, 3, 4, 5, 6, 7)

# NORMAL ARGS; *ARGS; DEFAULT ARGS
def my_function4(a, *args, b=None):
    print(*args, type(args))
    print('a: {}, b: {}, args: {}'.format(a, b, args))

my_function4(1, 5, 4, b=2)