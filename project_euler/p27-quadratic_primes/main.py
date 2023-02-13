import os
import sys

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../utils/'))

from project_euler_utils import is_prime, prime_number_generator


def check_consecutive_primes(a, b):
    number_of_consecutive_primes = -1
    number = b
    n = 0
    while is_prime(number):
        if number < 0:
            break
        number = n**2 + a * n + b
        n += 1
        number_of_consecutive_primes += 1
    return number_of_consecutive_primes


def main():
    result = [0, 0]
    max_consecutive_primes = 0
    for a in range(-999, 999, 2):
        pg = prime_number_generator()
        b = next(pg)
        while b < 1000:
            current_consecutive_primes = check_consecutive_primes(a, b)
            if current_consecutive_primes > max_consecutive_primes:
                max_consecutive_primes = current_consecutive_primes
                result = [a, b]
            b = next(pg)
    print(result[0] * result[1], result, max_consecutive_primes)
    return result[0] * result[1]


main()
