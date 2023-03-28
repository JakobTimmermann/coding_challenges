with open("triangle.txt") as file:
    triangle = file.readlines()

triangle = [[int(num) for num in line.strip().split()] for line in triangle]


def solution(triangle_file):
    while len(triangle_file) > 1:
        last_line = triangle_file.pop()
        for idx in range(1, len(last_line)):
            triangle_file[-1][idx - 1] += max(last_line[idx - 1], last_line[idx])
    print(f"The maximum path sum is: {triangle_file[-1][0]}")


solution(triangle)
