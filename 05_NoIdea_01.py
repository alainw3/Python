input()
occ= input().split(" ")
a = input().split(" ")
b = input().split(" ")
#print(occ)
score =0

for c in a:
    score = score + occ.count(c)
for c in b:
    score = score - occ.count(c)
        
print(score)