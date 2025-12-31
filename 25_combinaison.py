# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

(S,k)= input().split()
A=[]
A=list(S)
A.sort()

for _ in range(int(k)):
    for x in (list(combinations(A,_+1))):
        print("".join(x))