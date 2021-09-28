# default arguments
class ABC:
    def fun1(self, n1 = 0, n2 = 0, n3 = 0):
        print((n1 * n2) * n3)

num = ABC()
num.fun1()
num.fun1(2, 20, 3)

# variable length arguments

class add:
    def AddionofNNumbers(self, *no):
        total = 0
        for num in no:
            total = total + num
        print(total)    

abc1 = add()

abc1.AddionofNNumbers()
abc1.AddionofNNumbers(10)
abc1.AddionofNNumbers(10,20,30,40)
