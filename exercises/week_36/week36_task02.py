# Sample solution for task 2 of the week 36 exercises
# Turid Torheim, NMBU

# Task 2 - User input
# Write a script that asks the user for an integer between 1 and 10
# The script should then print all integers starting with 0 and ending with the inputted number

# We first use the input function to ask the user for a number
input_num = input("Enter an integer between 1 and 10: ")
print("You entered:", input_num)
# Note: Below we specify int(input_num) as the input function returns a string, not an integer.
# You can verify this by printing type(input_num).
print("Let me count for you: ")
for i in range(1, int(input_num) + 1):
    # The range function will by default start at 0 and end at n-1.
    # We therefore have to specify that we want to start at 1 and end at n.
    print(i)
# Another option is to create a list of the numbers and printing that instead.
print("Or if you prefer a list: ")
print(list(range(1, int(input_num) + 1)))
