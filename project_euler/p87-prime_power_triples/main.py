import itertools
import os
import sys

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_number_generator

primes = []
pg = prime_number_generator()
prime_power_triples = set()

for _ in range(1000):
    primes.append(next(pg))

for a, b, c in itertools.product(primes, primes[:250], primes[:150]):
    q = a ** 2 + b ** 3 + c ** 4

    if q < 50_000_000:
        prime_power_triples.add(q)

print(
    f"Numbers below fifty million that can be expressed as the sum of a prime square, prime cube, and prime fourth power: {len(prime_power_triples)}")
