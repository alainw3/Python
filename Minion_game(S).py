def minion_game(S):
    # your code goes here

    listVoyell ="aeiouAEIOU"    ;
    stuart  =0;
    kevin   =0;
    # consonants
    
    S =S.upper();
    
    #print(S)  ;  
 
            
        
    #if (listVoyell.find(x[0])!=-1) : print ("VOYELL");
    #else : print("COSONNANT");
    
    #print(S.index("B"))      ; 
    #print(S[0:4]);
    #print(S.count("A"));
    #indexStart = S.index("B");
    
    listFoundConsonnant="";
    listFoundVoyell="";

    x = list(s);
    #for e in x:
    for idx, e in enumerate(x) :   
        # FOR STUART
        # Cnsonnant
        if (listVoyell.find(e)==-1): 
            if (listFoundConsonnant.find(e)==-1):
                listFoundConsonnant= listFoundConsonnant +e;
                #print("list cosonnant",listFoundConsonnant);
                indexStart = S.index(e);
                for i in range(indexStart+1,len(S)+1):
                    #print(S[indexStart:i],"--",S.count(S[indexStart:i]));
                    #stuart = stuart + S.count(S[indexStart:i]);
                    j=0;
                    while S[indexStart:i] in S[j:len(S)+1]:
                           stuart = stuart + 1;
                           #print(S[indexStart:i],"----index=",S.index(S[indexStart:i],j));
                           j = S.index(S[indexStart:i],j)+1;
            #else:
                #print();
        else:
            if (listFoundVoyell.find(e)==-1):
                listFoundVoyell = listFoundVoyell +e;
                print("list voyell",listFoundVoyell);
                indexStart = S.index(e);
                for i in range(indexStart+1,len(S)+1):
                    j=0;
                    while S[indexStart:i] in S[j:len(S)+1]:
                           kevin = kevin + 1;
                           print(S[indexStart:i],"----index=",S.index(S[indexStart:i],j));
                           j = S.index(S[indexStart:i],j)+1;
                        
                
                    

                
    #if (kevin > stuart):              
    print("Kevin", kevin);
    #else:
    print("Stuart", stuart);
        
        