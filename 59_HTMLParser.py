# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag,attrs):
        print("Start :", tag  )
        for _ in attrs:
            print("->", _[0],">", _[1])
    def handle_endtag(self, tag):
        print("End   :", tag  )
         
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag  )
        for _ in attrs:
            print("->", _[0],">", _[1])
         
    
    #def handle_data(self, tag):
        #print("Empty : ", tag  )

N =int(input())
parser = MyHTMLParser()
for _ in range(int(N)):
    s = input()
    #print(s)
    parser.feed(s)
