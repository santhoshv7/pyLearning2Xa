class Calc():
    def sum(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self, a,b):
        return a*b
    def div(self, a,b):
        return a/b

a = Calc()
result = a.sum(5,6)
result1 = a.sub(5,6)
result2 = a.mul(5,6)
result3 = a.div(5,6)


print (result)
print (result1)
print (result2)
print (result3)