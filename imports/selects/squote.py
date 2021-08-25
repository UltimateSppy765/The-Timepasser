import os,requests
from imports.utils.quotes import qfinder

baseurl=os.environ['BASE_URL']

def select(query:str,sinfo,usid:str,aid:str,token:str,iid:str):
    if usid!=sinfo["userid"]:
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": "<:tickNo:315009174163685377> You can't use that select menu on someone else's message, please try on your own one."
            }
        }
    query=query.strip()
    requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":7,"data":{"components":[],"embeds":[{"title":f":mag: Searching for Query: '{query}'","color":3092791}]}})
    requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=qfinder.qres(query=query,userid=sinfo["userid"]))
    return
