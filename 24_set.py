# Enter your code here. Read input from STDIN. Print output to STDOUT
M=input()
Mset = set(input().split())
N=input()
Nset = set(input().split())


ls = list(map(int,list( Mset.difference(Nset).union(Nset.difference(Mset)))))
ls.sort()
for _ in ls:
    print(_)
