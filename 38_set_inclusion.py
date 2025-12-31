# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for _ in range(T):
    len_A = int(input())
    A= set(input().split())
    len_B = int(input())
    B=set(input().split())
    
    print(all(e in B for e in A))

    #if len(A.difference(B))>0:
    #if (len(A-B)>0):
    #    print("False")
    #else:
    #    print("True")
