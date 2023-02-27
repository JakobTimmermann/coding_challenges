import time


def sort_digit_of_number(number_to_sort: int) -> int:
    return int(''.join(sorted(list(str(number_to_sort)))))


def is_happy_number(number_to_check):
    visited_numbers = set()
    current_number = number_to_check
    while True:
        if current_number in visited_numbers:
            return False
        if current_number == 1:
            return True
        visited_numbers.add(current_number)
        current_number = sum([int(digit)**2 for digit in str(current_number)])
        current_number = sort_digit_of_number(current_number)


t0 = time.time()
# At most we have 7 digits. The range of the sumsq of the digits will be [1,..., 567].
# The last number we obtain for 9_9999_999 i.e. 7 * 9**2 = 567.
# So first we calculate the chains for 1...567 storing the result in table[].
happy_number_look_up_table = {}
number_of_unhappy_numbers = 0

for sumsq in range(1, 568):
    if is_happy_number(sumsq):
        happy_number_look_up_table[sumsq] = True
    else:
        happy_number_look_up_table[sumsq] = False
        number_of_unhappy_numbers += 1

# Then we use this lookup table to speed up the calculation
target = 10_000_000
for remaining_number in range(568, target):
    sumsq = sum([int(digit)**2 for digit in str(remaining_number)])
    if not happy_number_look_up_table[sumsq]:
        number_of_unhappy_numbers += 1

t1 = time.time()

print(f"Solution of problem 92: {number_of_unhappy_numbers}\nTotal time {(t1-t0):.5f} sec")