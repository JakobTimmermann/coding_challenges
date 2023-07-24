import math

limit = 2_000_000
x = 2
min_diff = float('inf')
y = limit // 6

while x <= y:
    diff = abs(x * (x + 1) * y * (y + 1) // 4 - limit)
    if diff < min_diff:
        area, min_diff, xx, yy = x * y, diff, x, y
    x += 2
    y = int(math.sqrt(limit * 4 / (x * x + x)))

print(f"Area of the {xx}x{yy}-grid that comes closest to 2_000_000: {area}.")