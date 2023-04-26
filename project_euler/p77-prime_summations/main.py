import os
import sys

import numpy as np

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_number_generator, number_of_summations

primes = []
png = prime_number_generator()
for _ in range(10_000):
    primes.append(next(png))
primes = np.array(primes)

number_of_ways = 0
number = 1
while number_of_ways < 5000:
    number_of_ways = number_of_summations(number, primes[primes < number])
    number += 1
print(
    f"First value which can be written as the sum of primes in over five thousand different ways:"
    f" {number - 1} with {number_of_summations(number - 1, primes[primes < number - 1])} ways")
