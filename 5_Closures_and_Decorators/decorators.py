# Decorators:
# - wraps a function by another function - "ummantelt eine Funktion mit weiteren Funktionalitäten"
# - takes a function as an argument, returns a closure
# - the clousure runs the previous passed in function with the *args and **kwargs arguments

def decorator(fn):
    print("Start decorator function from: ", fn.__name__)
    def wrapper(*args, **kwargs):
        print("Start wrapper function from: ", fn.__name__)
        fn_result = fn(*args, **kwargs)
        print("End wrapper function from: ", fn.__name__)
        return fn_result
    print("End decorator function from: ", fn.__name__)
    return wrapper

def print_arguments(a, b, c=None):
    print("a: {}, b: {}, c: {}".format(a, b, c))

decorated_print_arguments = decorator(print_arguments) # Start decorator function
decorated_print_arguments(a=10, b=20, c=30) # Start wrapper function


# kürzer
@decorator
def print_arguments2(a, b, c=None):
    print("a: {}, b: {}, c: {}".format(a, b, c))

print_arguments2(a=10, b=20, c=30)

