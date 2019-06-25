sum_of_squares = 0
sum = 0
for index in range (1,101):
    sum_of_squares += index**2
    sum += index
square_of_sum = sum**2
difference = square_of_sum - sum_of_squares
print (difference)

