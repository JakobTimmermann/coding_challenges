import os
import sys
from itertools import combinations

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_number_generator, is_prime


def is_prime_pair(p1, primes_to_compare_to , ascending_primes=None):
    for p2 in primes_to_compare_to:
        p1p2 = int(str(p1) + str(p2))
        p2p1 = int(str(p2) + str(p1))
        if not is_prime(p1p2, ascending_primes) or not is_prime(p2p1, ascending_primes):
            return False
    return True


pg = prime_number_generator()
primes_here = []
min_sum = float("inf")

for _ in range(1300):
    primes_here.append(next(pg))


def solution(primes):
    for a in primes:
        for b in primes:
            if b <= a:
                continue
            if is_prime_pair(a, [b], primes):
                for c in primes:
                    if c <= b:
                        continue
                    if is_prime_pair(c, [a, b], primes):
                        for d in primes:
                            if d <= c:
                                continue
                            if is_prime_pair(d, [a, b, c], primes):
                                for e in primes:
                                    if e <= d:
                                        continue
                                    if is_prime_pair(e, [a, b, c, d], primes):
                                        print(f"Found this set of primes: {a, b, c, d, e}")
                                        return a + b + c + d + e

print(f"We check all prime numbers up to {primes_here[-1]}")
prime_pair_sum = solution(primes_here)
print(f"The lowest sum for a set of five primes for which any two primes concatenate to produce another prime is {prime_pair_sum}.")