# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
T= int(input())
for _ in range(T):
    uid = input()
    valid = False
    if (len(set(uid))==10 and bool(re.match(r'^[a-zA-Z0-9]*$',uid))):
        if (    bool(re.match(r'.*\d.*\d.*\d'   ,uid)) 
            and bool(re.match(r'.*[A-Z].*[A-Z]' ,uid))
           ):
            valid= True
    print("Valid" if valid else "Invalid")
    
                
                