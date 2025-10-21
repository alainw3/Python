nm= input()

l= nm.split(' ')

occ= map(int,input().split(' '))

al = input().split(' ')
bl = input().split(' ')

#a_p= len(list(set(a) & set(occ)))
#b_p= len(list(set(b) & set(occ)))

#print(a_p-b_p)

A = set (map(int,al))
B = set (map(int,bl))
happiness = 0
for l in occ:
    if l in  A:
        happiness +=1
    elif l in B :
        happiness -=1
print(happiness)