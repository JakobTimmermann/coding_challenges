# Super simple with python arbitrarly large numbers
number = pow(2, 1000)
number_map = map(int, str(number))
print(sum(number_map))
