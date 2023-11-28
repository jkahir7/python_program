class A:
    num = 5

class B(A):
    def squre(self):
        ans = self.num * self.num
        print(ans)
        self.ans = ans
        
    def display(self):
        print(self.ans)

class C(B):
    def check(self):
        if self.ans%2 == 0:
            print("number is even")

        else:
            print("number is odd")


obj = C()
obj.squre()
obj.check()