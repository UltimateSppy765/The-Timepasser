from random import choice
import requests,json,traceback

baseurl="https://discord.com/api/v9/"
tings=["Drank too much juice...","Lazed around too much...","**Started studying**...","Looked at myself in the mirror...","Walked into the 'I give up Pit'...","**Someone asked me whether I was smart...**"]

def err(error:str):
    return {
        "type": 4,
        "data": {
            "content": f"> <:tickNo:315009174163685377> Sorry, an error has occured. Either your input has caused this error or it is from my side.\n> **__Error Code:__** {choice(tings)}",
            "embeds": [
                {
                    "description": f":clipboard: **Please report this error to the bot developers:**\n```py\n{error}\n```",
                    "color": 3092791,
                    "footer": {
                        "text": "For finding the bot developers, run \"/aboutme\".",
                        "icon_url": "https://cdn.discordapp.com/avatars/791153806058455075/4fc80d3c7cf9bf40fba1d461e1ad5c54.webp"
                    }
                }
            ]
        }
    }

def existnt(cname:str):
    return {
        "type": 4,
        "data": {
            "flags": 64,
            "content": f"> <:tickNo:315009174163685377> Sorry to say but the command you tried to use (which is `/{cname}`) is currently unavailable (and probably under development or modification :tools:).\n> Please try again later."
        }
    }

def dmerr():
    return {
        "type": 4,
        "data": {
            "flags": 64,
            "content": "> <:tickNo:315009174163685377> Sorry, my commands do not work in DMs, please use them in a guild."
        }
    }

def eval(token:str,iid:str,sc:str,aid:str,jsn):
    try:
        jsa=json.loads(jsn)
    except:
        jsnerr={
            "type": 4,
            "data": {
                "flags": 64,
                "content": "<:tickNo:315009174163685377> The input given was not a valid JSON, please enter a valid JSON."
            }
        }
        requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json=jsnerr)
        return 
    else:
        if sc=="followup":
            jsp={
                "type": 4,
                "data": {
                    "content": "<a:typing:597589448607399949>  Processing Request..."
                }
            }
            requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json=jsp)
            res=requests.post(f"{baseurl}webhooks/{aid}/{token}",headers={"Content-Type": "application/json"},json=jsa)
            if res.status_code==200:
                requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json={"content": f"<:tickYes:315009125694177281> Successfully evaluated JSON.```\nReturned Status Code: {res.status_code}\n```"})
                return 
            else:
                jsnerr={
                    "content": f"<:tickNo:315009174163685377> Your evaluation failed, detailed information given below:```\nReturned Status Code: {res.status_code}\n{res.json()}\n```"
                }
                requests.patch(f"{baseurl}webhooks/{aid}/{token}/messages/@original",json=jsnerr)
                return 
        elif sc=="original":
            res=requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json=jsa)
            if res.status_code==200:
                return
            else:
                jsnerr={
                    "type":  4,
                    "data": {
                        "content": f"<:tickNo:315009174163685377> Your evaluation failed, detailed information given below:```\nReturned Status Code: {res.status_code}\n{res.json()}\n```"
                    }
                }
                requests.post(f"{baseurl}interactions/{iid}/{token}/callback",json=jsnerr)
                return