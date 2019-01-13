class name:
    def search(self,lst,sear):
        self.lst=lst
        self.sear=sear
        lst2=[]
        for i in range(len(self.lst)-1):
            if self.lst[i]==self.sear:
                lst2.append(i)
        print(lst2)
lst=[]
lst.extend(eval(input("enter the elements: ")))
print(lst)
sear=eval(input("enter the search element: "))
a=name()
a.search(lst,sear)
