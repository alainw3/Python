import numpy
numpy.set_printoptions(legacy='1.13')

(N,M)=input().split()
print (numpy.eye(int(N), int(M), k=0))

