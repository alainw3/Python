import numpy
(N,M)=input().split()
ls = []
for _ in range(int(N)):
    ls.append(list(map(int,input().split())))

a=numpy.array(ls) 
ls1 = numpy.sum(a,axis=0)

print(numpy.prod(numpy.array(ls1),axis=0))

