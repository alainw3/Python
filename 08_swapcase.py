def swap_case(s):
    l=list(s)
    l1=[x.lower() if x.upper() == x else x.upper() for x in l]
    s="".join(l1)
    return s