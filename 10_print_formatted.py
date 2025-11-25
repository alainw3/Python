def print_formatted(number):
    # your code goes here
    l=int(len(format(number,"b")))
   
    for _ in range(number):
        number=_+1  
        octo=format(number,"o")
        hexa = f"{number:X}"
        bina=format(number,"b")
       
        print(f"{number:>{l}}",
              f"{octo:>{l}}",
              f"{hexa:>{l}}",
              f"{bina:>{l}}"
        )




if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
