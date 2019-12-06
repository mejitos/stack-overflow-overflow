"""
    Module for all the helper functions used in "Stack Overflow
    overflow" program.
"""

import math


def round_up(x, row_length):
    """Helper function to get number of rows from number of characters

    Args:
        x: Total number of characters in a string
        row_length: Number of characters in a single row

    Returns:
        Number of rows rounded up
    """


    rounded = int(math.ceil(x / float(row_length))) * row_length
    return rounded // row_length


# def round_up(x, row_length):
#     return x if x % row_length == 0 else x + row_length - x % row_length