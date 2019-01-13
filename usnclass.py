class clyass:
    def disp(self,usn,name):
        self.usn=usn
        self.name=name
        d=dict(zip(self.usn,self.name))
        print(d)

usn=[]
name=[]
n=eval(input("enter the number entries: "))
for i in range(n):
    usn.append(input("enter the usn of the student: "))
    name.append(input("enter the name of the student: "))
a=clyass()
a.disp(usn,name)
