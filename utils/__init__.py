from math import sqrt


def digit_sum(n):
    """Return the sum of the digits of `n`"""
    return sum(map(int, str(n)))


def prime_factor_generator(n):  # (cf. https://stackoverflow.com/a/15703327/849891)
    j = 2
    while n > 1:
        for i in range(j, int(sqrt(n + 0.05)) + 1):
            if n % i == 0:
                n //= i
                j = i
                yield i
                break
            else:
                if n > 1:
                    yield n
                    break


def is_prime(number_to_check, include_one=True, ascending_and_complete_prime_list=None):
    if number_to_check < 0:
        return False
    starting_number = 2
    if ascending_and_complete_prime_list:
        for prime in ascending_and_complete_prime_list:
            if prime < 2:
                continue
            if number_to_check % prime == 0:
                return False
            if prime > int(number_to_check ** 0.5) + 1:
                return True
        starting_number = max(ascending_and_complete_prime_list[-1], starting_number)
    for potential_divisor in range(starting_number, int(number_to_check ** 0.5) + 1):
        if number_to_check % potential_divisor == 0:
            return False
    return True if include_one else number_to_check > 1


def prime_number_generator():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def get_prime_factors(number, unique_factors=False):
    png = prime_number_generator()
    prime = next(png)
    prime_factors = []
    while number > 1:
        while number % prime == 0:
            prime_factors.append(prime)
            number /= prime
        prime = next(png)
    if unique_factors:
        prime_factors = list(set(prime_factors))
    return prime_factors


def get_factors(n, unique_factors=False):
    list_of_divisors = [1]
    for potential_divisor in range(2, int(n ** 0.5) + 1):
        if n % potential_divisor == 0:
            list_of_divisors.append(potential_divisor)
            list_of_divisors.append(int(n / potential_divisor))
    if unique_factors:
        list_of_divisors = list(set(list_of_divisors))
    return list_of_divisors


def fibonacci_generator():
    f1 = 0
    f2 = 1
    while True:
        yield f1
        f1, f2 = f2, f1 + f2


def is_palindrome(string):
    if len(string) < 2:
        return True
    return string[0] == string[-1] and is_palindrome(string[1:-1])


def is_palindrome_number(number: int):
    number_str = str(number)
    return is_palindrome(number_str)


def convert_list_to_number(number_list):
    number_str = "".join([str(n) for n in number_list])
    return int(number_str)


def pentagon_numbers_generator(n=1):
    while True:
        yield int(n * (3 * n - 1) / 2)
        n += 1


def is_pentagon_number(number_to_invest):
    #  3*n**2 - n - 2p = 0
    #  n = [1 +/- sqrt(1 + 24p)]/6
    # minus case is not valid because n will be negative
    n = (1 + sqrt(1 + 24 * number_to_invest)) / 6
    return n.is_integer()


def is_hexagonal_number(number_to_invest):
    #  2*n**2 - n - h = 0
    #  n = [1 +/- sqrt(1 + 8p)]/4
    # minus case is not valid because n will be negative
    n = (1 + sqrt(1 + 8 * number_to_invest)) / 4
    return n.is_integer()


def is_triangle_word(word, triangle_numbers):
    ord_list = [ord(char) - 64 for char in list(word)]
    return sum(ord_list) in triangle_numbers


def triangle_number_generator():
    n = 1
    while True:
        yield int(0.5 * n * (n + 1))
        n += 1


def pentagonal_number_generator():
    n = 1
    while True:
        yield int(0.5*(n * (3*n - 1)))
        n += 1


def hexagonal_number_generator():
    n = 1
    while True:
        yield int(n * (2*n - 1))
        n += 1


def heptagonal_number_generator():
    n = 1
    while True:
        yield int(0.5*(n * (5*n - 2)))
        n += 1


def octagonal_number_generator():
    n = 1
    while True:
        yield int(n * (3*n - 2))
        n += 1


