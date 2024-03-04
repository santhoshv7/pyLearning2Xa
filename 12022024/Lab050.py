'''a , b = 0,1
while a<50:
    print (a, end = " ")
    a,b=b,a+b'''

num = int(input("Enter the number of elements of Fibonacci Series:\n"))
a = 0
b= 1
for i in range (1,num+1):
    print (a, end = " ")
    a = b
    b = a+b