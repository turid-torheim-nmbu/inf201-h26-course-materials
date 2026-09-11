"""
This is a sample solution for the zodiac sign dating app exercise, using the pandas library.
In this script we find two person's zodiac signs, compare them to the provided compatibility list
and print the result.
"""

__author__ = "Turid Torheim, NMBU"

from datetime import datetime

import pandas as pd


def find_zodiac(birth_day_str: str, zodiac_info: pd.DataFrame) -> str:
    """
    Function for finding the correct zodiac sign for a given birth date

    Args:
        birth_day_str: Birth date as a string with format "%d/%m/%Y", i.e. "16/03/2005"
        zodiac_info: Pandas dataframe with information on zodiac signs.
                     Should contain a column called "date_range" where each entry has the format
                     "Month-name date - Month-name date", i.e. "March 21 - April 19"
    Returns:
        A string with the zodiac sign corresponding to the provided birth date
    """

    # Convert the birth day string to a date
    # The .date() at the end removes the time stamp, as we are only interested in dates
    birth_day = datetime.strptime(birth_day_str, "%d/%m/%Y").date()
    # Extract birth year
    # By comparing using the correct year, we should avoid problems with leap years
    birth_year = birth_day.year

    # Split date range into start and and date
    zodiac_info[["start_date", "end_date"]] = zodiac_info["date_range"].str.split(" - ", expand=True)

    # Loop through the rows of zodiac_info to compare the birth date to the date range for each
    # zodiac sign until we find the correct one
    for sign_row in zodiac_info.itertuples(index=False):

        # First convert start and end dates to date time format
        # We use the year from the birth date, to avoid problems with leap year comparisons
        start_date = (datetime.strptime(f"{sign_row.start_date} {birth_year}", "%B %d %Y").date())
        end_date = (datetime.strptime(f"{sign_row.end_date} {birth_year}", "%B %d %Y").date())

        if start_date < end_date:
            # We check this as one of the date ranges crosses the year boundary,
            # making the end date come "before" the start date
            if birth_day >= start_date and birth_day <= end_date:
                return sign_row.zodiac_sign
        else:
            # end before start, ie wraps around the year
            if birth_day >= start_date or birth_day <= end_date:
                return sign_row.zodiac_sign

    # If we for some reason end up not selecting any of the signs, return a string saying "No sign chosen"
    return "No sign chosen"


def find_compatible(zodiac_sign: str, zodiac_info: pd.DataFrame, comp: str) -> list[str]:
    """
    Extract the compatible or incompatible signs to the given sign

    Args:
        zodiac_sign: String stating a zodiac sign, for example "Virgo"
        zodiac_info: Pandas dataframe with zodiac sign information.
                     Should contain the columns "zodiac_sign" (as "Virgo"),
                     "compatible" as ("Capricorn and Taurus") and
                     "incompatible" as ("Gemini and Sagittarius")
        comp: String indicating whether we are extracting the compatible or
              the incompatible signs.
              Should be either "compatible" or "incompatible"
    Returns:
        List of compatible or incompatible signs, for example ["Capricorn", "Taurus"]
    """

    # Extract the row for the relevant zodiac sign.
    # Using iloc here makes row a pandas Series rather than a 1D DataFrame,
    # making indexing more straigth-forward.
    row = zodiac_info[zodiac_info["zodiac_sign"] == zodiac_sign].iloc[0]
    return [s.strip() for s in str(row[comp]).split("and")]


def check_compatibility(candidates: list[dict], zodiac_info: pd.DataFrame) -> str:
    """
    Checks zodiac sign comparibility between two candidates, and prints the result.

    Args:
        candidates: List of dicts with information on two candidates.
                    Should contain "name", "zodiac_sign",
                    "compatible" and "incompatible"
        zodiac_info: Pandas dataframe with zodiac sign information.

    Returns:
        String stating whether the two candidates are "compatible"
        "incompatible" or whether the test is "inconclusive"
    """

    # Find each persons zodiac sign, as well as compatible/incompatible signs
    for candidate in candidates:
        candidate["zodiac_sign"] = find_zodiac(candidate["date_of_birth"], zodiac_info)
        candidate["compatible"] = find_compatible(candidate["zodiac_sign"], zodiac_info, "compatible")
        candidate["incompatible"] = find_compatible(candidate["zodiac_sign"], zodiac_info, "incompatible")

    # Counters to check for compatibility/incompatibility between the two candidates
    compatibility_counter = 0
    incompatibility_counter = 0

    # Check compatibility/incompatibility between person 0 and 1 as well
    # as between person 1 and 0, in case they are not the same
    if candidates[0]["zodiac_sign"] in candidates[1]["compatible"]:
        compatibility_counter += 1
    if candidates[1]["zodiac_sign"] in candidates[0]["compatible"]:
        compatibility_counter += 1
    if candidates[0]["zodiac_sign"] in candidates[1]["incompatible"]:
        incompatibility_counter += 1
    if candidates[1]["zodiac_sign"] in candidates[0]["incompatible"]:
        incompatibility_counter += 1

    # Print the result of the comparisons, as well as return a string that can
    # be used in potential further calculations
    if compatibility_counter == 2:
        print(f"{candidates[0]["name"]} and {candidates[1]["name"]} are compatible")
        return "compatible"
    elif incompatibility_counter == 2:
        print(f"{candidates[0]["name"]} and {candidates[1]["name"]} are incompatible")
        return "incompatible"
    else:
        print("The test is inconclusive, follow your heart!")
        return "inconclusive"


if __name__ == '__main__':
    # Read the file with information on the zodiac signs
    # Note that the file uses ; as a delimiter, so we need to specify that when reading the CSV file
    zodiac_df = pd.read_csv("exercises/week_37/zodiac_signs.csv", delimiter=";")

    # Input info on some potential matches
    # Here we assume comparison between two persons
    persons_test1 = [{"name": "Max", "date_of_birth": "03/11/2002"},
                     {"name": "Taylor", "date_of_birth": "27/06/2003"}]
    persons_test2 = [{"name": "Alex", "date_of_birth": "15/08/2001"},
                     {"name": "Morgan", "date_of_birth": "30/12/2000"}]

    # Check for compatability
    # Should print "Max and Taylor are compatible"
    compatibility_1 = check_compatibility(persons_test1, zodiac_df)
    # Should print "Alex and Morgan are incompatible"
    compatibility_2 = check_compatibility(persons_test2, zodiac_df)
