import wikiquote,wikiquotes
from random import choice

blacklist=["Quotes are arranged in chronological order"]

def ranlist(title):
    try:
        a=[wikiquotes.random_quote(title,"english")]
    except:
        a=[]
    try:
        b=wikiquote.quotes(title,max_quotes=1)
    except:
        b=[]
    Newlist=a+b
    for i in blacklist:
        if i in Newlist:
            Newlist.remove(i)
    return Newlist

def findtitles(query):
    List=[]
    try:
        a=wikiquotes.search(query,"english")
    except:
        pass
    else:
        List=a
        del a
    for i in wikiquote.search(query):
        if i not in List:
            List.append(i)
    return List

def qfind(query):
    Authorlist=findtitles(query=query)
    if Authorlist==[]:
        return ["NoAuthorFound",wikiquote.random_titles(max_titles=7)]
    else:
        Authorlist.sort()
        for i in Authorlist:
            if query.lower()==i.lower():
                qt=ranlist(i)
                if qt==[]:
                    Authorlist.remove(i)
                    continue
                else:
                    Authorlist.remove(i)
                    return ["Success",choice(qt),i,Authorlist]
        for i in Authorlist:
            if query.lower() in i.lower() or i.lower() in query.lower():
                qt=ranlist(i)
                if qt==[]:
                    Authorlist.remove(i)
                    continue
                else:
                    Authorlist.remove(i)
                    return ["Success",choice(qt),i,Authorlist]
        Quotelist=[]
        Resultlist=[]
        for i in Authorlist:
            try:
                a=wikiquotes.get_quotes(i,"english")
            except:
                pass
            else:
                Quotelist=a
                del a
            try:
                c=wikiquote.quotes(i,max_quotes=5)
            except:
                c=[]
            for k in c:
                if k not in Quotelist:
                    Quotelist.append(k)
            for j in Quotelist:
                if query.lower() in j.lower():
                    Resultlist.append([j,i])
        if Resultlist!=[]:
            Resultlist.sort()
            Quote=choice(Resultlist)
            Authorlist.remove(Quote[1])
            return ["Success",Quote[0],Quote[1],Authorlist]
        else:
            return ["NoQuoteFound",Authorlist]
