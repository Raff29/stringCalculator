"""
This programm performs a sum of the numbers in a string
separated by a comma or a specified custom delimiter
"""
import re


# get_delimiters() Function to get a list of delimiters @param string_numbers: String of numbers separated by a comma
# or a custom delimiter specified at the start of the string @return delimiters: List of delimiters
def get_delimiters(string_numbers):
    # Set default delimiter as comma
    delimiters = [","]

    # Find if there is a custom delimiter in the string
    custom_delimiter = re.search("//(.*)\n", string_numbers)
    if custom_delimiter:
        # Split the custom delimiters and set delimiters variable to the custom delimiters specified
        delimiters = custom_delimiter.group(1).split(",")

    return delimiters


# check_negative() Function to check if there are negative numbers present in a list
# if a negative number is found, an exception is thrown with a custom message
# @param numbers: List of numbers
def check_negative(numbers):
    negative_numbers = [x for x in numbers if x < 0]

    if negative_numbers:
        raise ValueError(
            "Negative numbers not allowed. Please remove numbers {}".format(
                negative_numbers
            )
        )


# Add() Function to perform a sum of the numbers present in a string of numbers separated by delimiters
# @param string_numbers: String of numbers separated by a comma or a custom delimiter specified at the start of the string
# @return result: type int. Result of the sum performed on the numbers. Empty strings return 0
def Add(string_numbers):
    # If string is empty
    if not string_numbers:
        return 0

    # Define delimiters
    delimiters = get_delimiters(string_numbers)

    # Remove delimiter expression from the string
    string_numbers = re.sub("//(.*)\n", "", string_numbers)

    # Remove new lines from string
    string_numbers = re.sub("\n", "", string_numbers)

    # Split the string on the delimiters and convert the list items to integers
    numbers = list(
        map(int, re.split("|".join(map(re.escape, delimiters)), string_numbers))
    )

    # Check for negative numbers
    check_negative(numbers)

    # Remove numbers greater than 1000
    numbers = [x for x in numbers if x <= 1000]

    result = sum(numbers)

    return result
