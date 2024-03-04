number =  [1,2,3,4,5,6,7,8]

def even(num):
    return num % 2 == 0

even_lambda = lambda num: num%2 == 0

even_number = filter(even_lambda,number)

print (list(even_number))