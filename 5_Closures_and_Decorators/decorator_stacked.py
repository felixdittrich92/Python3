import time
from functools import wraps

def debug(fn):
    print("Entering debug!")
    @wraps(fn)
    def debugger(*args, **kwargs):
        print("Entering debugger!")
        args_values_types = [(a, type(a)) for a in args]
        kwargs_values_types = [(k, v, type(v)) for k, v in kwargs.items()]
        print("Args: {}".format(args_values_types))
        print("Kwargs: {}".format(kwargs_values_types))
        print("Function {} called".format(fn.__name__))
        fn_result = fn(*args, **kwargs)
        print("Function {} returns: {}".format(fn.__name__, fn_result))
        return fn_result
    return debugger

def timing(fn):
    print("Entering timing!")
    @wraps(fn)
    def timer(*args, **kwargs):
        print("Entering timer!")
        start_time = time.perf_counter()
        fn_result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        time_duration = end_time - start_time
        print("Function {} took: {} s".format(fn.__name__, time_duration))
        return fn_result
    return timer

@timing
@debug
def my_function(name):
    print("Hello: {}".format(name))

my_function("Hans")