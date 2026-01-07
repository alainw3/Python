import numpy
(N, M,P)=input().split()
l1=[]
for _ in range(int(N)):
    l1.append(list(map(int,input().split())))
    
l2=[]    
for _ in range(int(M)):
    l2.append(list(map(int,input().split())))

#print(l1)
#print(l2)

a1= numpy.array(l1)
a2= numpy.array(l2)
#print (a1)
#print (a2)
print(numpy.concatenate((a1,a2)))