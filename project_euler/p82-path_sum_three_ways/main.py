import copy

import numpy as np

test_matrix = [
    [131, 673, 234, 303, 118],
    [10, 10, 10, 965, 150],
    [630, 803, 10, 422, 111],
    [537, 699, 10, 121, 956],
    [805, 732, 10, 10, 10]
]


def find_path_sum(matrix):
    # Algorithm is more tricky than I thought.
    # As usual, we work backwards!
    # For each row we first go from top to bottom (only considering down and right)
    # and then again from bottom to top (only considering up and right)
    # to determine the minimum path
    # The CRUCIAL thing is: since we loop from the top and from the bottom we also consider paths that move up
    # multiple steps in one col (compare test_matrix)
    matrix = np.array(matrix)
    cost = copy.deepcopy(matrix[:, -1])
    for col_idx in reversed(range(matrix.shape[1] - 1)):
        # In first loop from top to bottom, the top most element can only be reached via its element to the left
        cost[0] += matrix[0, col_idx]
        # Working our way closer to the start (remember: backwards) in the first loop each element at row_idx, col_idx
        # can be reached either by the element right or above them
        for row_idx in range(1, matrix.shape[0]):
            cost[row_idx] = matrix[row_idx, col_idx] + min(cost[row_idx], cost[row_idx - 1])
        # In the second loop we select the minimum value of the element itself (representing) the minimum of right/above
        # and the element below it.
        for row_idx in reversed(range(matrix.shape[0] - 1)):
            cost[row_idx] = min(matrix[row_idx, col_idx] + cost[row_idx + 1], cost[row_idx])
    return min(cost)


with open("matrix.txt", "r") as file:
    p82_matrix = [list(map(int, row.split(','))) for row in file.readlines()]

print(f"Minimal path sum for matrix.txt: {find_path_sum(p82_matrix)}")
