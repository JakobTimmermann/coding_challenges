import os
import sys

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_number_generator


def relative_prime_sieve(number):
    # Not necessary but just for fun
    relative_primes = [1] * number
    relative_primes[-1] = 0
    for i in range(0, number-2):
        if relative_primes[i+1] == 0:
            continue
        if number % (i+2) == 0:
            relative_primes[i+1::(i+2)] = [0] * int(number/(i+2))
    return sum(relative_primes)


# In general the number with the most distinct prime factors will have the least number of remaining relative primes
# Hence we will just multiply prime numbers and max them out
number = 1
png = prime_number_generator()
while number < 1_000_000:
    prime = next(png)
    number *= prime
number/= prime

print(f"Solution for problem 69: Totient Maximum:{int(number)}")