# This is also an improved version of the ugly script
# I have included type hints to the functions, more about that in the week 38 lecture

import numpy as np


def add_one(x: float) -> float:
    """Add one to the floating point number"""
    return x + 1


# As we only use np.e as input to the function,
# and don't do anything else with it, it doesn't really need to be saved as a variable
var1 = 2.34
var2 = var1 + add_one(np.e)

# f-strings are a flexible way to format strings
print(f"New number: {var2:.2f}")
