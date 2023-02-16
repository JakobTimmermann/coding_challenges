with open("p042_words.txt","r") as file:
    words = file.read()
words = words.split(",")


def is_triangle_word(word, triangle_numbers):
    ord_list = [ord(char) - 64 for char in list(word)]
    return sum(ord_list) in triangle_numbers


def triangle_number_generator():
    n = 1
    while True:
        yield int(0.5 * n * (n + 1))
        n += 1


def get_triangle_numbers(limit):
    triangle_numbers_up_to_limit = []
    tng = triangle_number_generator()
    triangle_number = next(tng)
    while triangle_number < limit:
        triangle_numbers_up_to_limit.append(triangle_number)
        triangle_number = next(tng)
    return triangle_numbers_up_to_limit


longest_word = max(words, key=len)
largest_possible_triangle_number = len(longest_word) * ord("Z")
triangle_numbers = get_triangle_numbers(largest_possible_triangle_number + 1)

number_of_triangle_words = 0
for word in words:
    if is_triangle_word(word, triangle_numbers):
        number_of_triangle_words += 1

print(number_of_triangle_words)