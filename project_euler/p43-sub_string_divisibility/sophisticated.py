# https://www.xarg.org/puzzle/project-euler/problem-43/
print("d6 must be 5")
print("d6d7d8 must be divisible by 11 --> d6d7d8 can be: {506,517,528,539,561,572,583,594}")
print("d7d8d9 must be divisible by 13 --> d6d7d8d9 can only be: {5286,5390,5728,5832}")
print("d8d9d10 must be divisble by 17 --> d6d7d8d9d10 can only be: {52867,53901,57289}")

def determining_d5d6d7():
    d6d7 = ['52', '53', '57']
    divisor = 7
    possible_numbers = []
    for d5 in range(1, 10):
        for tail in d6d7:
            if d5 not in [int(k) for k in list(tail)]:
                number = str(d5) + tail
                if int(number) % divisor == 0:
                    possible_numbers.append(number)
    return possible_numbers

print(f"\nWith determining_d5d6d7 via brute force d5d6d7 can only be {' or '.join(determining_d5d6d7())}")
print("Accordingly we get --> d5d6d7d8d9d10 can only be {952867,357289}")

def determining_d3tod10():
    tail = {
            9: [5, 2, 8, 6, 7],
            3: [5, 7, 2, 8, 9],
            }
    possible_numbers = []
    for d3 in [0, 1, 3, 4, 6, 9]: #
        for d4 in [0, 4, 6]: # d4 must be even
            if d4 == d3:
                continue
            for d5 in tail.keys():
                if d5 == d3 or d5 == d4:
                    continue
                if d3 not in tail[d5] and d4 not in tail[d5]:
                    number_str = "".join(str(n) for n in [d3, d4, d5])
                    if int(number_str) % 3 == 0:
                        possible_numbers.append(number_str)
    return possible_numbers

print(f"\nFor d3d4d5 we obtain {', '.join(determining_d3tod10())}")
print("Which for d3-d10 leaves us with {06357289, 30952867, 60357289}")
print("For d1 and d2 we have no restrictions leaving us with all combinations with 1 and 4")


def solution():
    return 1430952867 + 1460357289 + 1406357289 + 4130952867 + 4160357289 + 4106357289;


print(f"\n---\nThe solution then is {solution()}")