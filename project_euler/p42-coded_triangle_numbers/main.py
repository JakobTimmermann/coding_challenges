import os
import sys
from itertools import permutations

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import triangle_number_generator, is_triangle_word

with open("p042_words.txt","r") as file:
    words = file.read()
words = words.split(",")



def get_triangle_numbers(limit):
    triangle_numbers_up_to_limit = []
    tng = triangle_number_generator()
    triangle_number = next(tng)
    while triangle_number < limit:
        triangle_numbers_up_to_limit.append(triangle_number)
        triangle_number = next(tng)
    return triangle_numbers_up_to_limit


longest_word = max(words, key=len)
largest_possible_triangle_number = len(longest_word) * ord("Z")
triangle_numbers = get_triangle_numbers(largest_possible_triangle_number + 1)

number_of_triangle_words = 0
for word in words:
    if is_triangle_word(word, triangle_numbers):
        number_of_triangle_words += 1

print(number_of_triangle_words)