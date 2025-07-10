def minion_game(S):
    # your code goes here

    listVoyell ="aeiouAEIOU"    ;
    stuart  =0;
    kevin   =0;
    # consonants
    
    print(S)  ;  
    x = list(s);
            
        
    if (listVoyell.find(x[0])!=-1) : print ("VOYELL");
    else : print("COSONNANT");
    print(S.index("B"))      ; 
    print(S[0:4]);
    
    print(S.count("A"));
    indexStart = S.index("B");
    
    listFoundConsonnant="";
    listFoundVoyell="";

    for e in x:
        # FOR STUART
        # Cnsonnant
        if (listVoyell.find(e)==-1): 
            if (listFoundConsonnant.find(e)==-1):
                listFoundConsonnant= listFoundConsonnant +e;
                print("list cosonnant",listFoundConsonnant);
                indexStart = S.index(e);
                for i in range(indexStart+1,len(S)+1):
                    print(S[indexStart:i],"--",S.count(S[indexStart:i]));
                    stuart = stuart + S.count(S[indexStart:i]);
            else:
                print();
        else:
            if (listFoundVoyell.find(e)==-1):
                listFoundVoyell = listFoundVoyell +e;
                print("list voyell",listFoundVoyell);
                indexStart = S.index(e);
                for i in range(indexStart+1,len(S)+1):
                    print(S[indexStart:i],"--",S.count(S[indexStart:i]));
                    kevin= kevin + S.count(S[indexStart:i]);
                
                    

                
    print("KEVIN", kevin);
    print("STUART", stuart);
        