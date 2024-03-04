import math
my_list = [34, 125, 49, 68]

def sq_rt(num):
    return math.cbrt(num)

sq_list = list(map(sq_rt,my_list))
print (sq_list)