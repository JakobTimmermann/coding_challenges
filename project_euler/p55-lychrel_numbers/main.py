import os
import sys

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import is_palindrome_number


def is_lychel_number(number):
    reverse_number = int(str(number)[::-1])
    current_number = number + reverse_number
    for _ in range(50):
        if is_palindrome_number(current_number):
            return False
        reverse_number = int(str(current_number)[::-1])
        current_number = current_number + reverse_number
    return True


lychel_numbers = []
for number in range(10,10_001):
    if is_lychel_number(number):
        lychel_numbers.append(number)
print(f"How many Lychrel numbers are there below ten-thousand? {len(lychel_numbers)}")


