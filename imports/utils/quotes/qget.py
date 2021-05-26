import wikiquote,requests,json,traceback

def getquote(type:str,userid:str):
    if type=="qotd":
        (qt,autor)=wikiquote.quote_of_the_day()
        try:
            return {
            "embeds": [
                {
                    "color": 3092791,
                    "title": "Quote of the Day:",
                    "description": f"{qt}\n- {autor}",
                    "thumbnail": {
                        "url": "https://cdn.discordapp.com/attachments/789798190353743874/796948926590615572/oie_transparent_1.png"
                    },
                    "footer": {
                        "text": "Quotes from Wikiquote",
                        "icon_url": "https://cdn.discordapp.com/attachments/789798190353743874/794948919594450944/QqJDyLtUbgAAAAASUVORK5CYII.png"
                    }
                }
            ]
        }
        except:
            print(traceback.format_exc())    
    else:
        res=requests.get("http://api.quotable.io/random").json()
        qt=res["content"]
        autor=res["author"]
        return {
            "embeds": [
                {
                    "color": 3092791,
                    "title": "Random Quote:",
                    "description": f"{qt}\n- {autor}",
                    "thumbnail": {
                        "url": "https://cdn.discordapp.com/attachments/789798190353743874/796948926590615572/oie_transparent_1.png"
                    },
                    "footer": {
                        "text": "Powered by Quotable API",
                        "icon_url": "https://cdn.discordapp.com/attachments/839610105858752522/839610124271484938/download.jpeg"
                    }
                }
            ],
            "components": [{
                "type": 1,
                "components":[{
                    "type": 2,
                    "style": 1,
                    "label": "Another One!",
                    "custom_id": json.dumps({"bfn":"quote","subc":"getran","userid":userid})
                  },
                  {
                    "type": 2,
                    "style": 2,
                    "label": "Search Quote from Author",
                    "custom_id": json.dumps({"bfn":"quote","subc":"passre","userid":userid,"query":autor})
                }]
            }]
        }
