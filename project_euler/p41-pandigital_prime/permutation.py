import os
import sys
from itertools import permutations

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_number_generator, is_prime, convert_list_to_number

# pandigitals of length 9 and 8 are both divisible by 3

pandigital_permutations = list(permutations(range(1, 8)))
for pandigital_list in pandigital_permutations[::-1]:
    pandigital_number = convert_list_to_number(pandigital_list)
    if is_prime(pandigital_number):
        break

print(f"The largest pandigital number is {pandigital_number}")

