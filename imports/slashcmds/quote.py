import os,wikiquote,requests,json
from imports.utils.quotes import qfinder,qget
from imports.utils import perspective

baseurl=os.environ['BASE_URL']

def cmd(subc:str,query:str,token:str,aid:str,iid:str,usid:str):
    if subc=="get":
        return {"type":4,"data":qget.getquote(type=query,userid=usid)}
    else:
        if len(query)>100:
            return {
                "type": 4,
                "data": {
                    "flags": 64,
                    "content": f"<:tickNo:315009174163685377> Your query cannot be greater than 100 characters. (Given query is `{len(query)}` characters long)\nThis is to prevent breaking of the command. I hope you're smart enough to understand..."
                }
            }
        a=perspective.analyse(cont=query)
        if a is not None:
            return a
        requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":5})
        jsr=qfinder.qres(query=query,userid=usid)
        a=requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=jsr)
        return
