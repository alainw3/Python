# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
ls=list(s)
found =''
for _ in ls:
    #print(_)
    if (re.match(r'[a-zA-Z0-9]',_)):
        pattern = r'.*('+_+'{2}).*'
        m = re.match(pattern,s)
        try:
            m.group(1)
            found=_
            break
        except Exception as e:
            s_e=e

print(found if found else -1)     
