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
    if Authorlist=[]:
        return ["NoAuthorFound"]
    elif query in Authorlist:
        return ["Success",choice(wikiquote.quotes(query,max_quotes=1),wikiquotes.random_quote(query,"english")),query]
    else:
        Authorlist.sort()
        for i in Authorlist:
            if query in i:
                return ["Success",choice(wikiquote.quotes(i,max_quotes=1),wikiquotes.random_quote(i,"english")),i]
        Quotelist=[]
        Resultlist=[]
        for i in Authorlist:
            try:
                a=wikiquotes.get_quotes(i,"english")
            except:
                pass
            else:
                Quotelist=a
            for k in wikiquote.quotes(i,max_quotes=5):
                if k not in Quotelist:
                    Quotelist.append(k)
            for j in Quotelist:
                if query in Quotelist:
                    Resultlist.append([j,i])
        if Resultlist!=[]:
            Quote=choice(Resultlist)
            return ["Success",Quote[0],Quote[1]]
        else:
            return ["NoQuoteFound",AuthorList]
