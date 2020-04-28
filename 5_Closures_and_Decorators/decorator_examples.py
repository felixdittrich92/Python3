# Problem: The function name, its docstring, and parameter list of 'fn' are hidden by 
# the wrapper function.

# Solution: The functools.wraps decorator, opies the lost metadata from the undecorated function 
# to the decorated closure.

from functools import wraps # wraps(fn) -> dadurch gehen Metadaten wie Docu nicht verloren
import time

# Debugger
print("----------DEBUGGER----------")

def debug(fn):
    @wraps(fn)
    def debugger(*args, **kwargs):
        args_values_types = [(a, type(a)) for a in args]
        kwargs_values_types = [(k, v, type(v)) for k, v in kwargs.items()]
        print("Args: {}".format(args_values_types))
        print("Kwargs: {}".format(kwargs_values_types))
        print("Function {} called".format(fn.__name__))
        fn_result = fn(*args, **kwargs)
        print("Function {} returns: {}".format(fn.__name__, fn_result))
        print("---------------------------------------------")
        return fn_result
    return debugger

@debug
def do_something(a, b, c=None):
    """Do something.
    """
    return a + b if c else 0

@debug
def do_something2(a, b, c=None):
    return a - b if c else 0

@debug
def do_something3(a, b, c=None):
    return a * b if c else 0

@debug
def do_something4(a, b, c=None):
    return a / b if c else 0

do_something(10, 20, c=1)
do_something2(10, 20, c=1)
do_something3(10, 20, c=1)
do_something4(10, 20, c=1)


# TIMER
print("----------TIMER----------")

def timing(fn):
    @wraps(fn)
    def timer(*args, **kwargs):
        start_time = time.perf_counter()
        fn_result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        time_duration = end_time - start_time
        print("Function {} took: {} s".format(fn.__name__, time_duration))
        return fn_result
    return timer

@timing
def do_something5(a, b, c=None):
    """Do something.
    """
    return a + b if c else 0

do_something5(a=10, b=20, c=True)

@timing
def iterate(n):
    val = 0
    for i in range(n):
        val += i
    return val

iterate(1_000_000)







