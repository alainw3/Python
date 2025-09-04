import re
def minion_game(string):
    #print(s)
    
    #remove duplicate in a list s
    noduplicate     = list(dict.fromkeys(s))
    #print(noduplicate)
    
    #remove consonant or vowel
    onlyconsonantOrVower   = filter(lambda w: not(isvowel(w)),noduplicate)
    stuartScore = getscore(onlyconsonantOrVower,noduplicate)
    #stuartScore = 0
    
    onlyconsonantOrVower   = filter(lambda w: isvowel(w),noduplicate)
    kevinScore = getscore(onlyconsonantOrVower,noduplicate)
    #kevinScore =0
    
    if(stuartScore>kevinScore):
        print("Stuart " + str(stuartScore))
    if(stuartScore == kevinScore):        
        print("Draw")
    if(stuartScore<kevinScore):
        print("Kevin " + str(kevinScore))
    
def getscore(letters,noduplicate):
    score=0
    for y in letters:
        score = score  + s.count(y)
        #print(y,'---',s.count(y),'--->',score)
        score = listcomposition(y,noduplicate,score)
    return score
    
def listcomposition(b,noduplicate,score):
    n = map (lambda w: b+w[0],noduplicate)
    compose = list(n)
    only_matching = filter(lambda compose:s.count(str(compose))>0, compose)
    for x in only_matching:
        #score = score + s.count(x)
        score = score + len(re.findall('(?='+x+')', s))
        #print(x,'---',len(re.findall('(?='+x+')', s)),'--->',score)
        score = listcomposition(x,noduplicate,score)
    return score
    
def isvowel(v):
    return v=='A' or  v=='E' or v=='U' or  v=='I' or v=='O' 