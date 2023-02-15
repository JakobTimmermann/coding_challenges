import os
import sys

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import isPalindrome

palindrom_sum = 0
for number in range(1,1_000_000):
    binary_number = "{0:b}".format(number).lstrip()
    if isPalindrome(str(number)) and isPalindrome(binary_number):
        palindrom_sum += number

print(f"Sum of all numbers, less than one million, which are palindromic in base 10 and base 2 is {palindrom_sum}")
