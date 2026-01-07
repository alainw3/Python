# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re
n=input()
for _ in range(int(n)):
    e=input()
    #print(e)
    s= email.utils.parseaddr(e)
    #print(s)
    if (bool(re.match(r'^[^_\-\.]\w.*\@[a-zA-Z]+\.[a-zA-Z]{1,3}$',s[1]))):
        print(email.utils.formataddr(s))
    