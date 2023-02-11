# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
import os, sys
current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '..'))

from utils import  prime_number_generator

def get_rotations(n):
  rotations = set()
  for i in range( len( str(n) ) ):
    m = int( str(n)[i:] + str(n)[:i] )
    rotations.add(m)
  return rotations

def isprime(number, primes):
    for p in primes:
        if number % p == 0:
            return False
        if number < p * p:
            break
    return True

circular_primes = []
gp = prime_number_generator()
current_prime = next(gp)
primes = []

while current_prime < 1_000_000:
    rotations = get_rotations(current_prime)
    rotIsPrime = True
    for rot in rotations:
        if not isprime(rot, primes):
            rotIsPrime = False
            break
    if rotIsPrime:
        circular_primes.append(current_prime)
    primes.append(current_prime)
    current_prime = next(gp) 

print(len(circular_primes))
