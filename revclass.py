class rev:
    def rever(self,lst):
        self.lst=lst
        lst2=self.lst[::-1]
        print(' '.join(lst2))

inp=input("enter the string: ")
lst=inp.split()
a=rev()
a.rever(lst)
