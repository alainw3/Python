# Enter your code here. Read input from STDIN. Print output to STDOUT# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S=input()
k=input()
m=re.search(r''+k,S[2:])

ls=[]
for i in range(len(S)):
    m=re.search(r''+k,S[i:])
    try:

        v = (m.start()+i,m.start()+i+len(k)-1)
        ls.append(v)
    except Exception as e:
        a=0
last=(-1,-1)
if len(ls)>0:        
    for _ in ls:
        if last != _:
            print(_)
        last=_
else:
    print((-1,-1))
    