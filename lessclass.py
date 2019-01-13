class less:
    def limit(self,s):
        self.s=s
        lst2=[]
        for j in range(len(self.s)):
            if self.s[j]<5:
                lst2.append(self.s[j])
        print(lst2)
a=less()
lst=[]
n=eval(input('enter the number of elements to be added: '))
for i in range(n):
    lst.append(eval(input('enter the elements: ')))
print(lst)
a.limit(lst)


