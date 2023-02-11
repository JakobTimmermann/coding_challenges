"""
See:
    https://www.xarg.org/puzzle/project-euler/problem-16/

The length L(n) of a number n is L(n)=[1+log(n)].
So in this case the length of the number is 
L(n) = [1 + log(2^1000)] = [1 + 1000 * log(2)] = 302

We then build a vector of length 302 and do primary school multiplication
The current_number will store the result in reverse
"""
from math import log10
pot = 1000

length_number = int(1 + pot * log10(2))
current_number = [0] * length_number
current_number[0] = 1
order = 0

for _ in range(pot):
    carry = 0
    for idx in range(0, order+1):
        digit = current_number[idx]
        product = digit * 2 + carry
        current_number[idx] = product % 10
        carry = product // 10
        if idx == order and carry > 0:
            order += 1
            current_number[order] = carry



