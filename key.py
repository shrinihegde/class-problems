lst=[1,2,3,2,0,65,21,4,2,10]
lst2=[]
n=len(lst)
s=eval(input('enter the search element: '))
for i in range(n-1):
    if lst[i]==s:
        lst2.append(i)
print(lst2)
