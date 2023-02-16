import os
import sys
from itertools import permutations

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_number_generator

##### First approach, waaaaay to slow!!
# def has_k_prime_factors(number, limit=4):
#     png = prime_number_generator()
#     prime = next(png)
#     prime_factors = set()
#     while number > 1:
#         while number % prime == 0:
#             prime_factors.add(prime)
#             number /= prime
#         if len(prime_factors) == limit:
#             return number == 1
#         prime = next(png)
#     return False
#
#
# def main(target_length):
#     consecutive_numbers = 0
#     number = 1
#     while True:
#         if has_k_prime_factors(number, limit=target_length):
#             consecutive_numbers += 1
#             if consecutive_numbers == target_length:
#                 print(number - target_length + 1)
#                 break
#         else:
#             consecutive_numbers = 0
#         number += 1
#         if number % 50 == 0:
#             print(number)
#
# main(4)


def solve_via_sieve(target=4, limit=150000):

    number_of_prime_divisors = [0] * limit
    rolling_length = 0

    for number in range(2, limit):
        if number_of_prime_divisors[number] == 0: # We found a prime
            for m in range(2 * number, limit, number):
                number_of_prime_divisors[m] += 1 # Increase number of prime factors by 1
            rolling_length = 0
        elif number_of_prime_divisors[number] == target: # We found a number that has exactly target prime factors
            rolling_length += 1
        else:
            rolling_length = 0

        if rolling_length == target:
            return number - target + 1


print(solve_via_sieve(4))
