alphabet = "abcdefghijklmnopqrstuvwxyz"
with open("p022_names.txt", "r") as file:
    names = file.readline().split(",")
    names.sort()

names_score = 0
for idx, name in enumerate(names):
    name = name.lower()
    name_numbers = [ord(char) - 96 if char in alphabet else 0 for char in name]
    name_score = sum(name_numbers)
    names_score += (idx + 1) * name_score
print(names_score)
