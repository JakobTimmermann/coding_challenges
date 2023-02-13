from itertools import permutations

perm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for k in range(1_000_000):
    x = next(perm)
print(''.join([str(num) for num in x]))


# #### Using own functions #########
# def getPermutations(array):
#     output = []
#     getPermutationsHelper(array, [], output)
#     return output
#
#
# def getPermutationsHelper(array, perm, output):
#     if not len(array) and len(perm):
#         output.append(perm)
#     else:
#         for j in range(len(array)):
#             new_perm = perm + [array[j]]
#             new_array = array.copy()
#             new_array.pop(j)
#             getPermutationsHelper(new_array, new_perm, output)
#
#
# perm = getPermutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(''.join([str(num) for num in perm[1_000_000]]))
