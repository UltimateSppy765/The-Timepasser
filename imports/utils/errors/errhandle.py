import os,json,traceback,requests
from imports.utils.errors import slasherr,contexterr,componenterr
from random import choice

tings=["Drank too much juice...","Lazed around too much...","**Started studying**...","Looked at myself in the mirror...","Walked into the 'I give up Pit'...","**Someone asked me whether I was smart...**"]
baseurl=os.environ['BASE_URL']
wid=os.environ['ERROR_WEBHOOK_ID']
wtoken=os.environ['ERROR_WEBHOOK_TOKEN']

def usres(r,jsnres):
    r1=requests.get(f"{baseurl}webhooks/{r.json['application_id']}/{r.json['token']}/messages/@original")
    try:
        msgflags=r1["flags"]
        print(msgflags)
    except:
        requests.post(f"{baseurl}interactions/{r.json['id']}/{r.json['token']}/callback",json={"type":4,"data":jsnres})
        return
    perms= 1 << 6 | 1 << 7
    if (msgflags & perms) == perms:
        requests.patch(f"{baseurl}webhooks/{r.json['application_id']}/{r.json['token']}/messages/@original",headers={"Content-Type":"application/json"},json=jsnres)
        return
    elif perms & 1 << 7:
        requests.delete(f"{baseurl}webhooks/{r.json['application_id']}/{r.json['token']}/messages/@original")
        requests.post(f"{baseurl}webhooks/{r.json['application_id']}/{r.json['token']}",headers={"Content-Type":"application/json"},json=jsnres)
        return
    else:
        requests.post(f"{baseurl}webhooks/{r.json['application_id']}/{r.json['token']}",headers={"Content-Type":"application/json"},json=jsnres)
        return

def handle(r,t):
    if r.json["type"]==3:
        errlog=componenterr.componenterr(r=r,traceback=t)
    elif r.json["type"]==2:
        if r.json["data"]["type"]==1:
            errlog=slasherr.slasherr(r=r,traceback=t)
        elif r.json["data"]["type"] in [2,3]:
            errlog=contexterr.contexterr(r=r,traceback=t)
    jsn={
        "content": f"\n**Interaction ID:** {r.json['id']}\n"+errlog[0],
        "embeds": errlog[1],
        "components": [{
            "type": 1,
            "components": [{
                "type": 3,
                "custom_id": json.dumps({"sfn":"errlogaction","errid":r.json['id']}),
                "placeholder": "Actions you can perform",
                "options": [{"label":"Mark as fixed","value":"markfixed","description":"Marks the error as fixed.","emoji":{"name":"tick","id":"847861518195884063"}},{"label":"Working on Fix","value":"fixing","description":"Marks the error as being worked on.","emoji":{"name":"inworks","id":"878990445286391809"}},{"label":"Delete Error","value":"delerr","description":"Deletes the error.","emoji":{"name":"trashcan","id":"877957522026287134"}}]
            }]
        }]
    }
    requests.post(f"{baseurl}webhooks/{wid}/{wtoken}?wait=true",json=jsn)
    jsn2={
        "flags":64,
        "content":f"<:tickNo:315009174163685377> Snap. I ran into an issue while attempting to do your bidding.\n**Reason:** _{choice(tings)}_\nYour interaction ID is `{r.json['id']}`. Please use this ID as reference if you wish to report this bug to our bot devs who can be found in their community server linked in the button below.",
        "components": [{
            "type": 1,
            "components": [{
                "type": 2,
                "style": 5,
                "label": "Our Community Server",
                "url": "https://discord.gg/JXGe9MfXPF"
            }]
        }]
    }
    usres(r=r,jsnres=jsn2)
    return
