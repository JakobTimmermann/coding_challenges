import os
import sys

import numpy as np

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_number_generator, get_prime_factors


def construct_totients_with_matrix(limit):
    # In general this would work but runs into memory problems
    png = prime_number_generator()
    prime_number = next(png)
    totients = np.ones((limit, limit), dtype="uint8")
    totients = np.tril(totients, k=-1)
    while prime_number < limit / 2 + 1:
        totients[2 * prime_number - 1::prime_number, prime_number::prime_number] = 0
        prime_number = next(png)
    return totients.sum(axis=1)


def relative_prime_sieve(number):
    # In general this would work but it will take forever time
    relative_primes = [1] * number
    relative_primes[-1] = 0
    for i in range(0, number - 2):
        if relative_primes[i + 1] == 0:
            continue
        if number % (i + 2) == 0:
            relative_primes[i + 1::(i + 2)] = [0] * int(number / (i + 2))
    return sum(relative_primes)


def calculate_totient_via_formula(number):
    # totient (phi) can be calculated via the prime numbers used to construct its number
    # where for number = prime_1 * prime_2 we get
    # phi(number) = (prime_1 - 1) * (prime_2 - 1)
    # with prime_1 != prime_2
    # if prime_1 == prime_2 ==> phi(prime_1 * prime_1) = prime_1 * (prime_1 - 1)
    primes = get_prime_factors(number)
    totient = 1
    for prime in set(primes):
        if primes.count(prime) > 1:
            totient *= (primes.count(prime) - 1) * prime * (prime - 1)
        else:
            totient *= (prime - 1)
    return totient


# calculate_totient_via_formula would still take too long (due to get_prime_factors) However we only have to consider
# numbers that are constructed based on prime pairs because:
# If we consider n = p1 * p2 based on a prime pair (p1, p2 ) and n' as a product of a prime tuple (p1, p2, p3)
# Then with r as the ratio of n/φ(n) and r', the ratio of n'/φ(n') we look at r/r’ = (p3-1)/p3 which is smaller than 1.
# And thus r < r', so a composite number n which is a product of two primes will produce the minimal ratio.

# Considering only primes between 2000 and 4000 because sqrt of 10_000_000 is about 3162

def is_permutation(number_one, number_two):
    if set(str(number_one)) != set(str(number_two)):
        return False
    return sorted(list(str(number_one))) == sorted(list(str(number_two)))


primes = []
png = prime_number_generator()
prime = next(png)
while prime < 4000:
    if prime > 2000:
        primes.append(prime)
    prime = next(png)


def calculate_totient_ratio_for_permutations(limit, primes):
    min_ratio, min_number = 2, 0
    for idx, p1 in enumerate(primes):
        for p2 in primes[idx + 1:]:
            if (p1 + p2) % 9 != 1:  # Two numbers are only permutations if their difference is a multiple of 9
                continue
            number = p1 * p2
            totient = (p1 - 1) * (p2 - 1)
            if number > limit:
                return min_ratio, min_number
            if is_permutation(number, totient):
                ratio = number / totient
                if ratio < min_ratio:
                    min_ratio = ratio
                    min_number = number


print(f"Number for with the ratio n/φ(n) (with the totient φ(n)) produces a minimum:"
      f" {calculate_totient_ratio_for_permutations(10_000_000, primes)[1]}")

