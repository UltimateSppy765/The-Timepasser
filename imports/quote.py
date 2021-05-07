import wikiquotes, wikiquote
from random import choice

class Error(Exception):
  pass

class NoAuthorFound(Error):
  pass

class NoQuoteFound(Error):
  pass

def qfind(query:str):
  auxlist=[]
  try:
    a=wikiquote.search(query)
  except:
    a=[]
  else:
    for wor in a:
      auxlist.append(wor)
  try:
    b=wikiquotes.search(query,"english")
    for word in b:
      if word not in auxlist:
        auxlist.append(word)
  except:
    b=[]
  if auxlist==[]:
    raise NoAuthorFound
  else:
    for c in auxlist:
      if query.lower()==c.lower():
        autor=c
        try:
          d=[wikiquotes.random_quote(c,"english")]
        except:
          d=[]
        try:
          e=wikiquote.quotes(c,max_quotes=1)
        except:
          e=[]
        qt=choice(d+e)
        break
      elif query.lower() in c.lower():
        autor=c
        try:
          d=[wikiquotes.random_quote(c,"english")]
        except:
          d=[]
        try:
          e=wikiquote.quotes(c,max_quotes=1)
        except:
          e=[]
        qt=choice(d+e)
        break
    try:
      return [qt,autor]
    except:
      pass
    qtlist=[]
    for f in auxlist:
      auxlist1=[]
      try:
        g=wikiquotes.get_quotes(f,"english")
      except:
        g=[]
      else:
        for q1 in g:
          auxlist1.append(q1)
      try:
        h=wikiquote.quotes(f,max_quotes=10)
        for q2 in h:
          if q2 not in auxlist1:
            auxlist1.append(q2)
      except:
        h=[]
      for i in auxlist1:
        if query.lower() in i.lower():
          r=[i,f]
          qtlist.append(r)
    if qtlist==[]:
      pass
    else:
      p=choice(qtlist)
      qt=p[0]
      autor=p[1]
    try:
      return [qt,autor]
    except:
      raise NoQuoteFound
