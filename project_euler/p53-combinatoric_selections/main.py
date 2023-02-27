from math import comb


def binary_search_approach(n, target):
    left = 0
    middle = int(n/2) - 1 + n%2
    current_comb = comb(n, middle)
    if current_comb < target:
        return 0
    right = middle
    while left < right:
        middle = (left + right) // 2
        current_comb = comb(n, middle)
        if current_comb < target:
            left = middle + 1
        elif current_comb > target:
            right = middle - 1
    return left if comb(n, left) > target else left + 1


target = 1_000_000
greater_than_target = 0
for n in range(2, 101):
    middle = int(n/2) - 1 + n%2
    r = binary_search_approach(n, target)
    if r:
        greater_than_target += (middle-r + 1) * 2 + 1 - n%2

print(f"Values greater than {target}: {greater_than_target}")