# This is a brute force approach exploiting all the permutations
# Which still runs in sufficiently short time.
# For a more sophisticated approach: https://blog.dreamshire.com/project-euler-68-solution/

import itertools

gon_dimension = 5
numbers = range(1, gon_dimension * 2 + 1)
solutions = []
for outside_numbers in itertools.combinations(range(1, (gon_dimension * 2) + 1), gon_dimension):
    remaining_numbers = list(set(numbers) - set(outside_numbers))
    for inside_permutation in itertools.permutations(remaining_numbers):
        total = None
        all_the_same = True
        combinations = []
        inside_permutation = list(inside_permutation) + [inside_permutation[0]]
        for idx in range(5):
            combination = [outside_numbers[idx], inside_permutation[idx + 1], inside_permutation[idx]]
            if total is None:
                total = sum(combination)
                combinations.append(combination)
                continue
            if total != sum(combination):
                all_the_same = False
                break
            combinations.append(combination)

        if all_the_same:
            permutation = [combinations[0]] + sorted(combinations[1:], reverse=True)
            permutation = "".join(["".join([str(digit) for digit in comb]) for comb in permutation])
            if len(permutation) == 16:
                solutions.append(int(permutation))


print(f"Maximum 16-digit string for a 'magic' 5-gon ring: {max(solutions)}")