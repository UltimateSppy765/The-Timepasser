import os,wikiquote,requests,json
from imports.utils.quotes import qfinder
from imports.utils import perspective

baseurl=os.environ['BASE_URL']

def cmd(subc:str,query:str,token:str,aid:str,iid:str,usid:str):
    if subc=="get":
        if query=="qotd":
            titl="Quote of the Day:"
            ftext="Quotes from Wikiquote"
            ficon="https://cdn.discordapp.com/attachments/789798190353743874/794948919594450944/QqJDyLtUbgAAAAASUVORK5CYII.png"
            (qt,autor)=wikiquote.quote_of_the_day()
        elif query=="random":
            titl="Random Quote:"
            ftext="Powered by Quotable"
            ficon="https://cdn.discordapp.com/attachments/839610105858752522/839610124271484938/download.jpeg"
            res=requests.get("http://api.quotable.io/random").json()
            qt=res["content"]
            autor=res["author"]
        return {
            "type": 4,
            "data": {
                "flags": 64,
                "embeds": [
                    {
                        "color": 3092791,
                        "title": titl,
                        "description": f"{qt}\n- {autor}",
                        "thumbnail": {
                            "url": "https://cdn.discordapp.com/attachments/789798190353743874/796948926590615572/oie_transparent_1.png"
                        },
                        "footer": {
                            "text": ftext,
                            "icon_url": ficon
                        }
                    }
                ]
            },
            "components": [] if query=="qotd" else [{"type":1,"components":["type":2,"style":1,"label":"Another One!","custom_id":json.dumps({"bfn":"quote","subc":"getran","userid":usid})]}]
        }
    else:
        a=perspective.analyse(cont=query)
        if a is not None:
            return a
        requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json={"type":5})
        jsr=qfinder.qres(query=query)
        requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=jsr)
        return
