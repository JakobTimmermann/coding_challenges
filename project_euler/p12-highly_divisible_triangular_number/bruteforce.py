from math import sqrt
from itertools import count


def count_factors(num):
    """Return the number of factors of `num`"""
    sum_ = 0
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            sum_ += 2
    if int(sqrt(num))**2 == num:
        sum_ -= 1
    return sum_

def triangular_nums():
    """Yield the triangular numbers"""
    t = 0
    for i in count():
        t += i
        yield t

def main():
    for triNum in triangular_nums():
        if count_factors(triNum) > 500:
            return triNum

if __name__ == "__main__":
    ans = main()
    if ans is not None:
        print(ans)
