import numpy
(N,M)=input().split()
l=[]
for _ in range(int(N)):
    l.append(list(map(int,input().split())))

array = numpy.array(l)  

print(numpy.transpose(array))
print(array.flatten())
