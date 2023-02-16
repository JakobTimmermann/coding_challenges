import os
import sys
from itertools import permutations

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import is_pentagon_number

searching = True
i = 0
while searching:
    pi = int(i * (3 * i - 1) / 2)
    for j in range(1, i):
        pj = int(j * (3 * j - 1) / 2)

        if is_pentagon_number(pi + pj) and is_pentagon_number(pi - pj):
            print(f"Solution for pentagon numbers problem: {pi - pj}")
            break
    i += 1

