#factorial

num = int(input("Enter the value to find its factorial:\n"))

if num<0:
    print("Invalid Input")
elif num == 0:
    print ("The factorial of 0 is 1")
else:
    fact=1
    for i in range(1,num+1):
        fact = fact*i
    print(f"The factorial of {num} is {fact}")