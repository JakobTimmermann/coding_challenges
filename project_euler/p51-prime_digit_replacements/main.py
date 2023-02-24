import os
import sys
from itertools import combinations

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_number_generator, is_prime


def determine_how_many_primes(number_str, char_to_replace='x'):
    number_of_primes = 0
    for i in range(10):
        number = int(number_str.replace(char_to_replace, str(i)))
        if number > 10**(len(number_str)-1) and is_prime(number):
            number_of_primes += 1
    return number_of_primes


def generate_valid_number_str(real_digits, number_of_placeholder):
    number_length = len(real_digits) + number_of_placeholder
    possible_combinations = combinations(range(number_length), number_of_placeholder)
    valid_permutations = []
    for comb in possible_combinations:
        number_list = []
        i = 0
        for idx in range(number_length):
            if idx in comb:
                number_list.append('x')
            else:
                number_list.append(str(real_digits[i]))
                i += 1
        valid_permutations.append("".join(number_list))
    return valid_permutations


def main():
    max_length = 0
    for i in range(10):
        for k in range(10):
            for j in range(10):
                for number in generate_valid_number_str([i, j, k], 3):
                    current_length = determine_how_many_primes(number, 'x')
                    max_length = max(max_length, current_length)
                    if max_length == 8:
                        return number


number = main()
print(f"Number with 8 primes: {number}")
print(f"Is 121313 a prime? {is_prime(121313)}")
