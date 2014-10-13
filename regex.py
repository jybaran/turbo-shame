# -*- coding: cp1252 -*-

import re

corpus = open('worldwartwo.txt','r')
temp = corpus.read()
corpus_text = temp.replace('\n',' ')
corpus.close()

english = open('words.txt','r')
words = english.read()
english.close()

match_names = re.findall(r"((?!A |The |a |the )([A-ZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝ][a-zàáâãäåæçèéêëìíîïðñòóôõöøùúûüý]*\. )?([A-ZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝ][a-zàáâãäåæçèéêëìíîïðñòóôõöøùúûüý]*\.? ?)+(((von )?(van )?(del )?(de la )?(de los )?(de las )?(l')?(d')?(Mc)?(Mac)?[A-ZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝ][a-zàáâãäåæçèéêëìíîïðñòóôõöøùúûüý]*))?(( Sr\.)|( Jr\.)|( M*D*C*L?X*V*I*V?X?L?C?D?M?))?)",corpus_text)
match_dates = re.findall(r"((January|February|March|April|May|June|July|August|September|October|November|December) ([0-3]?[0-9](th|rd|st|nd)?,? )?([0-9]+(\-[0-9]+)?)?(( (A(\.)?D(\.)?))|( B(\.)?C(\.)?E(\.)?)|( (B(\.)?C(\.)?)))?)",corpus_text)

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
print names



dates = []
for d in match_dates:
    date = d[0]
    l = date.split(" ")
    while "" in l: #null characters aaaaaaaa
        l.remove("")
    item = (" ").join(l).strip()
    dates.append(item)
    
print dates












