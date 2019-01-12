lst1=[]
lst2=[]
n=eval(input("enter the number of elements: "))
for i in range(n):
    lst1.append(input("enter the %d keys: "%(i+1)))
    lst2.append(input("enter the %d values: "%(i+1)))
print(lst1)
print(lst2)
d=dict(zip(lst1,lst2))
print(d)
