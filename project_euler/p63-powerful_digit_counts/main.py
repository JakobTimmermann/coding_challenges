def get_powerful_digit(digit):
    base = 1
    number = base**digit
    count = 0
    while len(str(number)) < digit + 1:
        if len(str(number)) == digit:
            count += 1
        base += 1
        number = base**digit
    return count


powerful_digits = 0
for digit in range(1000):
    powerful_digits += get_powerful_digit(digit)

print(f"Number of n-digit positive integers which are also an nth power: {powerful_digits}")
