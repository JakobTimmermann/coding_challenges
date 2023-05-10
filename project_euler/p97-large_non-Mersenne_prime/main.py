first_term = 28433
# Obviously calculating 28433 * 2^7830457 + 1 is not possible
# Fortunately, the pow module can calculate a number as a function of it's modulus.
# What we hence calculate is:
second_term = pow(base=2, exp=7830457, mod=10 ** 10)
# Where we only extract the last 10 digits via the modulus 10^10
third_term = 1

last_ten_digits = (first_term * second_term + third_term) % 10**10
print(f"Last ten digits of prime number 28433 * 2^7830457 + 1: {last_ten_digits}")
