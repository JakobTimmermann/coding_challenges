import os
import sys

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import digit_sum

max_digit_sum = 0
for a in range(100):
    for b in range(100):
        max_digit_sum = max(max_digit_sum, digit_sum(a**b))

print(f"Solution for problem 56: {max_digit_sum}")
