"""
Right integer triangle Examples are:
a : b : c
3 : 4 : 5
5 : 12 : 13
8 : 15 : 17
(Primitive) triangles can be constructed via
a = m**2 - n**2
b = 2*m*n
c = m**2 + n**2
with m > n > 0
and have to be multiplied to yield all possible combinations
"""


def solution(max_length=300, search_range=1000):
    triangle_lengths = {}
    for n in range(1, search_range):
        for m in range(n + 1, search_range):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            k = 1
            triangle_length = k * (a + b + c)
            while triangle_length < max_length:
                if triangle_length not in triangle_lengths:
                    triangle_lengths[triangle_length] = set()
                triplet = tuple(sorted([k * a, k * b, k * c]))
                triangle_lengths[triangle_length].add(triplet)
                k += 1
                triangle_length = k * (a + b + c)

    triangle_lengths = {key: triangle_lengths[key] for key in sorted(triangle_lengths.keys())}
    return triangle_lengths


single_triangles_count = 0
right_integer_triangles = solution(max_length=1_500_000, search_range=1000)
for triangle_length, triplets in right_integer_triangles.items():
    if len(triplets) == 1:
        single_triangles_count += 1

print(f"Number of triangles with L <= 1_500_000 with exactly one integer triplet: {single_triangles_count}")
