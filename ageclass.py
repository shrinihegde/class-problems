class nameage:
    def cal(self,age):
        total=0
        self.age=age
        total=2019+100-self.age
        return total
    def disp(self,m,n):
        self.m=m
        self.n=n
        print(f"hey {self.m} you'll turn 100years in {self.n}")
inp=input('enter your name:')    
age=eval(input("enter your age: "))
a=nameage()
b=a.cal(age)
a.disp(inp,b)

              
             
