import os
import sys

current_folder = os.path.dirname(__file__)

sys.path.append(os.path.join(current_folder, '../../'))

from utils import *


def get_figurative_numbers_for_n(n):
    return (3, n * (n + 1) / 2), (4, n * n), (5, n * (3 * n - 1) / 2), (6, n * (2 * n - 1)), (7, n * (5 * n - 3) / 2), (
    8, n * (3 * n - 2))


def get_all_figurative_numbers():
    figurative_numbers = []
    n = 19
    fn = get_figurative_numbers_for_n(n)
    while not all([number > 9999 for type, number in fn]):
        for order, number in fn:
            if 999 < number < 10000 and number % 100 > 9:  # Make sure nothing like 1201 is included!
                figurative_numbers.append((order, number))
        n += 1
        fn = get_figurative_numbers_for_n(n)
    return figurative_numbers


def build_list_of_connections(numbers):
    connections = {}
    for ord1, n1 in numbers:
        for ord2, n2 in numbers:
            if ord1 != ord2 and n1 % 100 == n2 // 100:
                connections[(ord1, n1)] = connections.get((ord1, n1), []) + [(ord2, n2)]
    return connections


def cascade_numbers(connections, orders, numbers):
    if len(orders) == 6 and (numbers[0] // 100 == numbers[-1] % 100):
        # print(orders, numbers)
        print(f"Solution for problem 61 (cyclical figurate numbers): {int(sum(numbers))}")
        return orders, numbers
    for order, number in connections.get((orders[-1], numbers[-1]), []):
        if order not in orders:
            return cascade_numbers(connections, orders + [order], numbers + [number])


available_numbers = get_all_figurative_numbers()
connections = build_list_of_connections(available_numbers)
for order, number in connections:
    result = cascade_numbers(connections, [order], [number])
