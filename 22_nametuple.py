# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
student = namedtuple('Student',input())

#sum_marks = 0
#for _ in range(n):
#    #(a,b,c,d) = input().split()
#    sum_marks +=int(student(*input().split()).MARKS)
    

print(sum(int(student(*input().split()).MARKS)  for x in range(n))/n)
