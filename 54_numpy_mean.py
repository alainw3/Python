import numpy
(N,M)=input().split()
ar = numpy.array([input().split() for _ in range(int(N)) ],float)
print (numpy.mean(ar,axis=1))
print (numpy.var(ar,axis=0))
print (round( numpy.std(ar),11))
