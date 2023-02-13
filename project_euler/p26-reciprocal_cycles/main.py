import math

def find_recurring(denominator):
    seq_values = {
        "sub_num" : [],
        "sub_val" : [],
    }
    num = 1
    while True:
        while num < denominator:
            num *= 10
        sub_val = math.floor(num/denominator)
        sub_result = num - sub_val * denominator
        if sub_result == 0:
            break
        elif num in seq_values["sub_num"]:
            # cycle might not start with first digit e.g. 1/6 = 0.1(6)
            num_idx = seq_values["sub_num"].index(num)
            return "".join(str(n) for n in seq_values["sub_val"][num_idx:])
        seq_values["sub_num"].append(num)
        seq_values["sub_val"].append(sub_val)
        num = sub_result

#print(find_recurring(102))
max_length = 0
max_val = 0
for d in range(1,1001):
    reciprocal_cycle = find_recurring(d)
    reciprocal_cycle_length = (len(str(reciprocal_cycle)))
    if reciprocal_cycle_length > max_length:
        max_val = d
        max_length = reciprocal_cycle_length

print(max_length, max_val)