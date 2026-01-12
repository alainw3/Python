import re


def wrapper(f):
    def fun(l):
        # complete the function
        l= [arrange(_) for _ in l]
        l.sort()
        return f(l)
        #for _ in l:
        #    print(_)

    return fun
    
        
def arrange(s):
    if (len(s)==10):
        s=re.sub(r'(\d{5})(\d{5})','+91 \\1 \\2',s)
    if (len(s)>10):
        s=re.sub(r'^[+]*91(\d{5})(\d{5})','+91 \\1 \\2',s)
        s=re.sub(r'^0(\d{5})(\d{5})','+91 \\1 \\2',s)
    return s


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
