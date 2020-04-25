import matplotlib.pyplot as plt

# kwargs (keyword arguments)

# NORMAL ARGS; *ARGS; DEFAULT ARGS; **KWARGS
# *ARGS: TUPLE
# **KWARGS: DICT
def my_function(a, *args, x=2, y=3, z=4, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))
    print('a: {}, x: {}, y: {} , z: {}, args: {}, kwargs: {}'.format(a, x, y, z, args, kwargs))

my_function(1, 3, 4, x=13.37, b=False, c=30, d=40.5)

print("--------------------------------")

def my_function2(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))
    print('args: {}, kwargs: {}'.format(args, kwargs))

my_function2(1, 3, 4, x=13.37, b=False, c=30, d=40.5)

print("--------------------------------")

def my_function3(a, *args, **kwargs):
    print(a)
    a *= 2
    print(a)
    print(args, type(args))
    print(kwargs, type(kwargs))
    print('args: {}, kwargs: {}'.format(args, kwargs))

my_function3(1, 3, 4, x=13.37, b=False, c=30, d=40.5)


# Beispiel:
def plot_my_lists(list_x, list_y, **kwargs):
    plt.scatter(list_x, list_y, **kwargs)
    plt.show()

list_x = [-3, -2, -1, 1, 2, 3]
list_y = [9, 4, 1, 1, 4, 9]
#                             Kwargs
plot_my_lists(list_x, list_y, c='red')