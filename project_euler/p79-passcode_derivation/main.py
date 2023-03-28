with open("keylog.txt") as file:
    key_logs = file.readlines()

key_logs = [int(key) for key in key_logs]


def is_part_of_password(password, key_log):
    idx = 0
    password = [int(p) for p in str(password)]
    key_log = [int(d) for d in str(key_log)]
    for number in password:
        if key_log[idx] == number:
            idx += 1
            if idx == 3:
                return True
    return False

for key in key_logs:
    if not is_part_of_password(73162890, key):
        print(":-(")
        print(key)