import math

"""
This is just reusing the code from p-73 with adapted limits!
"""


def determine_number_of_fractions_inbetween_target(denominator, lower_limit_denominator=3, upper_limit_denominator=2):
    upper_bond = math.floor(denominator / upper_limit_denominator)
    lower_bond = math.ceil(denominator // lower_limit_denominator)
    if denominator % 2 == 0:
        return upper_bond - lower_bond - 1
    return upper_bond - lower_bond


def main(limit):
    """
     We have to take into account that e.g. for 24 as denominator we only have one new fraction (11/24)
     since 9/24 and 10/24 are no new distinct fractions as they collapse to 3/8 and 5/12 and should not be counted
     In order to do so we in advance decrease the number of fractions for a denominators that are multiples of the
     current denominator
    """
    number_of_factions = [0] * (limit + 1)
    for digit in range(1, limit + 1):
        fractions = determine_number_of_fractions_inbetween_target(digit, 1_000_001, 1)
        number_of_factions[digit] += fractions
        for multiple in range(2 * digit, limit + 1, digit):
            number_of_factions[multiple] -= 1 * number_of_factions[digit]
    return sum(number_of_factions)


print(f"Number of elements contained in the set of reduced proper fractions for d ≤ 1,000,000: {main(1_000_000)}")

