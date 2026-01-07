import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    n=0

    #n=n+len(node.attrib)
    #for _ in node:
    #    n=n+get_attr_number(_)  
        
    n=sum(len(_.attrib) for _ in node.iter())
              
    return n

if __name__ == '__main__':