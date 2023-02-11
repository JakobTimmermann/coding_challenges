from math import log10
def fibonacci_generator():
    f1 = 1
    f2 = 1
    while True:
        yield f1
        f1, f2 = f2, f1 + f2

fib_seq = fibonacci_generator()

idx = 1 # Fibonacci Sequence starts at F1 = 1
fibN = next(fib_seq)
len_fibN = int(1 + log10(fibN))
while len_fibN < 1000:
    fibN = next(fib_seq)
    len_fibN = int(1 + log10(fibN))
    idx += 1

print(idx)
