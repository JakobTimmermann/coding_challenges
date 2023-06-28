"""
This brute force approach takes way, way, way too much time
"""


def is_reversible(number):
    str_number = str(number)
    if str_number[-1] == '0':
        return False
    result = str(int(str_number) + int(str_number[::-1]))
    for digit in [int(d) for d in result]:
        if not digit % 2 or digit == 0:
            return False
    return True


count = 0
i = 1
# Only check odd numbers and increase count by two (36 and 63)
for number in range(1, 1_000_000, 2):
    if is_reversible(number):
        count += 2
print(f"Result: {count}")
