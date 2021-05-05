import requests
from imports import misc
def anipic(anim,animal:str):
    print(animal)
    if animal=="fox":
        if anim==False:
            foxy=requests.get("https://randomfox.ca/floof").json()
            url=foxy["image"]
            cont=":fox: Here's a fox pic for you."
            ftext="Powered by RandomFox"
            ficon="https://cdn.discordapp.com/attachments/789798190353743874/798118721091928074/logo.png"
            greet="Ring-ding-ding-ding-dingeringeding!"
        else:
            return misc.existnt(cname="/anipic")
    elif animal=="cat":
        return misc.existnt(cname="/anipic")
    elif animal=="dog":
        return misc.existnt(cname="/anipic")
    return {
        "type": 4,
        "data": {
            "content": cont,
            "embeds": [
                {
                    "title": greet,
                    "color": 3092791,
                    "image": {
                        "url": url
                    },
                    "footer": {
                        "text": ftext,
                        "icon_url": ficon
                    }
                }
            ]
         }
    }
