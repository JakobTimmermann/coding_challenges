import os
import sys
from itertools import permutations

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_number_generator


def generate_all_four_digit_primes():
    png = prime_number_generator()
    collection_of_four_digital_primes = []
    prime = next(png)
    while prime < 10000:
        if prime > 999:
            collection_of_four_digital_primes.append(prime)
        prime = next(png)
    return collection_of_four_digital_primes


def check_permutations(n1, n2, n3):
    sn1 = sorted(list(str(n1)))
    sn2 = sorted(list(str(n2)))
    sn3 = sorted(list(str(n3)))
    return sn1 == sn2 == sn3


four_digit_primes = generate_all_four_digit_primes()
idx = 0
searching = True
while idx < len(four_digit_primes) and searching:
    first_prime = four_digit_primes[idx]
    for second_prime in four_digit_primes[idx+1:]:
        difference_to_next_prime = second_prime - first_prime
        third_number = second_prime + difference_to_next_prime
        if third_number > 9999:
            break
        if check_permutations(first_prime, second_prime, third_number) and third_number in four_digit_primes:
            print("".join([str(n) for n in [first_prime, second_prime, third_number]]))
            searching = True
            break
    idx += 1


