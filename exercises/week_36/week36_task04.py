# Sample solution for task 3 of the week 36 exercises
# Turid Torheim, NMBU

# Task 4 - Working with files
# Copy the file "norway_municipalities_2017.csv" into your working directory
# This file contains information about the Norwegian municipalities for our 2017 national election,
# specifically which district each minicipality belongs to, as well as their population
# Write a script that reads from this file, and prints a table showing the number of municipalities and total
# population of each district.
# Plot a figure that shows the total population in each disctrict.

import matplotlib.pyplot as plt
import pandas as pd

# This solution uses the pandas library to read the csv file and work with the data.
# The pandas csv reader reads the csv file and creates a DataFrame object, which is a 2-dimensional table of data
# with rows and columns. This is very similar to R's data frame, and to how you are used to working with spreadsheets
# in for example Excel

# First read from the file.
# Unless otherwise specified, the first row of the csv file will be used as the column names for the DataFrame.
# Note that pandas is also able to read the special Norwegian characters æ, ø and å, as long as the file is saved
# with UTF-8 encoding.
election_data = pd.read_csv("norway_municipalities_2017.csv")

# Group the data by district
# Groupby will by default sort the data by the groupby column, in this case "District".
# We specify that the municipalities should be counted, and the population should be summed
data_by_district = election_data.groupby("District").agg(Municipalities=("Municipality", "count"),
                                                         Population=("Population", "sum"))
print(data_by_district)

# Show the population distribution by district in a bar chart.
# The x-axis will be the district names, and the y-axis will be the population.
plot = data_by_district.plot(kind="bar", y="Population", legend=False)
plt.xlabel("District")
plt.ylabel("Population")
plt.title("Population Distribution by District")
plt.show()

# Let's make a version of the bar chart that is sorted by population, so that we can see which district has the
# largest population.
# We can use the sort_values function to sort the DataFrame by the "Population" column.
data_by_district_sorted = data_by_district.sort_values(by="Population", ascending=False)
plot = data_by_district_sorted.plot(kind="bar", y="Population", legend=False)
plt.xlabel("District")
plt.ylabel("Population")
plt.title("Population Distribution by District")
plt.show()
