import os
import sys
from itertools import permutations

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import is_prime


def is_goldbach_other_conjecture(number_to_invest, primes):
    current_number = 1
    idx = 1
    while current_number < number_to_invest:
        current_number = 2 * idx**2
        potential_prime = number_to_invest - current_number
        if is_prime(potential_prime, include_one=False, ascending_and_complete_prime_list=primes):
            return True
        idx += 1
    return False


rolling_primes = [2, 3, 5, 7]
number = 9
while True:
    if is_prime(number, rolling_primes):
        rolling_primes.append(number)
    elif not is_goldbach_other_conjecture(number, rolling_primes):
        print(number)
        break
    number += 2