import os
import sys
import re

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_number_generator, is_prime


def is_truncatable_prime(number):
    snumber = str(number)
    for i in range(1, len(snumber)):
        if not is_prime(int(snumber[i:]), include_one=False) or not is_prime(int(snumber[:i]), include_one=False):
            return False
    return True


pg = prime_number_generator()
prime = next(pg)
while prime < 10:
    prime = next(pg)

truncatable_primes = []
while len(truncatable_primes) < 11:
    if not (prime > 100 and re.search('[245680]', str(prime))):
        if is_truncatable_prime(prime):
            truncatable_primes.append(prime)
    prime = next(pg)
print(f"Sum of all truncatable primes: {sum(truncatable_primes)}")
