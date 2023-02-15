# Possible digit length combinations are
# 1 x 4 = 4
# 2 x 3 = 4

def is_combined_pandigit(multiplicant, multiplier, product):
    combined_digits = str(multiplicant) + str(multiplier) + str(product)
    combined_digits = sorted(combined_digits)
    return combined_digits == ['1','2','3','4','5','6','7','8','9']


pandigit_produts = set()

for a in range(1, 10):
    for b in range(1000, 10000):
        product = a*b
        if is_combined_pandigit(a, b, product) and product not in pandigit_produts:
            pandigit_produts.add(product)

for a in range(10, 100):
    for b in range(100, 1000):
        product = a*b
        if is_combined_pandigit(a, b, product) and product not in pandigit_produts:
            pandigit_produts.add(product)

print(f"Sum of all pandigit numbers is {sum(pandigit_produts)}")



