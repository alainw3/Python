import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth

    maxdepth = max(maxdepth,level+1)
    #for _ in elem.iter():
    #    if (elem.tag != _.tag):
    #        if ((len(list(_.iter()))>=1)):
    #            maxdepth = depth(_,level+1)
    
    for child in elem:
        maxdepth = depth(child,level+1)
        
    return  maxdepth
if __name__ == '__main__':