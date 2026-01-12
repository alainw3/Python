import operator

def person_lister(f):
    def inner(people):
        # complete the function
        #print (people)
        #l=[]
        people.sort(key=lambda x : int(x[2]))
        

        l = [f(_) for _ in people]
        return l
        
    return inner

@person_lister