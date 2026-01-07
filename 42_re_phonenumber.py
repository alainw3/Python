# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N= int(input())

for _ in range(N):
    s= input()
    m= re.match(r'^[789]\d{9}$',s)
    print ('YES' if bool(m) else 'NO')