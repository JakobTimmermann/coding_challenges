import numpy as np


def extract_periodic_segment(number):
    sqrt_number = np.sqrt(number)
    digit = sqrt_number // 1
    if digit == np.sqrt(number):
        return 0
    denominator = 1
    numerator_rest = digit
    digit, denominator, numerator_rest = calculate_next_digit(sqrt_number, denominator, numerator_rest)
    count = 1
    while not np.isclose(denominator, 1):
        digit, denominator, numerator_rest = calculate_next_digit(sqrt_number, denominator, numerator_rest)
        count += 1
    return count


def calculate_next_digit(sqrt_number, denominator, numerator_rest):
    target_number = denominator / (sqrt_number - numerator_rest)
    new_denominator = (sqrt_number + numerator_rest) / target_number
    new_digit = target_number // 1
    remainder = target_number % 1
    new_numerator_rest = sqrt_number - remainder * new_denominator
    return new_digit, new_denominator, round(new_numerator_rest,0)


count_odds = 0
for k in range(1, 10000):
    if extract_periodic_segment(k) % 2 == 1:
        count_odds += 1
print(f"Continued fractions below 10000 with odd period: {count_odds}")
