import time 
from functools import wraps

# TIMER
print("----------TIMER----------")

def timing_extended(use_ns_timer=False):
    if use_ns_timer:
        time_fn = time.perf_counter_ns
        time_scale = "ns"
    else:
        time_fn = time.perf_counter
        time_scale = "n"

    def timing(fn): # Decorator          
        @wraps(fn)
        def timer(*args, **kwargs):
            start_time = time_fn()
            fn_result = fn(*args, **kwargs)
            end_time = time_fn()
            time_duration = end_time - start_time
            print("Function {} took: {} {}".format(fn.__name__, time_duration, time_scale))
            return fn_result
        return timer
    return timing # return Decorator

@timing_extended(use_ns_timer=True)
def iterate(n):
    val = 0
    for i in range(n):
        val += i
    return val

iterate(1_000_000)


