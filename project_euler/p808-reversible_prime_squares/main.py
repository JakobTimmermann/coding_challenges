import os
import sys

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import is_palindrome_number, prime_number_generator

squares = {}
png = prime_number_generator()


def reverse_number(number):
    return int(str(number)[::-1])

count = 0
sum_of_reversible_prime_squares = 0

while count < 50:
    squared_prime_number = next(png)**2
    if is_palindrome_number(squared_prime_number):
        continue
    r_number = reverse_number(squared_prime_number)
    squares[squared_prime_number] = False
    if r_number in squares:
        squares[r_number] = True
        squares[squared_prime_number] = True
        count += 2
        sum_of_reversible_prime_squares += r_number + squared_prime_number
        print(count)
        print(r_number)

print(sum_of_reversible_prime_squares)



