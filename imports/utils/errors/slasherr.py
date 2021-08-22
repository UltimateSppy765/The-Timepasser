def slasherr(r,traceback):
    cmdname=r.json["data"]["name"]
    itrid=r.json["id"]
    a=int(itrid) >> 22
    Tstamp=a+1420070400000
    Content=f"Exception raised in slash command: `/{cmdname}`" 
    Embed=[{
        "title": "🔴 Traceback Called:",
        "color": 15745587,
        "description": f"```py\n{traceback}\n```",
        "fields": [{
            "name": "Interaction Created at:",
            "value": f"<t:{Tstamp//1000}:F>",
            "inline": True
          },
          {
            "name": "Status:",
            "value": "Not Fixed",
            "inline": True
        }]
    }]
    return [Content,Embed]
