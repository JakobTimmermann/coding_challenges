import os
import sys

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import *


def generate_all_numbers():
    trin = triangle_number_generator()
    pentn = pentagonal_number_generator()
    hexn = hexagonal_number_generator()
    hepn = heptagonal_number_generator()
    octn = octagonal_number_generator()

    all_numbers = {}
    for n in [trin, pentn, hexn, hepn, octn]:
        l = []
        for _ in range(10000):
            number = next(n)
            if len(str(number)) == 4:
                l.append(number)
            if len(str(number)) > 4:
                break
        all_numbers[n.__name__.split('_')[0]] = l

    all_numbers['squares'] = [n ** 2 for n in range(32, 100)]

    return all_numbers


def are_cyclic_numbers(numbers_str: list):
    number_str = numbers_str.pop()
    start_str = number_str[:2]
    end_str = number_str[2:]
    return connects_start_and_end(numbers_str, start_str, end_str)


def connects_start_and_end(numbers_str, start_str, end_str):
    if len(numbers_str) == 0 and start_str == end_str:
        return True
    for idx, number in enumerate(numbers_str):
        if number[:2] == end_str:
            end_str = number[2:]
            if connects_start_and_end([x for i, x in enumerate(numbers_str) if i != idx], start_str, end_str):
                return True
    return False


figurative_numbers = generate_all_numbers()

#for tri in figurative_numbers['triangle']:
#    for sq in figurative_numbers['squares']:
#        print(sq)
#        for pe in figurative_numbers['pentagonal']:
#            for hex in figurative_numbers['hexagonal']:
#                for hep in figurative_numbers['heptagonal']:
#                    for oct in figurative_numbers['octagonal']:
#                        if are_cyclic_numbers([str(tri), str(sq), str(pe), str(hex), str(hep), str(oct)]):
#                            print([tri, sq, pe, hex, hep, oct])
#                            break
