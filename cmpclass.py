class less:
    def limit(self,s):
        self.s=s
        n=len(self.s)
        lst2=[]
        for j in range(n-1):
            if self.s[(j+1)]!=self.s[j]:
                lst2.append(self.s[j+1])
        print(lst2)
a=less()
lst=[]
n=eval(input('enter the number of elements to be added: '))
for i in range(n):
    lst.append(eval(input('enter the elements: ')))
print(lst)
a.limit(lst)
