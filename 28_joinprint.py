# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

(S,k)= input().split()
l=list(S)
l.sort()
#for _ in list(combinations_with_replacement(l,int(k))):
#    print("".join(_))
print("\n".join(("".join(x) for x in list(combinations_with_replacement(l,int(k))) )))