####AYAY BEAUTIFUL SOUp

from bs4 import BeautifulSoup

html_doc = open('bsoup.html','r').read()
soup = BeautifulSoup(html_doc)

print soup.get_text().encode('UTF-8')

