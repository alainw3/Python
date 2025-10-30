if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=list(arr)
    maxl = max(l)
    #ln =[x for x in l if x < maxl] 
    ln = filter(lambda x : x < maxl, l) 
    print(max(ln))
