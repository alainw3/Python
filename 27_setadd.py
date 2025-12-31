# Enter your code here. Read input from STDIN. Print output to STDOUT
N=input()
s=set()

#for _ in range(int(N)):
#    s.add(input())
#print (len(s))

print(len(set([input() for _ in range(int(N))])))

