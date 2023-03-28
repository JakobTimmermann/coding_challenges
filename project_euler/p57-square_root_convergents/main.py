def square_root_convergence_denominator_generator():
    n0 = 1
    n1 = 2
    while True:
        yield n1
        n0, n1 = n1, 2*n1 + n0


def square_root_convergence_numerator_generator():
    n0 = 1
    n1 = 3
    while True:
        yield n1
        n0, n1 = n1, 2*n1 + n0


src_denoms = square_root_convergence_denominator_generator()
src_nums = square_root_convergence_numerator_generator()

number_of_fractions_with_larger_numerator = 0
for _ in range(1000):
    numerator = next(src_nums)
    denominator = next(src_denoms)
    if len(str(numerator)) > len(str(denominator)):
        number_of_fractions_with_larger_numerator += 1

print(f"Number of fractions containing a numerator with more digits than the denominator: {number_of_fractions_with_larger_numerator}")


