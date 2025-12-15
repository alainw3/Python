#!/bin/python3


import math
import os
import random
import re
import sys
import re


# Complete the solve function below.
ls=[]
def solve(s):
    s= s.replace(s[0],s[0].upper())
    #print(*(x.upper() for x in s))
    #s = re.sub(r'(\s*)(\w)',r'\1\2',s)
    for i,l in enumerate(list(s)):
        if (i>0 and s[i-1]==' '):
            ls.append(s[i].upper())    
        else:    
            ls.append(s[i])    
    s ="".join(ls)  
   
    new_list = s.split(" ")
    new_list = map(str.capitalize,new_list)
    return " ".join(new_list)


    return s