# Enter your code here. Read input from STDIN. Print output to STDOUT
nm= input()

l= nm.split(" ")

occ= input().split(" ")
a = input().split(" ")
b = input().split(" ")

score =0

for c in occ:
    if c in a:
        score+= 1
    if c in b:
        score-= 1
        
print(score)