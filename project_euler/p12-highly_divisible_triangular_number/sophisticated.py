
"""
See:
https://pythonandr.com/2015/09/01/highly-divisible-triangular-number-project-euler-problem-12/

First Step: Find the smallest number with 500 divisors. Seems like a good starting point to begin our search.

Second Step: Starting at the number found in the previous step, search for the next triangle number. 
Check to see whether this number has 500+ divisors. If yes, this is the number we were looking for, else…

Third Step: Check n for which ∑n = triangle number found in the previous step

Fourth Step: Add (n+1) to the last triangle number found, to find the next triangle number. 
Check whether this number has 500+ divisors. If yes, this number is the answer. If not, repeat Fourth Step till the process terminates.
"""

"""
FIRST STEP: Every integer N is the product of powers of prime numbers

N = p^α·q^β·…·r^γ
Where p, q, …, r are prime, while α, β, …, γ are positive integers. Such representation is unique up to the order of the prime factors.
If N is a power of a prime, N = p^α, then it has α + 1 factors:
1, p, …, p^(α-1), p^α
The total number of factors of N equals (α + 1)(β + 1) … (γ + 1)
---> 
500 = 2 x 2 x 5 x 5 x 5
So, the number in question should be of the form a·b·q^4·r^4·s^4 where a, b, q, r, s are primes that minimize this term. 
This is satisfied by 7·11·2^4·3^4·5^4 = 62370000. 
This is where we start our search for our magic number.
"""


from math import sqrt

# Function to calculate the number of divisors of integer n
def divisors(n):
    limit = int(sqrt(n))
    divisors_list = []
    for i in range(1, limit+1, 1):
        if n % i == 0:
            divisors_list.append(i)
            if i != n/i:
                divisors_list.append(n/i)
    return len(divisors_list)

# Function to check for triangle number
def isTriangleNumber(n):
    a = int(sqrt(2*n))
    return 0.5*a*(a+1) == n

# Function to calculate the last term of the series adding up to the triangle number
def lastTerm(n):
    if isTriangleNumber(n):
        return int(sqrt(2*n))
    else:
        return None

######################################### Production ########################################
# First Step
# First number 'check' to have 500 divisors
check = 2**4 * 3**4 * 5**4 * 7 * 11

# Second Step
# Starting from 'check', iterate sequentially checking for the next 'triangle' number
while not isTriangleNumber(check):
    check += 1

# Result is 62378865


# Third and Fourth Steps
# Calculate the last term of the series ('seriesLastTerm') that adds up to the newly calculated triangle number 'check'
seriesLastTerm = lastTerm(check)

# Iterate over triangle numbers checking for divisors > 500
while divisors(check) <= 500:
    # add the next term to check to get the next triangle number
    check += (seriesLastTerm + 1)
    seriesLastTerm += 1
print(check)

