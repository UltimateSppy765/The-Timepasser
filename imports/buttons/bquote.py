import json,os,requests,re
from imports.utils.quotes import qget,qfinder

baseurl=os.environ['BASE_URL']

def btn(aid:str,iid:str,token:str,binfo,msg,usid:str):
    if usid!=binfo["userid"]:
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": "<:tickNo:315009174163685377> You can't use that button on someone else's message, please try on your own one."
            }
        }
    if binfo["subc"]=="getran":
        requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":7,"data":qget.getquote(type="random",userid=binfo["userid"])})
        return
    else:        
        if binfo["subc"]=="are":
            pattern=r"\n-\ (.*)"
            qry=re.search(pattern,msg["embeds"][0]["description"]).group(1)
            requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":7,"data":{"components":[],"embeds":[{"title":f":mag: Searching for Query: '{qry}'","color":3092791}]}})
            a=qfinder.qres(query=qry,userid=binfo["userid"])
            requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=a)
        elif binfo["subc"]=="passre":
            pattern=r"query: \**\'(.*)'\**"
            qry=re.search(pattern,msg["embeds"][0]["title"]).group(1)
            requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":7,"data":{"embeds":[{"color":3092791,"title":":mag: Searching Again..."}],"components":[]}})
            a=qfinder.qres(query=qry,userid=binfo["userid"])
            requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=a)
        return
