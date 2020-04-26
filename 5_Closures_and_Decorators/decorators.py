# Todo


# Decorators:
# - wraps a function by another function
# - takes a function as an argument, returns a closure
# - the clousure runs the previous passed in function with the *args and **kwargs arguments

def outer_fn(fn):
    def inner_fn():
        fn_result = fn()
        return fn_result
    return inner_fn

def print_hello_world():
    print("Hello World!")

decorated_print_hello_world = outer_fn(print_hello_world)
decorated_print_hello_world()

def decorator(fn):
    print("Start decorator function from: ", fn.__name__)
    def wrapper(*args, **kwargs):
        print("Start wrapper function from: ", fn.__name__)
        fn_result = fn(*args, **kwargs)
        print("End wrapper function from: ", fn.__name__)
        return fn_result
    print("End decorator function from: ", fn.__name__)
    return wrapper

decorated_print_hello_world2 = decorator(print_hello_world)
decorated_print_hello_world2()

def print_arguments(a, b, c=None):
    print("a: {}, b: {}, c: {}".format(a, b, c))

decorated_print_arguments = decorator(print_arguments)
decorated_print_arguments(a=10, b=20, c=30)
decorated_print_arguments(a=11, b=21, c=31)

@decorator
def print_arguments2(a, b, c=None):
    print("a: {}, b: {}, c: {}".format(a, b, c))

print_arguments2(a=10, b=20, c=30)

