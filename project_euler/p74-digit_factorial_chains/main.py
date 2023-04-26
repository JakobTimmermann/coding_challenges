from math import factorial


def factorial_sum(number):
    factorial_of_digits = [factorial(int(n)) for n in str(number)]
    return sum(factorial_of_digits)


chains = {
    169: 3,
    1454: 3,
    363601: 3,
    871: 2,
    872: 2,
    45362: 2,
    45361: 2,
    145: 1
}

chains = {}
for number in range(1_000_000):
    current_loop = []
    current_number = number
    remaining_chain_length = 0
    while current_number not in current_loop:
        current_loop.append(current_number)
        current_number = factorial_sum(current_number)
        if current_number in chains:
            remaining_chain_length = chains[current_number]
            break
    for count, loop_number in enumerate(reversed(current_loop)):
        chains[loop_number] = count + remaining_chain_length + 1


count60 = 0
for count in chains.values():
    if count == 60:
        count60 += 1
print(f"Chains containing exactly sixty non-repeating terms with starting number below one million: {count60}")