import os
import sys
from itertools import permutations

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_number_generator, is_prime


def is_valid_sliding_window(all_primes, window_width):
    start_idx = 0
    end_idx = window_width
    while end_idx < len(all_primes):
        summed_primes = sum(all_primes[start_idx:end_idx])
        if summed_primes > primes[-1]:
            start_idx += 1
            end_idx += 1
            continue
        if is_prime(summed_primes):
            print(f"Prime with most consecutive primes below one-million: {summed_primes}")
            return True
        start_idx += 1
        end_idx += 1
    return False

def determine_largest_possible_window(primes):
    sum_all_primes = 0
    idx = 0
    while sum_all_primes < primes[-1]:
        prime = primes[idx]
        sum_all_primes += prime
        idx += 1
    return idx


png = prime_number_generator()
prime = next(png)
primes = []
while prime < 1_000_000:
    primes.append(prime)
    prime = next(png)


max_length = determine_largest_possible_window(primes)

for window_width in reversed(range(max_length)):
    if is_valid_sliding_window(primes, window_width):
        print(f"Number of consecutive primes: {window_width}")
        break
        