import os
import sys
from itertools import permutations

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import is_pentagon_number, is_hexagonal_number, triangle_number_generator

tng = triangle_number_generator()
triangle_number = next(tng)
triangle_number = next(tng) # Excluding 1 (which does not count)
searching = True
already_found_one = False
while searching:
    if is_pentagon_number(triangle_number) and is_hexagonal_number(triangle_number):
        if already_found_one:
            print(f"Solution for problem 45: {triangle_number}")
            searching = False
        else:
            already_found_one = True
    triangle_number = next(tng)

