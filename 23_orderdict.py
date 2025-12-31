# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

n = input()
ordered_dictionnary = OrderedDict()

for _ in range(int(n)):
    ls = input().split(" ")
   
    item_name =" ".join(ls[:-1])
    price = int(ls[len(ls)-1])
    
    if (ordered_dictionnary.get(item_name)):
        ordered_dictionnary[item_name]+= price  
    else:
        ordered_dictionnary[item_name] = price


for key,value in ordered_dictionnary.items():
    print(key,value)
