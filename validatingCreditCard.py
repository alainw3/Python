# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def validCard(w):
    x = re.search("^[456].*",w)
    if (x):
        x = re.search("^[0-9]{16}$",w)
        if x:
            return _consecutive(w)
        else: 
            x = re.search("^[0-9]{4}[\\-][0-9]{4}[\\-][0-9]{4}[\\-][0-9]{4}$",w)            
            if x:
                return _consecutive(w)
            else:
                return False
    else:
        return False
        
def _consecutive(w):
    w = re.sub(r'-','',w)
    # r"(\d)(-?\1){3}"
    x = re.search('1{4}|3{4}|2{4}|4{4}|5{4}|6{4}|7{4}|8{4}|9{4}|0{4}',w)
    if x:
        return False
    else:
        return True

s =input()
for _ in range(int(s)):
    cardNumber = input()
    if not validCard(cardNumber):
        print("Invalid")
    else:
        print("Valid")    

    