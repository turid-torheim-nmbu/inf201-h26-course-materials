"""
This is a sample solution for the zodiac sign dating app exercise, using only the standard library.
In this script we find two person's zodiac signs, compare them to the provided compatibility list
and print the result.
"""

__author__ = "Turid Torheim, NMBU"

import csv
from datetime import datetime


def read_zodiac_file(info_file: str) -> list[dict]:
    """
    Read the zodiac sign information from a CSV file and return it as a list of dictionaries.

    Args:
        info_file: Path to the CSV file containing zodiac sign information.
    Returns:
        A list of dictionaries, where each dictionary represents a zodiac sign and its associated data.
    """
    all_zodiac_info = []
    with open(info_file, encoding="utf-8") as f:
        # The CSV file uses ; as a delimiter, so we need to specify that
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            # Split the date range into start and end dates
            # (each as a string with format "Month-name date", i.e. "March 21")
            row["start_date_str"], row["end_date_str"] = [s.strip() for s in row["date_range"].split("-")]
            # Extract the compatible and incompatible signs as lists of strings, by splitting the string on "and"
            row["compatible"] = [s.strip() for s in row["compatible"].split("and")]
            row["incompatible"] = [s.strip() for s in row["incompatible"].split("and")]
            all_zodiac_info.append(row)
    return all_zodiac_info


def find_zodiac(birth_day_str: str, info_list: list[dict]) -> tuple[str, list[str], list[str]]:
    """
    Find the correct zodiac sign for a given birth date

    Args:
        birth_day_str: Birth date as a string with format "%d/%m/%Y", i.e. "16/03/2005"
        info_list: List of dictionaries with information on each zodiac sign.
    Returns:
        A tuple containing:
            - the zodiac sign corresponding to the provided birth date
            - a list of compatible signs
            - a list of incompatible signs
    """

    # Convert the birth day string to a date
    # The .date() at the end removes the time stamp, as we are only interested in dates
    birth_day = datetime.strptime(birth_day_str, "%d/%m/%Y").date()
    # Extract birth year
    # By comparing using the correct year, we should avoid problems with leap years
    birth_year = birth_day.year

    # Loop through the zodiac sign information to find the correct sign for the provided birth date
    for sign_row in info_list:
        # Convert the start and end dates for each zodiac sign to datetime objects,
        # using the birth year to avoid problems with leap years
        start_date = (datetime.strptime(f"{sign_row['start_date_str']} {birth_year}", "%B %d %Y").date())
        end_date = (datetime.strptime(f"{sign_row['end_date_str']} {birth_year}", "%B %d %Y").date())
        if start_date < end_date:
            # We check this as one of the date ranges crosses the year boundary,
            # making the end date come "before" the start date
            if birth_day >= start_date and birth_day <= end_date:
                # if the birth date is within the date range for this zodiac sign
                return sign_row["zodiac_sign"], sign_row["compatible"], sign_row["incompatible"]
        else:
            # end before start, ie wraps around the year
            if birth_day >= start_date or birth_day <= end_date:
                # if the birth date is within the date range for this zodiac sign
                return sign_row["zodiac_sign"], sign_row["compatible"], sign_row["incompatible"]

    # If we for some reason end up not selecting any of the signs
    # Without this, the function will return None, which could cause problems later on
    return "No sign", "No compatible signs", "No incompatible signs"


def check_compatibility(candidates: list, zodiac_info: list[dict]) -> str:
    """
    Check zodiac sign compatibility between two candidates, and prints the result.

    Args:
        candidates: List of dicts with information on two candidates.
                    Should contain "name", "zodiac_sign", "compatible" and "incompatible"
        zodiac_info: List of dicts with information on each zodiac sign.
    Returns:
        String stating whether the two candidates are "compatible", "incompatible" or the test is "inconclusive"
    """

    # Find their zodiac signs, as well as compatible/incompatible signs
    for candidate in candidates:
        candidate["zodiac_sign"], candidate["compatible"], candidate["incompatible"] = \
            find_zodiac(candidate["date_of_birth"], zodiac_info)

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
    zodiac_file = "exercises/week_37/zodiac_signs.csv"
    zodiac_list = read_zodiac_file(zodiac_file)

    # Input info on two potential matches
    persons_test1 = [{"name": "Max", "date_of_birth": "03/11/2002"},
                     {"name": "Taylor", "date_of_birth": "27/06/2003"}]
    persons_test2 = [{"name": "Alex", "date_of_birth": "15/08/2001"},
                     {"name": "Morgan", "date_of_birth": "30/12/2000"}]

    # Check for compatability
    # Here we assume comparison between two persons
    # Should print "Max and Taylor are compatible"
    compatibility_1 = check_compatibility(persons_test1, zodiac_list)
    # Should print "Alex and Morgan are incompatible"
    compatibility_2 = check_compatibility(persons_test2, zodiac_list)
