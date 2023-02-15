from math import sqrt


def digit_sum(n):
    """Return the sum of the digits of `n`"""
    return sum(map(int, str(n)))


def prime_factor_generator(n):    # (cf. https://stackoverflow.com/a/15703327/849891)
    j = 2
    while n > 1:
        for i in range(j, int(sqrt(n+0.05)) + 1):
            if n % i == 0:
                n //= i ; j = i
                yield i
                break
        else:
            if n > 1:
                yield n; break


def is_prime(number_to_check, include_one = True):
    if number_to_check < 0:
        return False
    for potential_divisor in range(2, int(number_to_check ** 0.5) + 1):
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


def get_divisors(n, unique_divisors=False):
    list_of_divisors = [1]
    for potential_divisor in range(2, int(n**0.5) + 1):
        if n % potential_divisor == 0:
            list_of_divisors.append(potential_divisor)
            list_of_divisors.append(int(n/potential_divisor))
    if unique_divisors:
        list_of_divisors = list(set(list_of_divisors))
    return list_of_divisors


def fibonacci_generator():
    f1 = 0
    f2 = 1
    while True:
        yield f1
        f1, f2 = f2, f1 + f2


def isPalindrome(string):
    if len(string) < 2:
        return True
    return string[0] == string[-1] and isPalindrome(string[1:-1]) 





