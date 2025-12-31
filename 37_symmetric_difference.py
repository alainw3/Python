# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
s_e=set(input().split())
input()
s_f=set(input().split())
print(len(s_e.symmetric_difference(s_f)))
