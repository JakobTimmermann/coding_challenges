

def is_digit_cancelling_fraction(numerator, denominator):
    numerator_list = sorted([int(n) for n in list(str(numerator))])
    denominator_list = sorted([int(n) for n in list(str(denominator))])
    if (len(set(numerator_list)) != len(numerator_list)) or (len(set(denominator_list)) != len(denominator_list)):
        return False
    if numerator_list == denominator_list:
        return False
    if 0 in numerator_list or 0 in denominator_list:
        return False
    for num in numerator_list:
        if num in denominator_list:
            numerator_list.remove(num)
            denominator_list.remove(num)
    if len(denominator_list) == 2:
        return False
    return numerator_list[0]/denominator_list[0]== numerator/denominator


product_of_curios_fractions = 1
for n in range(10, 100):
    for d in range(n, 100):
        if is_digit_cancelling_fraction(n, d):
            product_of_curios_fractions *= n/d
print(product_of_curios_fractions)

