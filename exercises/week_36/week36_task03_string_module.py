# Sample solution for task 3 of the week 36 exercises
# Turid Torheim, NMBU

# Task 3 - String formatting
# Write a script that prints a nicely formatted table of the alphabet (A-Z) with both upper case and lower case letters
# You can base this solution on imported modules, or use build-in functions only (or why not try both versions?)
import string

# The string module has functions who will return both the upper case and lower case letter of the alphabet.
# To make the output pretty, we print a header with a border underneath.
# The :<15> in the f-string specifies that the string should be left-aligned and take up 15 characters of space,
# making the header take up a total of 30 characters.
print(f"{'Upper case':<15}{'Lower case':<15}")
print("-" * 30)
# Loop through the letters, and print them
# The zip function creates tuples of each upper and lower case letter pair,
# allwoing us to easily loop over them.
for upper, lower in zip(string.ascii_uppercase, string.ascii_lowercase, strict=True):
    print(f"{upper:<15}{lower:<15}")

# We can also chose to display the alphabet in a more compact way, with 3 rows of up to 10 letters each.
# First we use the zip function as before to collect the lower and upper case letter pairs.
# We turn this into a list to be able extract rows of length 10 for our output table.
alphabet = list(zip(string.ascii_uppercase, string.ascii_lowercase, strict=True))
# Then we print the letters in rows of 10, with the upper and lower case letters separated by a slash.
# The '10' argument in the range function indicates that we want to loop through the alphabet list in steps of 10.
print("\nCompact table of the alphabet")
for i in range(0, len(alphabet), 10):
    # Each row in the table should show the 10 next letters.
    row = alphabet[i : i + 10]
    # Use "/" as separator between upper and lower case,
    # and " | " as separator between the different letters.
    print(" | ".join(f"{upper}/{lower}" for upper, lower in row))
