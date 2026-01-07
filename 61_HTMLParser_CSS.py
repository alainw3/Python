# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    s= input()
    ls = s.split(';')
    #print(ls)
    for _ in ls:
        ls1 = _.split(',')
        for l in ls1:
            m =re.match(r'.+(#[\dABCDEFabcdef]{6}|#[\dABCDEFabcdef]{3}).*',l) 
            if (bool(m)):
                #print(s)
                print(m.group(1))
        
