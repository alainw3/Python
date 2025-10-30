if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    
my_list_x=list(range(x+1))
my_list_y=list(range(y+1))
my_list_z=list(range(z+1))


combinaison=[list((x_n,y_n,z_n)) for x_n in (my_list_x) for y_n in (my_list_y) for z_n in (my_list_z)]

final = list (filter(lambda x: sum(x)!=n ,combinaison))
print(final)

