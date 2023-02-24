# number has to have at least 6 digits
# Any number and its permutation always differ by a multiple of 9
def sorted_digits(number):
    number_str = str(number)
    return sorted(number_str)


current_number = 99999
while True:
    if sorted_digits(2*current_number) == sorted_digits(3*current_number) == sorted_digits(4*current_number) == sorted_digits(5*current_number) == sorted_digits(6*current_number):
        print(f"Solution for problem 52: {current_number}")
        break
    current_number += 9