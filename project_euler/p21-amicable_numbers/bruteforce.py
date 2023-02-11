def get_sum_of_divisors(n):
    list_of_divisors = [1]
    for potential_divisor in range(2,int(n**0.5) + 1):
        if n % potential_divisor == 0:
            list_of_divisors.append(potential_divisor)
            list_of_divisors.append(int(n/potential_divisor))
    return sum(list_of_divisors)

def main(cap=10_000):
    number = 1
    list_of_amicable_numbers = []
    while number < cap:
        dofN = get_sum_of_divisors(number) # Exclude number itself 
        if dofN != number:
            dofN2 = get_sum_of_divisors(dofN) # Exclude number itself 
            if dofN2 == number:
                list_of_amicable_numbers.append(number)
        number += 1
    print(f"Sum of amicable numbers up to {cap}: {sum(list_of_amicable_numbers)}")

main()
