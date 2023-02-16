import os
import sys
from itertools import permutations

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import convert_list_to_number

# pandigitals of length 9 and 8 are both divisible by 3

def is_sub_divisible(number):
    number_str = str(number)
    for idx, div in enumerate([2, 3, 5, 7, 11, 13, 17]):
        sub_string = number_str[idx+1:idx+4]
        if int(sub_string) % div != 0:
            return False
    return True


sum_of_divisible_numbers = 0
for per9 in permutations(range(0, 10)):
    per9 = convert_list_to_number(per9)
    if is_sub_divisible(per9):
        sum_of_divisible_numbers += per9
print(is_sub_divisible(1406357289))
print(f"The sum of all 0 to 9 pandigital numbers with divisible sub-strings is {sum_of_divisible_numbers}")