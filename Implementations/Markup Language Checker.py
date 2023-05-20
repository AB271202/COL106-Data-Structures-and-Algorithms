from Stacks import Stack

S='''<html>
<head></head>
</html>'''
def checkMarkup(S):
    stk=Stack()
    i=0
    while i<len(S):
        if S[i]=='<':
            i+=1
            if S[i]!='/':
                s=""
                while S[i]!='>':
                    s+=S[i]
                    i+=1
                stk.push(s)
            else:
                i+=1
                s=""
                while S[i]!='>':
                    s+=S[i]
                    i+=1
                if stk.is_empty():
                    return False
                elif stk.top()!=s:
                    return False
                else:
                    stk.pop()
        i+=1
    return stk.is_empty()

print(checkMarkup(S))
