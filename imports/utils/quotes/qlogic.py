import wikiquote,wikiquotes
from random import choice

def qsearch(query):
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
        return ["NoAuthorFound"]
    else:
        Authorlist.sort()
        for i in Authorlist:
            if query.lower()==i.lower():
                return ["Success",choice(wikiquote.quotes(i,max_quotes=1)+[wikiquotes.random_quote(i,"english")]),i]
            elif query.lower() in i.lower():
                return ["Success",choice(wikiquote.quotes(i,max_quotes=1)+[wikiquotes.random_quote(i,"english")]),i]
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
            Quote=choice(Resultlist)
            return ["Success",Quote[0],Quote[1]]
        else:
            return ["NoQuoteFound",Authorlist]
