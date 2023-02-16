import math
p = {}
for a in range(1, 1000):
    for b in range(a, 1000):
        c = math.sqrt(a**2 + b**2)
        if c.is_integer():
            c = int(c)
            sum_ = int(a + b + c)
            if sum_ <= 1000:
                if sum_ in p:
#                    p[sum_].append([a,b,c])
                    p[sum_] += 1
                else:
                    p[sum_] = 1
print(max(p, key=p.get))
print(p[840])
