# import time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# largest pandigital number
largest = 0

# for loop to loop till 4 digits
for i in range(1,10000):
	
	# value for concatenated product
	product = ''
	
	# (1,2,3,4,.....n)
	integer = 1
	
	# if the product < 9 digits
	while len(product) < 9:
		
		# concatenating the product at each stage
		product += str(i*integer)
		
		# incrementing (1,2,3,4,....n)
		integer += 1
		
	# check for digits less than 9
	# check for all 1-9 numbers
	# check if '0' not in concatenated sting
	if ((len(product) == 9) and (len(set(product)) == 9) and ('0' not in product)):
	
		# check if product is greater than largest
		if int(product) > largest:
			largest = int(product)

# printing the largest
print(largest)

# time at the end of program execution
end = time.time()

#total time for execution
print(end - start)
