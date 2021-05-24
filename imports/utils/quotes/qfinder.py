import traceback
from imports.utils.quotes import qlogic

def qres(query:str,userid:str):
    ftext="Quotes from Wikiquote"
    ficon="https://cdn.discordapp.com/attachments/789798190353743874/794948919594450944/QqJDyLtUbgAAAAASUVORK5CYII.png"
    thum="https://cdn.discordapp.com/attachments/789798190353743874/796948926590615572/oie_transparent_1.png"
    try:
        quot=qlogic.qfind(query=query)
    except Exception as l:
        ename=type(l).__name__
        if ename=="NoAuthorFound":
            json={
                "content": "I tried searching, but...",
                "embeds": [
                    {
                        "title": f"No result found for query: **'{query}'**",
                        "description": "Sorry, your query didn't work. Please try with a different one.",
                        "color": 3092791,
                        "thumbnail": {
                            "url": thum
                        },
                        "footer": {
                            "text": ftext,
                            "icon_url": ficon
                        }
                    }
                ]
            }
        elif ename=="NoQuoteFound":
            json={
                "content": "I tried searching, but...",
                "embeds": [
                    {
                        "title": f"No result for query: **'{query}'**",
                        "description": "Sorry, I couldn't find a quote for the given query. Please try again.",
                        "color": 3092791,
                        "thumbnail": {
                            "url": thum
                        },
                        "footer": {
                            "text": ftext,
                            "icon_url": ficon
                        }
                    }
                ],
                "components": [{
                    "type": 1,
                    "components": [{
                        "type": 2,
                        "style": 2,
                        "label": "Try Again",
                        "custom_id": json.dumps({"bfn":"quote","subc":"failre","userid":userid})
                    }]
                }]
            }
            print(json)
        else:
            return misc.err(traceback.format_exc())
    else:
        qt=quot[0]
        autor=quot[1]         
        json={
            "embeds": [
                {
                    "content": "Here's what I found:",
                    "title": f"Search result for query: **'{query}'**",
                    "description": f"{qt}\n- {autor}",
                    "color": 3092791,
                    "thumbnail": {
                        "url": thum
                    },
                    "footer": {
                        "text": ftext,
                        "icon_url": ficon
                    }
                }
            ],
            "components": [{
                "type": 1,
                "components": [{
                    "type": 2,
                    "style": 1,
                    "label": "Search Again!",
                    "custom_id": json.dumps({"bfn":"quote","subc":"passre","userid":userid})
                }]
            }]
        }
    return json
