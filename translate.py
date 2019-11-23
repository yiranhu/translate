import re
from googletrans import Translator
import urllib.request as urllib
from bs4 import BeautifulSoup
url = ' https://www.jdsupra.com/legalnews/update-zum-bussgeldmodell-der-deutschen-13882/' # this should be read from standard input
response = urllib.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)
translator=Translator()

p=re.compile('^[a-zA-z\x7f-\xff]+$')
x="foo"
def isWord(x):
    return p.match(x) != None


for x in soup.get_text().split():
    print(x)
    # check if x is javascript
    # if library.isCode (x):
    # dont translate
    if isWord(x):
      print(translator.translate(x).text)
    # Figure out where all the text in the page is going 
