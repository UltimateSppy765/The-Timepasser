import json,os,requests
from imports.utils.quotes import qget,qfinder

baseurl=os.environ['BASE_URL']

def btn(aid:str,iid:str,token:str,binfo,usid:str):
    if usid!=binfo["userid"]:
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": "<:tickNo:315009174163685377> You can't use that button on someone else's message, please try on your own one."
            }
        }
    if binfo["subc"]=="getran":
        requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":7,"data":{"components":[]}})
        requests.post(f"{baseurl}webhooks/{aid}/{token}",headers={"Content-Type": "application/json"},json=qget.getquote(type="bran",userid=binfo["userid"]))
        return
    else:        
        if binfo["subc"]=="passre":
            requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":7,"data":{"components":[]}})
            c=requests.post(f"{baseurl}webhooks/{aid}/{token}",headers={"Content-Type": "application/json"},json={"content":"<a:typing:597589448607399949>  Searching for Quotes..."})
            a=qfinder.qres(query=binfo["query"],userid=binfo["userid"])
            d=requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/{c.json()['id']}",headers={"Content-Type": "application/json"},json=a)
            print(d.json())
        else:
            requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":7,"data":{"content":"<a:typing:597589448607399949>  Searching again...","embeds":[],"components":[]}})
            a=qfinder.qres(query=binfo["query"],userid=binfo["userid"])
            requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=a)
        return
