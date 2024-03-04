numbers = [1,2,3,4,5]

def square(number):
    return number ** 2

sq_number = list(map(square,numbers))

print(sq_number)