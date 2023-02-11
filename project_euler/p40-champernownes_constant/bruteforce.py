number = 1
dn = '0'
while len(dn) < 1_000_001:
    dn += str(number)
    number += 1

prod = 1
for k in range(6):
    print(10**k)
    prod *= int(dn[10**k])
print(prod)
