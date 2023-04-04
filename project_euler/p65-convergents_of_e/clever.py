# The numerator, n, for the continued fraction follows a predictable pattern (1, 2, 3, 8, 11, 19, 87, …)
# and we are exploiting that to solve this problem:
#       n_i = m_i * n_(i-1) + n_(i-2)
# where n_0 = 1 and n_1 = 2
# and the multiplier m follows the infinite continued fraction [2, 1, 2, 1, 1, 4 ...]

def numerator_generator():
    i = 2
    ni = 1
    nj = 2
    while True:
        yield ni
        nj, ni = (1 if i%3 else 2*i//3) * nj + ni, nj
        i += 1


ng = numerator_generator()
for _ in range(101):
    numerator = next(ng)

print(f"Sum of digits in the numerator of the 100th convergent of the continued fraction for the euler number: {sum([int(a) for a in str(numerator)])}")

