limit = 100

numbers = set()
for a in range(2, limit + 1):
    for b in range(2, limit + 1):
        num = a**b
        if num not in numbers:
            numbers.add(num)

print(len(numbers))
