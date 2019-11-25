#Just show some content by tags
from bs4 import BeautifulSoup
 
with open("Index.html", "r") as f:
    
    contents = f.read()
    soup = BeautifulSoup(contents, "lxml")
 
    print(soup.title)
    print(soup.p)