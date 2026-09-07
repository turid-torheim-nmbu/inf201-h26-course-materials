import numpy as np

var1 = 2.34
var2 = 5.1


def add_one(x):
    return x + 1


E = np.e
var2 = var1 + add_one(E)

print("New number")
print(var2)
