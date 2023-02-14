import os
import sys
import math

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import prime_factor_generator

radicals = {}
for k in range(1, 100_001):
    div_k = 1
    for prime in set(prime_factor_generator(k)):
        div_k *= prime
    radicals[k] = div_k

sorted_radicals = sorted(radicals.items(), key=lambda x:x[1])
print(sorted_radicals[9999])
