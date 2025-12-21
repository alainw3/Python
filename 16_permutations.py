# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
(word,k)=input().split()
ls = list(word)
ls.sort()
ps = list(permutations(ls,int(k)))
for p in ps:
    print("".join(p))
