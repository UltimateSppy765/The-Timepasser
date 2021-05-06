import wikiquotes, wikiquote
from random import choice

class Error(Exception):
  pass

class NoAuthorFound(Error):
  pass

class NoQuoteFound(Error):
  pass

def qfind(query:str):
  try:
    a=wikiquote.search(query)
  except:
    a=[]
  try:
    b=wikiquotes.search(query,"english")
  except:
    b=[]
  aulist=a+b
  auxlist1=[]
  for word in aulist:
    if word not in auxlist1:
      auxlist1.append(word)
  if aulist==[]:
    raise NoAuthorFound
  else:
    for c in auxlist1:
      if query.lower() in c.lower():
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
