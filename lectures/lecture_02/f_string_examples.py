# Some examples of string formatting in Python.
# Turid Torheim, NMBU

# Printing or writing nice looking strings with a lot of flexibility
name = "Turid"
course = "INF201"
year = 2026
print("Hello, " + name + "! You are teaching " + course + " the autumn of " + str(year) + ".")
print(f"Hello, {name}! You are teaching {course} the autumn of {year}.")

# Formatting numbers in strings
number = 2
print(f"{number} divided by 3 is {number / 3}.")
print(f"{number} divided by 3 is {number / 3:.2f}.")
print(f"{number} divided by 3 is {number / 3:.1%}.")

# Alignment and padding
print(f"{42:0>5}")
print(f"{'Lower case':<15}{'Upper case':<15}")
for i in range(26):
    lower = chr(97 + i)
    upper = chr(65 + i)
    print(f"{lower:<15}{upper:<15}")
