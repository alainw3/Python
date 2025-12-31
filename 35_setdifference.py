# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
set_e=set(input().split())
input()
set_f=set(input().split())
print(len(set_e.difference(set_f)))