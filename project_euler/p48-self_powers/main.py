import numpy as np


def get_last_digits(base: int, digit_limit: int):
    last_digits = [base] + [0] * (digit_limit - 1)
    for pot in range(0, base - 1):
        carry = 0
        for idx, d in enumerate(last_digits):
            result = d * base + carry
            value = result % 10
            carry = result // 10
            last_digits[idx] = value
    return np.array(last_digits)


def add_two_lists(list1, list2):
    merged_list = [0] * len(list1)
    carry = 0
    for idx in range(len(list1)):
        result = list1[idx] + list2[idx] + carry
        value = result % 10
        carry = result // 10
        merged_list[idx] = value

    return merged_list


current_last_digits = [0] * 10
for i in range(1, 1001):
    next_term_digits = get_last_digits(i, 10)
    current_last_digits = add_two_lists(current_last_digits, next_term_digits)

print(f"The last 10 digits of 1**2 + 2**2 + 3**3 ... 1000**1000 is {''.join([str(n) for n in current_last_digits[::-1]])}")