"""
Much more intelligent way to solve this respectively the only way to solve it in appropriate time
https://blog.dreamshire.com/project-euler-145/
and
https://www.educative.io/answers/projecteuler-145-how-many-reversible-numbers-are-below-1-million
"""

n = 9  # Limit is expressed as 10^n
reversible_numbers_count = 0

for n in range(2, n + 1):
    if n % 2 == 0:
        reversible_numbers_count += 20 * 30 ** (n // 2 - 1)
    elif n % 4 == 3:
        reversible_numbers_count += 100 * 500 ** (n // 4)

print(reversible_numbers_count)
