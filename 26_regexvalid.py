# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T= input()
for _ in range(int(T)):
    S= raw_input()

    try:
        re.compile(S)
        print("True")
    except :
        print("False")    
    
