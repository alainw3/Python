def print_rangoli(size):
    # your code goes here
    #size =3 
    dep = size+64

    for _ in range(size):
        x = _+1
   
        line =(*(chr((dep-_+i)).lower() for i in range(x-1,0,-1)),
               *(chr((dep-_+i)).lower() for i in range(x       )),
        )
        print("-".join(line).center((size*2+(size-1)*2)-1,"-"))
        
    for _ in range(size-2,-1,-1):
        x = _+1
   
        line =(*(chr((dep-_+i)).lower() for i in range(x-1,0,-1)),
               *(chr((dep-_+i)).lower() for i in range(x       )),
        )
        print("-".join(line).center((size*2+(size-1)*2)-1,"-"))


if __name__ == '__main__':