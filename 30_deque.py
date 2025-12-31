n = int(input())
s = set(map(int, input().split()))

cN= int(input())

for _ in range(cN):
    inC = input()
    if (inC == 'pop'):
        s.pop()
    else:
       (command, i)= inC.split()
       if (command == 'remove'):
            s.remove(int(i))
       if (command == 'discard'):
            s.discard(int(i))

            
print(sum(s))