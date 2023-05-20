#Vector Class
class Vector:
    def __init__(self,length):
        self._coord=[0]*length

    def __len__(self):
        return len(self._coord)

    def __getitem__(self,k):
        if k<0:k+=len(self)
        return self._coord[k]

    def __setitem__(self,k,v):
        self._coord[k]=v

    def __contains__(self,v):
        if v in self._coord:
            return True
        return False
    
    def __neg__(self):
        neg=Vector(self.length)
        for i in range(self.length):
            neg._coord[i]=-1*self._coord[i]
        return neg
    
    def __add__(self,other):
        assert len(self)==len(other), "The vectors are not of the same dimension"
        l=len(self)
        add=Vector(l)
        for i in range(l):
            add[i]=self[i]+other[i]
        return add
    
    def __sub__(self,other):
        return self+(-other)

    def __str__(self):
        s=""
        for i in self._coord:
            s+=str(i)+" "
        return "< "+s+">"


v = Vector(5) # construct five-dimensional <0, 0, 0, 0, 0>
v[1] = 23 # <0, 23, 0, 0, 0> (based on use of setitem )
v[-1] = 45 # <0, 23, 0, 0, 45> (also via setitem )
print(v[4]) # print 45 (via getitem )
u=v+v # <0, 46, 0, 0, 90> (via add )
print(u) # print <0, 46, 0, 0, 90>
total = 0
for entry in v: # implicit iteration via len and getitem
    total += entry
print(total)
