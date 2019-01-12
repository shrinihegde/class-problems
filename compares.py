lst=[]
lst2=[]
lst.extend(eval(input("enter the elements: ")))
print(lst)
n=len(lst)
for i in range(n-1):
    if lst[i]!=lst[(i+1)]:
        lst2.append(lst[i])
print(lst2)
