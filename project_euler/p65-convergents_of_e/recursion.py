from fractions import Fraction
import sys

sys.setrecursionlimit(2000)


def nth_continued_fraction(n: list):
    if len(n) == 1:
        return 1/n[0]
    return 1 / (n[0] + nth_continued_fraction(n[1:]))


def e_series_generator():
    k = 1
    l = 0
    n = [2, 1]
    while True:
        yield n
        if l == 0:
            n.append(k*2)
            k += 1
            l += 1
        elif l == 2:
            l = 0
            n.append(1)
        else:
            l += 1
            n.append(1)

e_series = [2, 1]
k = 1
l = 0
for _ in range(98):
    if l == 0:
        e_series.append(k*2)
        k += 1
        l += 1
    elif l == 2:
        l = 0
        e_series.append(1)
    else:
        l += 1
        e_series.append(1)
print(len(e_series))

# Does only work for small fractions!
x = 1/nth_continued_fraction(e_series)
print(Fraction(x).limit_denominator())