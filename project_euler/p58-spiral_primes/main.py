import os
import sys
from itertools import combinations

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import is_prime

def get_next_layer_spiral_numbers(spiral_numbers=[1], seperator=1):
    number = spiral_numbers[-1]
    new_spiral_numbers = []
    for _ in range(4):
        number += seperator + 1
        new_spiral_numbers.append(number)
    return new_spiral_numbers


def extract_number_of_primes(spiral_numbers):
    number_of_primes = 0
    for number in spiral_numbers:
        if is_prime(number, include_one=False):
            number_of_primes += 1
    return number_of_primes


spiral_numbers = [1]
seperator = 1
current_number_of_primes = 0
while True:
    new_spiral_numbers = get_next_layer_spiral_numbers(spiral_numbers, seperator)
    current_number_of_primes += extract_number_of_primes(new_spiral_numbers)
    spiral_numbers += new_spiral_numbers
    seperator += 2
    if current_number_of_primes/len(spiral_numbers) < 0.1:
        break
print(spiral_numbers)
print(current_number_of_primes, len(spiral_numbers))
print(current_number_of_primes/len(spiral_numbers))
# Seperator itself is already the spiral length. Seperator = 1 + 2 * layer == side length
print(f"Side length of the square spiral with ratio of primes along both diagonals below 10% {seperator}")
