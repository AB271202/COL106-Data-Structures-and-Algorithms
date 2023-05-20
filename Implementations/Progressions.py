class Progression:
    def __init__(self, start=0):
        self._current=start
    def _advance(self):
        self._current+=1
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer=self._current
            self._advance()
            return answer
    def __iter__(self):
        return self
    def printprogression(self,n):
        for i in range(n):
            print(next(self), end=" ")

class AP(Progression):
    def __init__(self,start=0,step=1):
        super().__init__(start)
        self._step=step
    def _advance(self):
        self._current+=self._step

class GP(Progression):
    def __init__(self,start=1,ratio=1):
        super().__init__(start)
        self._ratio=ratio
    def _advance(self):
        self._current*=self._ratio

class Fibbo(Progression):
    def __init__(self,start=0,second=1):
        super().__init__(start)
        self._prev=second-start
        
    def _advance(self):
        self._current,self._prev=self._prev, self._current+self._prev


F=Fibbo()
F.printprogression(10)
