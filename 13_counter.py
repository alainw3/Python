
from collections import Counter


# Enter your code here. Read input from STDIN. Print output to STDOUT
X= input()
Shoes_stock_list= input().split()
shoes_dict=Counter(Shoes_stock_list)
customers= input()
earn = 0
for _ in range(int(customers)):
    (shoe,price)=input().split()
    if (shoes_dict.get(shoe) and shoes_dict[shoe]>0):
        earn = earn + int(price)
        shoes_dict[shoe]-=1
print (earn)      
