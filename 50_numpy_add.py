import numpy

(N,M)=input().split()

lA=[list(map(int,input().split()))    for _ in range(int(N))]
lB=[list(map(int,input().split()))    for _ in range(int(N))]
A=numpy.array(lA,int)
B=numpy.array(lB,int)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
