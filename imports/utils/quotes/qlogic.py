import wikiquote,wikiquotes
from random import choice

def ranlist(title):
    try:
        a=[wikiquotes.random_quote(title,"english")]
    except:
        a=[]
    return a+wikiquote.quotes(title,max_quotes=1)

def qfind(query):
    Authorlist=[]
    try:
        a=wikiquotes.search(query,"english")
    except:
        pass
    else:
        Authorlist=a
        del a
    for i in wikiquote.search(query):
        if i not in Authorlist:
            Authorlist.append(i)
    if Authorlist==[]:
        return ["NoAuthorFound",wikiquote.random_titles(max_titles=7)]
    else:
        Authorlist.sort()
        for i in Authorlist:
            if not query.lower() in i.lower():
                if not i.lower() in query.lower():
                    continue
            qt=ranlist(i)
            if qt==[]:
                continue
            if query.lower()==i.lower():
                Authorlist.remove(i)
                return ["Success",choice(qt),i,Authorlist]
            elif query.lower() in i.lower() or i.lower() in query.lower():
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
