import requests,os,re
from imports.utils.botowners import ownerids
from imports.utils import fail

baseurl=os.environ["BASE_URL"]
wtoken=os.environ["ERROR_WEBHOOK_TOKEN"]
wid=os.environ["ERROR_WEBHOOK_ID"]

def select(msg,action:str,aid:str,iid:str,token:str,uid:str):
    if uid not in ownerids():
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "content": "<:tickNo:315009174163685377> You do not have the permission to use this."
            }
        }
    if action=="delerr":
        requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":5,"data":{"flags":64}})
        a=requests.delete(f"{baseurl}webhooks/wid/wtoken/messages/{msg['id']}")
        pattern=r'**Interaction ID:**\ (.?)\n'
        itrid=re.search(pattern,msg["content"]).group(1)
        if a.status_code==204:
            jsn={"content":f"<:tick:847861518195884063> Successfully deleted error with Interaction ID: {itrid}"}
        else:
            jsn={"content":f"<:tickNo:315009174163685377> Failed to delete error with Interaction ID: {itrid} ```\n{a.json()}\n```"}
        requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=jsn)
    elif action=="markfixed":
        return fail.cfail()
