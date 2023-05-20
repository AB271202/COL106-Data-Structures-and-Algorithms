class LinkedStack:
    '''Implementation of Stack using linked list'''
    # ---------------------Node for LL---------------------------------------------------------
    class _Node:
        __slots__ = ["_data", "_next"]  # This removes the dictionary associated with the object

        # Result of using __slots__:
        #       Fast access to attributes
        #       Saves memory space

        def __init__(self, data, next):
            self._data = data
            self._next = next

    # ------------------LinkedStack----------------------------------------------------------------
    def __init__(self):
        '''Initializing the class'''
        self._head = None
        self._size = 0

    def __len__(self):
        '''Returns length of the stack'''
        return self._size

    def is_empty(self):
        '''Checks if the stack is empty'''
        return self._size == 0

    def push(self, item):
        '''Adds an item to the stack.'''
        ''' Note that we must add the new node at the head of the LL, otherwise push operation will not be possible in constant time'''
        self._head = self._Node(item, self._head)
        self._size += 1

    def pop(self):
        '''Removes the element at the top of the stack and returns it'''
        if self.is_empty():
            raise Exception("Empty Stack")
        else:
            answer = self._head._data
            self._head = self._head._next
            self._size -= 1
            return answer

    def top(self):
        '''Returns the element at the top of the stack without removing it'''
        if self._head is None:
            raise Exception("Stack Empty")
        return self._head._data


def findPositionandDistance(P):
    answer = [0] * 4 #Initialize the answer to be returned to [0,0,0,0]
    stk = LinkedStack()
    stk.push(1) #1 is the basic multiplier for any + or - operation. For example +X means movement in +X direction 1 time
    n = 0
    m=len(P)
    while n < m:
        #Now we handle the three cases- if we get a number, a ')' or a '+'/'-' sign
        if P[n].isnumeric():
            s = P[n]
            n+=1
            while P[n]!='(':
                s += P[n]
                n += 1
            #The string s now has the number outside the bracket
            stk.push(stk.top() * int(s)) 
            #We multiply the number obtained with the one present at the top of the stack
            #For example 5(2(+Y3(+X))) means +Y operation takes place 5*2=10 times and +X takes place 10*3=30 times
            n +=1
        elif P[n] == ')':
            #')' signifies that now the multiplier has to be reset to the one outside current bracket
            stk.pop()
            n += 1
        else:
            #Now we add/subtract the corresponding coordinate the required number of times
            #ord('X')==88 ord('Y')==89 ord('Z')==90 so we can directly write for X Y or Z coordinate
            if P[n] == '+':
                answer[ord(P[n + 1]) - 88] += stk.top()
                answer[3] += stk.top()
            elif P[n] == '-':
                answer[ord(P[n + 1]) - 88] -= stk.top()
                answer[3] += stk.top()
            n += 2
    return answer

# print(findPositionandDistance('+X+Y+X-Y-Z+X+X-Z-Z-Z-Z-Y+Y-X'),'\n',
#       findPositionandDistance('+X2(+Y-X-Z)8(+Y)9(-Z-Z)'),'\n',
#       findPositionandDistance(''),'\n',
#       findPositionandDistance('5(2(3(+X+X)))'),'\n',
#       findPositionandDistance('+Z6(+X+Y+X-Y)9(-X+Z-X-Z8(+X+Y-Z)9(+Y-Z-X-Y4(-X+Y-X-Z+X)))'),'\n',
#       findPositionandDistance('1(+X)5(+Y)41(+Z)1805(-X)3263441(-Y)10650056950805(-Z)'),'\n',
#       findPositionandDistance('9999(+X)'))
