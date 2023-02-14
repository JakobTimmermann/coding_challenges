def get_power_digit(a, b, c = None, d= None, e = None, f = None, g = None):
    number = a ** pot + b ** pot
    digits = [a, b]
    for next_base in [c,d,e,f,g]:
        if next_base is not None:
            number += next_base ** pot
            digits.append(next_base)
    digits.sort()
    lnumber = [int(n) for n in str(number)]
    lnumber.sort()
    if digits == lnumber:
        return number
    return 0

sum_fifth_power = 0
pot = 5
c = d = e = f = g = None
for a in range(10):
    for b in range(a, 10):
        for c in range(b, 10):
            sum_fifth_power += get_power_digit(a, b, c)
            for d in range(c, 10):
                sum_fifth_power += get_power_digit(a, b, c, d)
                for e in range(d, 10):
                    sum_fifth_power += get_power_digit(a, b, c, d, e)
                    for f in range(e, 10):
                        sum_fifth_power += get_power_digit(a, b, c, d, e, f)

print(sum_fifth_power)