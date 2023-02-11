# Taken from https://www.youtube.com/watch?v=rw4s4M3hFfs

gyms = [False, False, False, False, True, False, False, True]
stores = [False, True, False, False, False, False, False, False]
schools = [True, False, False, False, True, False, False, False]

#gyms = [False, True, True, False, False]
#stores = [False, False, False, False, True]
#schools = [True, False, True, True, True]

gyms_walking_distance = [float("inf")] * len(gyms)
stores_walking_distance = [float("inf")] * len(gyms)
schools_walking_distance = [float("inf")] * len(gyms)


def measure_walking_distance_one_way(array, walking_distance):
    measuring = False
    for idx,k in enumerate(array):
        if k == True:
            measuring = True
            walking_distance[idx] = 0
            continue
        if measuring == True:
            walking_distance[idx] = min(walking_distance[idx], walking_distance[idx-1] + 1)


def measure_walking_distance(array, walking_distance):
    measure_walking_distance_one_way(array, walking_distance)
    walking_distance = walking_distance[::-1]
    array = array[::-1]
    measure_walking_distance_one_way(array, walking_distance)
    walking_distance = walking_distance[::-1]
    array = array[::-1]
    return walking_distance


gyms_walking_distance = measure_walking_distance(gyms, gyms_walking_distance)
schools_walking_distance = measure_walking_distance(schools, schools_walking_distance)
stores_walking_distance = measure_walking_distance(stores, stores_walking_distance)


def get_max_distance_for_block(schools_walking_distance, gyms_walking_distance,stores_walking_distance):
    idx = 0
    min_max_idx = 0
    min_max_distance = float("inf")
    for i,j,k in zip(schools_walking_distance, gyms_walking_distance,stores_walking_distance):
        max_distance = max(i,j,k)
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            min_max_idx = idx
        idx += 1
    return min_max_idx

best_block = get_max_distance_for_block(schools_walking_distance, gyms_walking_distance,stores_walking_distance)

print(f"Best appartement located in block {best_block}")





