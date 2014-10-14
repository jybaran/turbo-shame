####AYAY BEAUTIFUL SOUp

from bs4 import BeautifulSoup
import google
import urllib2



#html_doc = open('bsoup.html','r').read()
#soup = BeautifulSoup(html_doc)

data=""


for url in google.search("hello",num=1,start=0,stop=10): #searching for query "hello"
    u = urllib2.urlopen(url)
    d = u.read()
    soup = BeautifulSoup(d)
    for script in soup(["script","style"]):
        script.extract()
    data = data + soup.get_text().encode('UTF-8').replace("\n","")

print data 
#to get rid of dumb javascript that get_text method doesnt do 

#print soup.get_text().encode('UTF-8')

