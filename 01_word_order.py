# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

paragraphe =[]
n = input()
lw=[]
for _ in range(int(n)):
    w = input()
    paragraphe.append(w)   

#lw= list(dict.fromkeys(paragraphe))        
#print (paragraphe)
#print (lw)
#print(len(lw))
#for w in list(dict.fromkeys(paragraphe)):
#print(paragraphe.count(w), end=' ')

my_dict = {w: paragraphe.count(w) for w in paragraphe}
lw=list( my_dict.values())
print(len(my_dict))
#print(lw)
for l in lw:
    print(l, end=' ')
