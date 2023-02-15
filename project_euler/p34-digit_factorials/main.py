from math import factorial


def factorial_sum(number):
    factorial_of_digits = [factorial(int(n)) for n in str(number)]
    return sum(factorial_of_digits)

sum_of_all_factorial_digits = 0
for i in range(3, 100000):
    if i == factorial_sum(i):
        sum_of_all_factorial_digits += i

print(sum_of_all_factorial_digits)