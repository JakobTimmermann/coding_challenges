'''
The crucial point is to use the continued fraction (Kettenbruch) approach as outlined here:
https://mathematikalpha.de/pellsche-gleichung
Also first extracting the periodic segment and then applying it to determine numerator and 
denominator seems to be redundant. It probably can be combined
'''

import numpy as np


def extract_periodic_segment(number):
    sqrt_number = np.sqrt(number)
    digit = sqrt_number // 1
    segment = [digit]
    if digit == np.sqrt(number):
        return 0
    denominator = 1
    numerator_rest = digit
    digit, denominator, numerator_rest = calculate_next_digit(sqrt_number, denominator, numerator_rest)
    segment.append(digit)
    while not np.isclose(denominator, 1):
        digit, denominator, numerator_rest = calculate_next_digit(sqrt_number, denominator, numerator_rest)
        segment.append(digit)
    return segment


def calculate_next_digit(sqrt_number, denominator, numerator_rest):
    target_number = denominator / (sqrt_number - numerator_rest)
    new_denominator = (sqrt_number + numerator_rest) / target_number
    new_digit = target_number // 1
    remainder = target_number % 1
    new_numerator_rest = sqrt_number - remainder * new_denominator
    return new_digit, new_denominator, round(new_numerator_rest, 0)


def expand_segment(segment):
    """
    There is probably a smarter approach to expand the segment but this will do as long as the periodic segment doesn't get
    too large.
    """
    periodic_segment = segment[1:]
    if len(periodic_segment) % 2 == 0:
        expansion_segment = segment[:-1]
    else:
        expansion_segment = segment + periodic_segment[:-1]
    numerator = 1
    denominator = int(expansion_segment.pop())
    while len(expansion_segment):
        digit = int(expansion_segment.pop())
        denominator, numerator = digit * denominator + numerator, denominator
    return numerator, denominator


squares = []
i = 2
while i ** 2 < 1000:
    squares.append(i ** 2)
    i += 1

max_x = 0
max_D = 0
for D in range(2, 1001):
    if D not in squares:
        segment = extract_periodic_segment(D)
        x, y = expand_segment(segment)
        if x > max_x:
            max_x = x
            max_D = D
print(f"Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained: {max_D}")
