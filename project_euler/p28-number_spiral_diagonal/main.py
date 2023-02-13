seperator = 1
spiral_diagonal_sum = 0
number = 1
idx = 0
while number < 1001*1001 + 1:
    spiral_diagonal_sum += number
    number += seperator + 1
    idx += 1
    if idx == 4:
        idx = 0
        seperator += 2

print(spiral_diagonal_sum)