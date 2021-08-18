import traceback,json
from random import shuffle
from imports.utils.quotes import qlogic

def qres(query:str,userid:str):
    ftext="Quotes from Wikiquote"
    ficon="https://cdn.discordapp.com/attachments/789798190353743874/794948919594450944/QqJDyLtUbgAAAAASUVORK5CYII.png"
    thum="https://cdn.discordapp.com/attachments/789798190353743874/796948926590615572/oie_transparent_1.png"
    Search=qlogic.qfind(query=query)
    if Search[0]=="NoAuthorFound":
        jsn={
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
    elif Search[0]=="NoQuoteFound":
        Titles=Search[1]
        shuffle(Titles)
        Suggestions=[]
        for i in Titles:
            if len(Suggestions)<26:
                Suggestions.append({"label":i,"value":i,"emoji":{"name":"qauthor","id":"847687409034330132"}})
            else:
                break
        print(Suggestions)
        jsn={
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
                    "type": 3,
                    "custom_id": json.dumps({"sfn":"quote","subc":"sgtns","userid":userid}),
                    "placeholder": "🔎 Try searching",
                    "options": Suggestions
                }]
            }]
        }
    elif Search[0]=="Success":      
        jsn={
            "embeds": [
                {
                    "title": f"Search result for query: **'{query}'**",
                    "description": f"{Search[1]}\n- {Search[2]}",
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
                    "emoji": {
                        "name": "quote",
                        "id": "847687355481718794"
                    },
                    "custom_id": json.dumps({"bfn":"quote","subc":"passre","userid":userid})
                }]
            }]
        }
    return jsn
