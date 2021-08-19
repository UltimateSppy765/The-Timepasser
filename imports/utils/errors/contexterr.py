def contexterr(r,traceback):
    if r.json["data"]["type"]==2:
        ctxtype="USER"
    elif r.json["data"]["type"]==3:
        ctxtype="MESSAGE"
    cmdname=r.json["data"]["name"]
    itrid=r.json["id"]
    a=int(itrid) >> 22
    Tstamp=a+1420070400000
    Content=f"Exception raised in context command: `{cmdname}`" 
    Embed=[{
        "title": "🔴 Traceback Called:",
        "color": 15745587,
        "description": f"```py\n{traceback}\n```",
        "fields": [{
            "name": "Interaction Created at:",
            "value": f"<t:{Tstamp}:F>",
            "inline": True
          },
          {
            "name": "Status:",
            "value": "Not Fixed",
            "inline": True
          },
          {
            "name": "Context Command Type:",
            "value": f"`{ctxtype}`",
            "inline": True
        }]
    }]
    return [Content,Embed]
