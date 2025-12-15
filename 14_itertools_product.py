# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product


#A = [int(x) for x in  input().split()]
A = list(map(int,input().split()))


#B = [int(x) for x in input().split()]
B= list(map(int, input().split()))


l = list(product(A,B))
print(*(x for x in l))


