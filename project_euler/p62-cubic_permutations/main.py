NUMBER_OF_PERMUTATIONS = 5

cube_sets = {}
max_set_length = 0
n = 300
while max_set_length != NUMBER_OF_PERMUTATIONS:
    cube = n**3
    sorted_cube = ''.join(sorted(str(cube)))
    cube_sets[sorted_cube] = cube_sets.get(sorted_cube, []) + [cube]
    max_set_length = max(max_set_length, len(cube_sets[sorted_cube]))
    if max_set_length == NUMBER_OF_PERMUTATIONS:
        break
    n += 1

print(f"Smallest cube for which exactly five permutations of its digits are cube: {cube_sets[sorted_cube][0]}")
