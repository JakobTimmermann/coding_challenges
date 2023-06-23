# We apply a generating functions that requires the generalized pentagonal numbers (OEIS A001318)
# https://en.wikipedia.org/wiki/Partition_(number_theory)#Generating_function
# https://oeis.org/A001318
pentagonal_numbers = sum([[i * (3 * i - 1) / 2, i * (3 * i - 1) / 2 + i] for i in range(1, 250)], [])
pentagonal_numbers = [int(pn) for pn in pentagonal_numbers]

p = [1]
signs = [1, 1, -1, -1]
n = 0
target = 1_000_000

# This approach does not collect the actual number of ways in which n coins can be separated into piles
# Instead it only collects the remainder when divided by target.
# This saves memory
while p[n] > 0:
    n += 1
    px, i = 0, 0
    while pentagonal_numbers[i] <= n:
        px += p[n - pentagonal_numbers[i]] * signs[i % 4]
        i += 1
    p.append(px % target)

print(f"The least value of p_n for which it is divisible by one million: {n}")
