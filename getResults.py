# -*- coding: cp1252 -*-

from bs4 import BeautifulSoup
import google
import urllib2
import re
from collections import Counter


#corpus = open('worldwartwo.txt','r')
#temp = corpus.read()
#corpus_text = temp.replace('\n',' ')
#corpus.close()

english = open('words.txt','r')
words = english.read()
english.close()

def everything(query):
    data = get_results(query)
    if query[:4] == "who ": 
        l = findnames(data)
    elif query[:4] == "when":
        l= finddates(data)
    else: 
        return None
    c = Counter(l)
    l2 = c.most_common(5)
    return l2
    

def get_results(query):
    data=""
    for url in google.search(query,num=1,start=0,stop=10): #searching for query "hello"
        u = urllib2.urlopen(url)
        d = u.read()
        soup = BeautifulSoup(d)
        for script in soup(["script","style"]):
            script.extract()
        data = data + soup.get_text().encode('UTF-8').replace("\n","")
    return data

def findnames(text): 
    match_names = re.findall(r"((?!A |The |a |the )([A-Z�����������������������������][a-z�����������������������������]*\. )?([A-Z�����������������������������][a-z�����������������������������]*\.? ?)+(((von )?(van )?(del )?(de la )?(de los )?(de las )?(l')?(d')?(Mc)?(Mac)?[A-Z�����������������������������][a-z�����������������������������]*))?(( Sr\.)|( Jr\.)|( M*D*C*L?X*V*I*V?X?L?C?D?M?))?)",text)
    names = []
    for name in match_names:
        item = name[0]
        l = item.split(" ")
        while "" in l: #null characters are a sin
            l.remove("")
        item = (" ").join(l)
            
        if ((item[len(item)-1] == '.') or (item[len(item)-1] == '\xe2')): #get out of here sentence periods and utf hyphens
            item = item[:len(item)-1]
                
        l2 = item.split(" ")
        
        isEnglish = False
        isShort = True
        hasComma = False
        
        for word in l2:
            word = word.strip()
            s = "\n"+word.upper()+"\n"
            if s in words:
                isEnglish = True
                
        if len(item) > 1:
            isShort = False
                
        for w in l2:
            if ',' in w:
                hasComma = True

        if ((not isEnglish) and (not isShort) and (not hasComma)):
            names.append(item)
    return names 


def finddates(text): 
    match_dates = re.findall(r"((January|February|March|April|May|June|July|August|September|October|November|December) ([0-3]?[0-9](th|rd|st|nd)?,? )?([0-9]+(\-[0-9]+)?)?(( (A(\.)?D(\.)?))|( B(\.)?C(\.)?E(\.)?)|( (B(\.)?C(\.)?)))?)",text)

    dates = []
    for d in match_dates:
        date = d[0]
        l = date.split(" ")
        while "" in l: #null characters aaaaaaaa
            l.remove("")
            item = (" ").join(l).strip()
            dates.append(item)
    return dates
