from imports.utils import avpic

def uscmd(usid,av,uname:str,disc):
    return {
        "type": 4,
        "data": {
            "embeds": [
                {
                    "title": f":mirror: {uname}'s Avatar:",
                    "color": 3092791,
                    "image": {
                        "url": f"{avpic.usav(id=usid,discid=disc,av=av)}?size=256"
                    }
                }
            ]
        }
    }
