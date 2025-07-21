# Enter your code here. Read input from STDIN. Print output to STDOUT
paragraphe =[]
n = input()
lw=[]
k=0
for _ in range(int(n)):
    w = input()
    i = paragraphe.index(w) if w in paragraphe else -1
    if i >=0 :
        lw[i]+=1
    else:
        paragraphe.append(w) 
        lw.append(1)
        
print(len(lw))
print(*lw, end=' ')

