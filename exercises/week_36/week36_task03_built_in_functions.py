# Sample solution for task 3 of the week 36 exercises
# Turid Torheim, NMBU

# Task 3 - String formatting
# Write a script that prints a nicely formatted table of the alphabet (A-Z) with both upper case and lower case letters
# You can base this solution on imported modules, or use build-in functions only (or why not try both versions?)

# For this solution, we will take advantange of the fact that the letters in the alphabet are represented
# by numbers in the ASCII table. The lower case letters are represented by the numbers 97-122, and the
# upper case letters are represented by the numbers 65-90.

# To make the output pretty, we print a header with a border underneath.
# The ':<15' in the f-string specifies that the string should be left-aligned and take up 15 characters of space,
# making the header take up a total of 30 characters.
print(f"{'Lower case':<15}{'Upper case':<15}")
print("-" * 30)
# Loop through the letters, and print them
for i in range(26):
    lower = chr(97 + i)
    upper = chr(65 + i)
    print(f"{lower:<15}{upper:<15}")
