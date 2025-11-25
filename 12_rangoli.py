def print_rangoli(size):
    # your code goes here
    for _ in range(size):
        #print("a".center(size+2,"-"))
        x = _+1
        line =(*(chr((size+_-i-1)+65).lower() for i in range(x-1,0,-1)),
               *(chr((size+_-i-1)+65).lower() for i in range(x       )),
              )
        print("-".join(line).center((size*2+(size-1)*2)-1,"-"))
             


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
