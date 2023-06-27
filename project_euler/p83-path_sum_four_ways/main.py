from urllib.request import urlopen

import networkx as nx

file_url = 'https://projecteuler.net/project/resources/p082_matrix.txt'
with urlopen(file_url) as f:
    matrix = [list(map(int, row.decode('utf-8').split(','))) for row in f.readlines()]
n, m = len(matrix), len(matrix[0])

G = nx.DiGraph()
for i in range(n):
    for j in range(m):
        neighbors = [(i + x, j + y) for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)] if 0 <= i + x < n and 0 <= j + y < m]
        for ix, jy in neighbors:
            G.add_edge((i, j), (ix, jy), weight=matrix[ix][jy])

path_length = nx.dijkstra_path_length(G, source=(0, 0), target=(n - 1, m - 1))
print(
    f"Minimal path sum from the top left to the bottom right by moving left, right, up, and down: {path_length + matrix[0][0]}")
