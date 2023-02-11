from utils import get_divisors
from itertools import compress

def is_abundant(number_to_check):
    unique_factors = get_divisors(number_to_check, unique_divisors=True)
    sum_of_div = sum(unique_factors)
    if sum_of_div > number_to_check:
        return True
    return False


def main(limit=28123):
    abundant_numbers = []
    for number in range(1, limit):
        if is_abundant(number):
            abundant_numbers.append(number)
    numbers = [True] * limit
    for idx, abundNum1 in enumerate(abundant_numbers):
        for abundNum2 in abundant_numbers[idx:]:
            two_sum = abundNum1 + abundNum2
            if two_sum > limit:
                break
            numbers[two_sum - 1] = False
    return sum(list(compress(range(1, limit), numbers)))


print(main())
