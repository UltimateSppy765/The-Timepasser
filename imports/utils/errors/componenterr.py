import json

def componenterr(r,traceback):
    cjson=json.loads(r.json["data"]["custom_id"])
    if r.json["data"]["component_type"]==2:
        cname=cjson["bfn"]
        ctype="Button"
    elif r.json["data"]["component_type"]==3:
        cname=cjson["sfn"]
        ctype="Select Menu"
    itrid=r.json["id"]
    a=int(itrid) >> 22
    Tstamp=a+1420070400000
    Content=f"Exception raised in message component with identifier: `{cname}`" 
    Embed=[{
        "title": "🔴 Traceback Called:",
        "color": 15745587,
        "description": f"```py\n{traceback}\n```",
        "fields": [{
            "name": "Interaction Created at:",
            "value": f"<t:{Tstamp/1000}:F>",
            "inline": True
          },
          {
            "name": "Status:",
            "value": "Not Fixed",
            "inline": True
          },
          {
            "name": "Component Type:",
            "value": f"`{ctype}`",
            "inline": True
        }]
    }]
    return [Content,Embed]
