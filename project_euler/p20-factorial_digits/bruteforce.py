### From: https://github.com/heanuea/Python-Fundamentals-/blob/master/04.Factorial%20digit%20sum.py
### And: https://codereview.stackexchange.com/questions/224452/project-euler-20-factorial-digit-sum-in-python
import os, sys

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '..'))

from utils import digit_sum

def factorial(n):
    x = n
    for i in range(1, n):
        x = x*(n-i)
    return x

f100 = factorial(100)
sumOfDigits = digit_sum(f100)


print("The sum of digits for factorial 100 is " +str(sumOfDigits))   # Prints answer 

