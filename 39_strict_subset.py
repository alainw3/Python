# Enter your code here. Read input from STDIN. Print output to STDOUT
A= set(input().split())
#print(A)
#for _ in range(int(input())):
#    N=set(input().split())
#    print(N) 
#    print(len(N-A))

print("False" if sum(list((len(set(input().split())-A) for _ in range(int(input())))))>0 else "True"