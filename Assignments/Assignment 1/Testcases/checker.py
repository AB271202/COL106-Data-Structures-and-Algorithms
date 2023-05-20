from time import time
from a1 import findPositionandDistance
import time
n=int(input('Enter number of big test cases to test (from 1 to 10)'))
m = 0
d = open("check.txt", "r")
r = d.readlines()
print("Starting Checker")
st = time.time()
for i in open("testcases.txt", "r"):
    if str(findPositionandDistance(str(i).replace("\n", ""))) != str(r[m]).rstrip():
        print(f"Testcase {m+1} didnt match")
    else:
        print(f"Testcase {m+1}  match")
    if m+1==10*n:
        break
    m += 1
print(f"Time taken for normal testcases is {time.time()-st}")
print()
print("Checking Big Testcases")
m=100
st = time.time()

for i in open("testcases_big.txt", "r"):
    if str(findPositionandDistance(str(i).replace("\n", ""))) != str(r[m]).rstrip():
        print(f"Testcase {m+1} didnt match")
    else:
        print(f"Testcase {m+1}  match")
    
    if m+1==100+n:
        break
    m += 1
print(f"Time taken for big testcases is {time.time()-st}")
