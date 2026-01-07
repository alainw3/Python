import numpy
(N,M)=input().split()

ls=[list(input().split())    for _ in range(int(N))]
ar = numpy.array(ls,int)
mn = numpy.min(ar,axis =1 )
print(max(mn))