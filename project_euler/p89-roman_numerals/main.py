def to_roman(val):
    symbols = {"M":1000,"CM":900, "D":500,"CD":400, "C":100,"XC":90, "L":50,"XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
    output = ""
    for s,n in symbols.items():
        for i in range(int(val/n)):
            output += s
            val -= n
    return output


def from_roman(roman_num):
    symbols = {"CM":900, "CD":400, "XC":90, "XL":40, "IX":9, "IV":4, "M":1000, "D":500,"C":100,"L":50,"X":10, "V":5, "I":1}
    val = 0
    for s,n in symbols.items():
        val += roman_num.count(s) * n
        roman_num = roman_num.replace(s,'')
    return val

with open("roman.txt", "r") as file:
    numbers = file.readlines()

old_number_of_chars = sum([len(a.strip()) for a in numbers])
new_numbers = [to_roman(from_roman(a.strip())) for a in numbers]
new_number_of_chars = sum([len(a.strip()) for a in new_numbers])
print(f"Number of chars in old style: {old_number_of_chars}")
print(f"Number of chars in old style: {new_number_of_chars}")
print(f"Difference: {old_number_of_chars-new_number_of_chars}")