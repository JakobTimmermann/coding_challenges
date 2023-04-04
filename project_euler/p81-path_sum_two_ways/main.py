import numpy as np

#matrix = [
#    [131, 673, 234, 103, 18],
#    [201, 96, 342, 965, 150],
#    [630, 803, 746, 422, 111],
#    [537, 699, 487, 121, 956],
#    [805, 732, 524, 37, 331]
#]


def find_path_sum(matrix):
    matrix = np.array(matrix)
    for idx in range(len(matrix)):
        matrix[-1][idx] = sum(matrix[-1][idx:])
    matrix = matrix.transpose()
    for idx in range(len(matrix)):
        matrix[-1][idx] = sum(matrix[-1][idx:])
    matrix = matrix.transpose()
    for dim in reversed(range(len(matrix) - 1)):
        for idx in reversed(range(len(matrix) - 1)):
            matrix[dim][idx] += min(matrix[dim+1][idx], matrix[dim][idx+1])
    return matrix[0][0]


with open("matrix.txt", "r") as file:
    matrix = [list(map(int, row.split(','))) for row in file.readlines()]

print(f"Minimal path sum for matrix.txt: {find_path_sum(matrix)}")
