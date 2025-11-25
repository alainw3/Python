Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
l = s.split()
N = int(l[0])
M = int(l[1])
c=".|."
for _ in range(int(N/2)):
    x =2*_+1
    print((c*x).center(M,"-"))
print("WELCOME".center(M,"-"))
for _ in range(int(N/2)):
    x =N-(2*_+2)
    print((c*x).center(M,"-"))
