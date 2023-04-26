import os
import sys

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_number_generator, number_of_summations

print(f"Different ways one hundred can be written as a sum of at least two positive integers:"
      f" {number_of_summations(100, list(range(1, 100)))}")
