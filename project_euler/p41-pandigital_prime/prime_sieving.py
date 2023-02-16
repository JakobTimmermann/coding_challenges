import os
import sys

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_number_generator, is_prime


def is_pandigital(number):
    number_str = str(number)
    number_len = len(number_str)
    number_set = set([int(n) for n in list(number_str)])
    return number_set == set(range(1, number_len+1))


pg = prime_number_generator()
prime = next(pg)
max_pandigital_prime = 0
while prime < 10000000:
    if is_pandigital(prime):
        max_pandigital_prime = max(prime, max_pandigital_prime)
    prime = next(pg)
print(max_pandigital_prime)
