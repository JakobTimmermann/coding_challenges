import numpy as np
bases = []
exponents = []
with open("base_exp.txt") as file:
    lines = file.readlines()
for l in lines:
    l.strip()
    base, exponent = l.split(',')
    bases.append(int(base))
    exponents.append(int(exponent))

exponents = np.array([exponents])/max(exponents)
print(f"Line number with greatest numerical value {np.argmax(np.power(bases, exponents)) + 1}")