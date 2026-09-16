# Some examples of mutability and immutability
# Turid Torheim, NMUB

# Mutable
x = [1, 2, 3]
print(id(x))
x.append(4)  # [1, 2, 3, 4]
print(id(x))  # the same as before

print("---")

# Immutable
s = "a b c"
print(id(s))
s += " d"  # "a b c d"
print(id(s))  # changed
