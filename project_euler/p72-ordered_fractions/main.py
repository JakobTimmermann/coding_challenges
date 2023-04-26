def find_fraction_closest_to_target(denominator, target):
    current_numerator = denominator
    left = 0
    right = denominator
    counter = 0
    while left + 2 < right:
        current_numerator = left + int((right - left) / 2)
        if current_numerator / denominator > target:
            right = current_numerator
        else:
            left = current_numerator
        counter += 1
    return current_numerator


closest_diff = float("inf")
closest_numerator = 0
closest_denominator = 0
for number in range(8, 1_000_000):
    numerator = find_fraction_closest_to_target(number, 3 / 7)
    while numerator / number < 3 / 7:
        numerator += 1
    while numerator / number > 3 / 7:
        numerator -= 1
    current_diff = 3 / 7 - numerator / number
    if not (numerator % 3 == 0 and number % 7 == 0) and current_diff < closest_diff:
        closest_numerator = numerator
        closest_denominator = number
        closest_diff = 3 / 7 - numerator / number

print(f"Fraction immediately to the left of 3/7: {closest_numerator} / {closest_denominator}")
