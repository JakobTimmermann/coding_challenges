from decimal import getcontext, Decimal
getcontext().prec = 102

perfect_squares = []
n = 1
while n ** 2 < 101:
    perfect_squares.append(n ** 2)
    n += 1

total_sum = 0
for number in range(2, 100):
    if number in perfect_squares:
        continue
    sroot = Decimal(number).sqrt()
    total_sum += int(sroot) + sum([int(i) for i in list(str(sroot).split('.')[-1])][:99])

print(f"Total of the digital sums of the first one hundred decimal digits for all the irrational square roots below "
      f"100: {total_sum}")