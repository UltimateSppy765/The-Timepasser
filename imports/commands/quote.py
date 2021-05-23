import os,wikiquote,requests,json
from imports.utils.quotes import qfinder,qget
from imports.utils import perspective

baseurl=os.environ['BASE_URL']

def cmd(subc:str,query:str,token:str,aid:str,iid:str,usid:str):
    if subc=="get":
        return qget.getquote(type=query,userid=usid)
    else:
        a=perspective.analyse(cont=query)
        if a is not None:
            return a
        requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":5})
        jsr=qfinder.qres(query=query,userid=usid)
        requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=jsr)
        return
