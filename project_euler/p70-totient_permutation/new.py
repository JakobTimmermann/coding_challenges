import os
import sys

import numpy as np

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_number_generator


def construct_totients(limit):
    png = prime_number_generator()
    prime_number = next(png)
    primes = []
    totients = np.arange(0, limit + 1)
    while prime_number < limit / 2 + 1:
        totients[2 * prime_number::prime_number] -= list(range(1, int(limit / prime_number)))
        for old_prime in primes:
            if 2 * old_prime * prime_number > limit/2 + 1:
                break
            totients[2 * old_prime * prime_number::old_prime * prime_number] += list(
                range(1, int(limit / (old_prime * prime_number))))
        primes.append(prime_number)
        prime_number = next(png)
    return totients - 1


def relative_prime_sieve(number):
    # Not necessary but just for fun
    relative_primes = [1] * number
    relative_primes[-1] = 0
    for i in range(0, number - 2):
        if relative_primes[i + 1] == 0:
            continue
        if number % (i + 2) == 0:
            relative_primes[i + 1::(i + 2)] = [0] * int(number / (i + 2))
    return sum(relative_primes)
