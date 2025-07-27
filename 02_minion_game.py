def minion_game(string):
    print(s)
    
    #remove duplicate in a list s
    noduplicate     = list(dict.fromkeys(s))
    #print(noduplicate)
    
    #remove vowels
    onlyconsonant   = filter(lambda w: isvowel(w),noduplicate)
    score = 0
    for y in onlyconsonant:
      
        score = score  + s.count(y)
        print(y,'---',s.count(y),'--->',score)
        score = listcomposition(y,noduplicate,score)
    print(score)
def listcomposition(b,noduplicate,score):
    n = map (lambda w: b+w[0],noduplicate)
    compose = list(n)
    only_matching = filter(lambda compose:s.count(str(compose))>0, compose)
    for x in only_matching:
        score = score + s.count(x)
        print(x,'---',s.count(x),'--->',score)
        score = listcomposition(x,noduplicate,score)
    return score
    
def isvowel(v):
    return v=='A' or  v=='E' or v=='U' or  v=='I' or v=='O' 