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
print(len(my_dict))
for key, value in my_dict.items():
    print(value,end=' ')
