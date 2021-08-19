import os,json,traceback
from imports.utils.errors import slasherr,contexterr,componenterr

baseurl=os.environ['BASE_URL']
wid=os.environ['ERROR_WEBHOOK_ID']
wtoken=os.environ['ERROR_WEBHOOK_TOKEN']

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
                "options": [{"label":"Mark as fixed","value":"markfixed","description":"Marks the error as fixed.","emoji":{"name":"tick","id":"847861518195884063"}},{"label":"Delete Error","value":"delerr","description":"Deletes the error.","emoji":{"name":"trashcan","id":"877957522026287134"}}]
            }]
        }]
    }
    requests.post(f"{baseurl}webhooks/{wid}/{wtoken}?wait=true",json=jsn)
    return
