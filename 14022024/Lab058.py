'''def demo_func(a,b,c=100):
    print (a+b+c)

demo_func(10,15)'''

def demo_func(*args):
    for i in args:
        print (i, end=" ")

demo_func(1,5,6,7,8)
