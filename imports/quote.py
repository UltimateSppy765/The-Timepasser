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
    qtlist3=[]
    for f in aulist:
      try:
        g=wikiquotes.get_quotes(f,"english")
      except:
        g=[]
      try:
        h=wikiquote.quotes(f,max_quotes=10)
      except:
        h=[]
      qtlist2=h+g
      auxlist2=[]
      for s in qtlist2:
        if not s in auxlist2:
          auxlist2.append(s)
      for i in auxlist2:
        if query.lower() in i.lower():
          r=[i,f]
          qtlist3.append(r)
    if qtlist3==[]:
      pass
    else:
      p=choice(qtlist3)
      qt=p[0]
      autor=p[1]
    try:
      return [qt,autor]
    except:
      raise NoQuoteFound
