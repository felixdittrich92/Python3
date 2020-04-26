# Closure: innere Funktion einer Funktion

# A closure is an inner function that has access to variables 
# in the local scope of the outer function

import time

def outer_fn(message):
    outer_message = "Outer: " + message
    current_time = time.time()

    def inner_fn():
        print("Inner: '" + outer_message + "'")
        print("Current time: ", current_time)
    return inner_fn()

outer_fn("Hello World!")