if __name__ == '__main__':
    l=[]
    N = int(input())
    for _ in range(N):
        command = input()
        c= command.split()
        #print(c)
        #print(l)
        match c[0]:
            case 'insert':
                l.insert(int(c[1]),int(c[2]))
            case 'print':
                print(l)
            case 'remove': 
                l.remove(int(c[1]))
            case 'append':
                l.append(int(c[1]))
            case 'sort':
                l.sort()
            case 'pop':
                l.pop()
            case 'reverse':
                l.reverse()
                