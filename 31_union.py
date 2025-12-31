# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
nr = set(input().split())

b= input()
br = set(input().split())


print(len(nr.union(br)))

