####AYAY BEAUTIFUL SOUp

from bs4 import BeautifulSoup

html_doc = open('bsoup.html').read()
soup = BeautifulSoup(html_doc)

#print soup.prettify()  #prints indentation
print soup.title #prints thing including <title> tag
print soup.title.string #prints thing WITHOUT <title> tag
