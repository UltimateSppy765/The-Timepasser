import traceback
from imports.utils import qlogic

def qres(query:str):
    ftext="Quotes from Wikiquote"
    ficon="https://cdn.discordapp.com/attachments/789798190353743874/794948919594450944/QqJDyLtUbgAAAAASUVORK5CYII.png"
    thum="https://cdn.discordapp.com/attachments/789798190353743874/796948926590615572/oie_transparent_1.png"
    try:
        quot=qlogic.qfind(query=query)
    except Exception as l:
        ename=type(l).__name__
        if ename=="NoAuthorFound":
            json={
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
                ]
            }
        else:
            return misc.err(traceback.format_exc())
    else:
        qt=quot[0]
        autor=quot[1]         
        json={
            "embeds": [
                {
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
            ]
        }
    return json
