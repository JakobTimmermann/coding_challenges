def relative_prime_sieve(number ):
    # Not necessary but just for fun
    relative_primes = [1] * number
    relative_primes[-1] = 0
    for i in range(0, number-2):
        if relative_primes[i+1] == 0:
            continue
        if number % (i+2) == 0:
            relative_primes[i+1::(i+2)] = [0] * int(number/(i+2))
    return sum(relative_primes)


def is_permutation(number_one, number_two):
    if set(str(number_one)) != set(str(number_two)):
        return False
    return sorted(list(str(number_one))) == sorted(list(str(number_two)))

relative_prime_sieve(10)
#ratio = 1
#number = 87109
#for number in range(20000, 100000):
#    totient_number = relative_prime_sieve(number)
#    if is_permutation(number, totient_number):
#        new_ratio = totient_number/number
#        print(new_ratio,number)
#        if new_ratio < ratio:
#            print(number)
#            ratio = new_ratio
#            result = number
#
#print(ratio, result)
