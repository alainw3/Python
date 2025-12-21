# Enter your code here. Read input from STDIN. Print output to STDOU
from collections import defaultdict


d= defaultdict(list)
(n,m)= input().split(' ')


for _ in range(int(n)):
    d['A'].append(input())


for _ in range(int(m)):
    w = input()
    ls = [str(i+1) for i,x in enumerate(d['A']) if x == w]
    print(' '.join(ls) if len(ls)>0 else '-1')    