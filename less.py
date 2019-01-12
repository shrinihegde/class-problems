lst=[]
cmp=[]
n=eval(input("enter the number of elements: "))
for i in range(n):
    inp=eval(input("enter the %d elements: "%(i+1)))
    lst.append(inp)
    if lst[i]<=5:
      a=lst[i]
      cmp.append(a)
print(lst)
print(cmp)
