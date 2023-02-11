arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
k = 4
import heapq


def kth_largest_value_sorting(arr, k):
    arr = sorted(arr, reverse=True)
    print(arr[k - 1])
    return arr[k - 1]


def kth_largest_heapq(array, k):
    array = [-element for element in array]
    heapq.heapify(array)
    for i in range(k - 1):
        heapq.heappop(array)
    return -heapq.heappop(array)


print(kth_largest_heapq(arr, k))
