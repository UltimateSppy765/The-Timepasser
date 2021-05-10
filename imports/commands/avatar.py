from imports.utils import usav
import requests,os

baseurl=os.environ['BASE_URL']

def avatar(us,uname:str,id:str,disc:str,av:str):
    if us is None:
        usname=uname
        avurl=notcmd.usav(id=id,discid=disc,av=av)
    else:
        res=requests.get(f"{baseurl}users/{us}",headers={"Authorization":f"Bot {os.environ['BOT_TOKEN']}"})
        smth=res.json()
        av1=smth["avatar"]
        disc1=smth["discriminator"]
        usname=smth["username"]
        avurl=notcmd.usav(id=us,discid=disc1,av=av1)
    return {
        "type": 4,
        "data": {
            "embeds": [
                {
                    "title": f":mirror: {usname}'s Avatar:",
                    "color": 3092791,
                    "image": {
                        "url": f"{avurl}?size=256"
                    }
                }
            ]
        }
    }
