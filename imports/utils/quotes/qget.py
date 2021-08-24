import wikiquote,requests,json,traceback

def getquote(type:str,userid:str):
    if type=="qotd":
        (qt,autor)=wikiquote.quote_of_the_day()
        Suggestions=[]
        for i in wikiquote.random_titles(max_titles=10):
            Suggestions.append({"label":i,"value":i,"emoji":{"name":"qauthor","id":"847687409034330132"}})
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
            ],
            "components": [{
                "type": 1,
                "components": [{
                    "type": 3,
                    "custom_id": json.dumps({"sfn":"quote","subc":"sgtns","userid":userid}),
                    "placeholder": "🔎 Try searching",
                    "options": Suggestions
                }]
              },
              {
                "type": 1,
                "components":[{
                    "type": 2,
                    "style": 1,
                    "emoji": {
                        "name": "qauthor",
                        "id": "847687409034330132"
                    },
                    "label": "Search Quote from Author",
                    "custom_id": json.dumps({"bfn":"quote","subc":"passre","userid":userid})
                }]
            }]
        } 
    else:
        res=requests.get("http://api.quotable.io/random").json()
        qt=res["content"]
        autor=res["author"]
        Suggestions=[]
        for i in wikiquote.random_titles(max_titles=10):
            Suggestions.append({"label":i,"value":i,"emoji":{"name":"qauthor","id":"847687409034330132"}})
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
                "components": [{
                    "type": 3,
                    "custom_id": json.dumps({"sfn":"quote","subc":"sgtns","userid":userid}),
                    "placeholder": "🔎 Try searching",
                    "options": Suggestions
                }]
              },
              {
                "type": 1,
                "components":[{
                    "type": 2,
                    "style": 1,
                    "emoji": {
                        "name": "quote",
                        "id": "847687355481718794"
                    },
                    "label": "Another One!",
                    "custom_id": json.dumps({"bfn":"quote","subc":"getran","userid":userid})
                  },
                  {
                    "type": 2,
                    "style": 2,
                    "label": "Search Quote from Author",
                    "emoji": {
                        "name": "qauthor",
                        "id": "847687409034330132"
                    },
                    "custom_id": json.dumps({"bfn":"quote","subc":"passre","userid":userid})
                }]
            }]
        }
