# Script showing aliasing in Python
# Turid Torheim, NMBU

x = [1, 2, 3]
y = x
y.append(4)
print(y)  # Output: [1, 2, 3, 4]
print(x)
print(id(x))
print(id(y))
print(id(x) == id(y))
